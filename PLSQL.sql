-- Procedure: CALL update_fantasy_points(playerID);
-- recalculates a specific player's fantasy_points by summing the impact_on_points from all events associated with that player.
DELIMITER $$

CREATE PROCEDURE update_fantasy_points(IN p_playerID INT)
BEGIN
    DECLARE total_impact DECIMAL(10,2);

    -- Calculate the total impact from all events associated with the player
    SELECT COALESCE(SUM(e.impact_on_points), 0)
    INTO total_impact
    FROM event e
    INNER JOIN player_event pe ON e.eventID = pe.eventID
    WHERE pe.playerID = p_playerID;

    -- Update the player's fantasy_points
    UPDATE player
    SET fantasy_points = total_impact
    WHERE playerID = p_playerID;
END $$

DELIMITER ;


-- Procedure: CALL update_fantasy_points_by_event(eventID);
-- recalculates the fantasy_points for all players associated with a specific event.
DELIMITER $$

CREATE PROCEDURE update_fantasy_points_by_event(IN p_eventID INT)
BEGIN
    DECLARE player_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR
        SELECT playerID FROM player_event WHERE eventID = p_eventID;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    -- Loop through all players associated with the event
    read_loop: LOOP
        FETCH cur INTO player_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Recalculate fantasy points for each player
        CALL update_fantasy_points(player_id);
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END $$

DELIMITER ;


-- Stored Procedure: Approve or Reject Waiver Requests
-- This procedure processes waiver requests by either approving or rejecting them based on the provided action.
DELIMITER $$

CREATE PROCEDURE process_waiver(
    IN waiver_id int(10),
    IN action CHAR(1)
)
BEGIN
    DECLARE player_id int(10);
    DECLARE team_id int(10);

    SELECT playerID, teamID INTO player_id, team_id
    FROM waiver
    WHERE waiverID = waiver_id;

    IF action = 'A' THEN
        UPDATE player
        SET teamID = team_id, availability_status = 'U'
        WHERE playerID = player_id;

        UPDATE waiver
        SET waiver_status = 'A'
        WHERE waiverID = waiver_id;
    ELSEIF action = 'R' THEN
        UPDATE waiver
        SET waiver_status = 'R'
        WHERE waiverID = waiver_id;
    END IF;
END $$

DELIMITER ;


-- PROCEDURE: CALL UpdateTeamRankings(leagueID) to update the rankings of teams in that league
DELIMITER $$

CREATE PROCEDURE UpdateTeamRankings(IN league INT)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE rank INT DEFAULT 0;
    DECLARE prev_points DECIMAL(6,2) DEFAULT NULL;
    DECLARE cur_teamID INT;
    DECLARE cur_points DECIMAL(6,2);

    -- Cursor to select teams in the specified league ordered by total_points DESC
    DECLARE cur CURSOR FOR
        SELECT teamID, total_points
        FROM team
        WHERE leagueID = league
        ORDER BY total_points DESC, teamID;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    -- Loop through the cursor
    read_loop: LOOP
        FETCH cur INTO cur_teamID, cur_points;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Increment rank if points differ from previous team
        IF prev_points IS NULL OR cur_points <> prev_points THEN
            SET rank = rank + 1;
        END IF;

        -- Update the team's ranking
        UPDATE team
        SET ranking = rank
        WHERE teamID = cur_teamID;

        SET prev_points = cur_points;
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END$$

DELIMITER ;