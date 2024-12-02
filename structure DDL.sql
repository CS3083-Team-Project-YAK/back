SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for draft
-- ----------------------------
DROP TABLE IF EXISTS `draft`;
CREATE TABLE `draft` (
  `draftID` decimal(8,0) NOT NULL,
  `leagueID` decimal(8,0) DEFAULT NULL,
  `draft_date` date DEFAULT NULL,
  `draft_order` char(1) DEFAULT NULL,
  `draft_status` char(1) DEFAULT NULL,
  PRIMARY KEY (`draftID`),
  KEY `leagueID` (`leagueID`),
  CONSTRAINT `draft_ibfk_1` FOREIGN KEY (`leagueID`) REFERENCES `league` (`leagueID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for draft_pick
-- ----------------------------
DROP TABLE IF EXISTS `draft_pick`;
CREATE TABLE `draft_pick` (
  `draftID` decimal(8,0) NOT NULL,
  `playerID` decimal(8,0) NOT NULL,
  PRIMARY KEY (`draftID`,`playerID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `draft_pick_ibfk_1` FOREIGN KEY (`draftID`) REFERENCES `draft` (`draftID`),
  CONSTRAINT `draft_pick_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for event
-- ----------------------------
DROP TABLE IF EXISTS `event`;
CREATE TABLE `event` (
  `eventID` decimal(10,0) NOT NULL,
  `matchID` decimal(8,0) DEFAULT NULL,
  `event_type` char(3) DEFAULT NULL,
  `event_time` time DEFAULT NULL,
  `impact_on_points` decimal(4,2) DEFAULT 0.00,
  PRIMARY KEY (`eventID`),
  KEY `matchID` (`matchID`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`matchID`) REFERENCES `matches` (`matchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for league
-- ----------------------------
DROP TABLE IF EXISTS `league`;
CREATE TABLE `league` (
  `leagueID` decimal(8,0) NOT NULL,
  `commissioner` decimal(8,0) DEFAULT NULL,
  `league_name` varchar(30) NOT NULL,
  `league_type` char(1) NOT NULL,
  `max_teams` decimal(2,0) NOT NULL DEFAULT 10,
  `draft_date` date DEFAULT NULL,
  PRIMARY KEY (`leagueID`),
  KEY `commissioner` (`commissioner`),
  CONSTRAINT `league_ibfk_1` FOREIGN KEY (`commissioner`) REFERENCES `user` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for matches
-- ----------------------------
DROP TABLE IF EXISTS `matches`;
CREATE TABLE `matches` (
  `matchID` decimal(8,0) NOT NULL,
  `team1ID` decimal(8,0) DEFAULT NULL,
  `team2ID` decimal(8,0) DEFAULT NULL,
  `winner` decimal(8,0) DEFAULT NULL,
  `match_date` date DEFAULT NULL,
  `final_score` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`matchID`),
  KEY `team1ID` (`team1ID`),
  KEY `team2ID` (`team2ID`),
  KEY `winner` (`winner`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`team1ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`team2ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`winner`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for player
-- ----------------------------
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
  `playerID` decimal(8,0) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `sport` char(3) NOT NULL,
  `position` varchar(3) DEFAULT NULL,
  `teamID` decimal(8,0) DEFAULT NULL,
  `real_team` varchar(50) DEFAULT NULL,
  `fantasy_points` decimal(6,2) DEFAULT 0.00,
  `availability_status` char(1) DEFAULT NULL,
  PRIMARY KEY (`playerID`),
  KEY `teamID` (`teamID`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for player_event
-- ----------------------------
DROP TABLE IF EXISTS `player_event`;
CREATE TABLE `player_event` (
  `eventID` decimal(10,0) NOT NULL,
  `playerID` decimal(8,0) NOT NULL,
  PRIMARY KEY (`eventID`,`playerID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `player_event_ibfk_1` FOREIGN KEY (`eventID`) REFERENCES `event` (`eventID`),
  CONSTRAINT `player_event_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for player_statistics
-- ----------------------------
DROP TABLE IF EXISTS `player_statistics`;
CREATE TABLE `player_statistics` (
  `statisticsID` decimal(10,0) NOT NULL,
  `playerID` decimal(8,0) DEFAULT NULL,
  `match_date` date DEFAULT NULL,
  `performance_stats` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`performance_stats`)),
  `injury_status` char(1) DEFAULT NULL,
  PRIMARY KEY (`statisticsID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `player_statistics_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for team
-- ----------------------------
DROP TABLE IF EXISTS `team`;
CREATE TABLE `team` (
  `teamID` decimal(8,0) NOT NULL,
  `leagueID` decimal(8,0) DEFAULT NULL,
  `owner` decimal(8,0) DEFAULT NULL,
  `total_points` decimal(6,2) DEFAULT 0.00,
  `ranking` decimal(8,0) DEFAULT NULL,
  `status` char(1) DEFAULT NULL,
  PRIMARY KEY (`teamID`),
  KEY `leagueID` (`leagueID`),
  KEY `owner` (`owner`),
  CONSTRAINT `team_ibfk_1` FOREIGN KEY (`leagueID`) REFERENCES `league` (`leagueID`),
  CONSTRAINT `team_ibfk_2` FOREIGN KEY (`owner`) REFERENCES `user` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for trade
-- ----------------------------
DROP TABLE IF EXISTS `trade`;
CREATE TABLE `trade` (
  `tradeID` decimal(10,0) NOT NULL,
  `trade_date` date DEFAULT NULL,
  `team1ID` decimal(8,0) DEFAULT NULL,
  `team2ID` decimal(8,0) DEFAULT NULL,
  `player1ID` decimal(8,0) DEFAULT NULL,
  `player2ID` decimal(8,0) DEFAULT NULL,
  PRIMARY KEY (`tradeID`),
  KEY `team1ID` (`team1ID`),
  KEY `team2ID` (`team2ID`),
  KEY `player1ID` (`player1ID`),
  KEY `player2ID` (`player2ID`),
  CONSTRAINT `trade_ibfk_1` FOREIGN KEY (`team1ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `trade_ibfk_2` FOREIGN KEY (`team2ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `trade_ibfk_3` FOREIGN KEY (`player1ID`) REFERENCES `player` (`playerID`),
  CONSTRAINT `trade_ibfk_4` FOREIGN KEY (`player2ID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userID` decimal(8,0) NOT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  `password` varchar(64) NOT NULL,
  `profile_setting` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`profile_setting`)),
  PRIMARY KEY (`userID`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email_address` (`email_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for waiver
-- ----------------------------
DROP TABLE IF EXISTS `waiver`;
CREATE TABLE `waiver` (
  `waiverID` decimal(8,0) NOT NULL,
  `teamID` decimal(8,0) DEFAULT NULL,
  `playerID` decimal(8,0) DEFAULT NULL,
  `waiver_order` decimal(3,0) DEFAULT NULL,
  `waiver_status` char(1) DEFAULT NULL,
  `pickup_date` date DEFAULT NULL,
  PRIMARY KEY (`waiverID`),
  KEY `teamID` (`teamID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `waiver_ibfk_1` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `waiver_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Procedure structure for process_waiver
-- ----------------------------
DROP PROCEDURE IF EXISTS `process_waiver`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `process_waiver`(
    IN waiver_id DECIMAL(8, 0),
    IN action CHAR(1)
)
BEGIN
    DECLARE player_id DECIMAL(8, 0);
    DECLARE team_id DECIMAL(8, 0);

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
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table event
-- ----------------------------
DROP TRIGGER IF EXISTS `update_fantasy_points`;
delimiter ;;
CREATE TRIGGER `league`.`update_fantasy_points` AFTER INSERT ON `event` FOR EACH ROW BEGIN
    DECLARE current_points DECIMAL(6, 2);
    DECLARE player_id DECIMAL(8, 0);
    DECLARE done BOOLEAN DEFAULT FALSE;

    -- Cursor to retrieve all player IDs associated with the new event
    DECLARE player_cursor CURSOR FOR
    SELECT playerID
    FROM player_event
    WHERE eventID = NEW.eventID;

    -- Declare a handler for the end of the cursor loop
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN player_cursor;

    -- Iterate through the cursor
    read_loop: LOOP
        FETCH player_cursor INTO player_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Retrieve the current fantasy points of the player
        SELECT fantasy_points INTO current_points
        FROM player
        WHERE playerID = player_id;

        -- Update the player's fantasy points
        UPDATE player
        SET fantasy_points = current_points + NEW.impact_on_points
        WHERE playerID = player_id;
    END LOOP;

    -- Close the cursor
    CLOSE player_cursor;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
