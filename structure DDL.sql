-- ----------------------------
-- Table structure for draft
-- ----------------------------
DROP TABLE IF EXISTS `draft`;
CREATE TABLE `draft` (
  `draftID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `leagueID` int(10) unsigned DEFAULT NULL,
  `draft_date` date DEFAULT NULL,
  `draft_order` char(1) DEFAULT NULL,
  `draft_status` char(1) DEFAULT NULL,
  PRIMARY KEY (`draftID`),
  KEY `leagueID` (`leagueID`),
  CONSTRAINT `draft_ibfk_1` FOREIGN KEY (`leagueID`) REFERENCES `league` (`leagueID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for draft_pick
-- ----------------------------
DROP TABLE IF EXISTS `draft_pick`;
CREATE TABLE `draft_pick` (
  `draftID` int(10) unsigned NOT NULL,
  `playerID` int(10) unsigned NOT NULL,
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
  `eventID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `matchID` int(10) unsigned DEFAULT NULL,
  `event_type` char(3) DEFAULT NULL,
  `event_time` time DEFAULT NULL,
  `impact_on_points` decimal(4,2) DEFAULT 0.00,
  PRIMARY KEY (`eventID`),
  KEY `matchID` (`matchID`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`matchID`) REFERENCES `matches` (`matchID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for league
-- ----------------------------
DROP TABLE IF EXISTS `league`;
CREATE TABLE `league` (
  `leagueID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `commissioner` int(10) unsigned DEFAULT NULL,
  `league_name` varchar(30) NOT NULL,
  `league_type` char(1) NOT NULL,
  `max_teams` tinyint(3) unsigned NOT NULL DEFAULT 10,
  `draft_date` date DEFAULT NULL,
  PRIMARY KEY (`leagueID`),
  KEY `commissioner` (`commissioner`),
  CONSTRAINT `league_ibfk_1` FOREIGN KEY (`commissioner`) REFERENCES `user` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for matches
-- ----------------------------
DROP TABLE IF EXISTS `matches`;
CREATE TABLE `matches` (
  `matchID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `team1ID` int(10) unsigned DEFAULT NULL,
  `team2ID` int(10) unsigned DEFAULT NULL,
  `winner` int(10) unsigned DEFAULT NULL,
  `match_date` date DEFAULT NULL,
  `final_score` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`matchID`),
  KEY `team1ID` (`team1ID`),
  KEY `team2ID` (`team2ID`),
  KEY `winner` (`winner`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`team1ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`team2ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`winner`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for player
-- ----------------------------
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
  `playerID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `full_name` varchar(50) NOT NULL,
  `sport` char(3) NOT NULL,
  `position` varchar(3) DEFAULT NULL,
  `teamID` int(10) unsigned DEFAULT NULL,
  `real_team` varchar(50) DEFAULT NULL,
  `fantasy_points` decimal(6,2) DEFAULT 0.00,
  `availability_status` char(1) DEFAULT NULL,
  PRIMARY KEY (`playerID`),
  KEY `teamID` (`teamID`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for player_event
-- ----------------------------
DROP TABLE IF EXISTS `player_event`;
CREATE TABLE `player_event` (
  `eventID` bigint(20) unsigned NOT NULL,
  `playerID` int(10) unsigned NOT NULL,
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
  `statisticsID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `playerID` int(10) unsigned DEFAULT NULL,
  `match_date` date DEFAULT NULL,
  `performance_stats` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`performance_stats`)),
  `injury_status` char(1) DEFAULT NULL,
  PRIMARY KEY (`statisticsID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `player_statistics_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for team
-- ----------------------------
DROP TABLE IF EXISTS `team`;
CREATE TABLE `team` (
  `teamID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `leagueID` int(10) unsigned DEFAULT NULL,
  `owner` int(10) unsigned DEFAULT NULL,
  `total_points` decimal(6,2) DEFAULT 0.00,
  `ranking` int(10) unsigned DEFAULT NULL,
  `status` char(1) DEFAULT NULL,
  PRIMARY KEY (`teamID`),
  KEY `leagueID` (`leagueID`),
  KEY `owner` (`owner`),
  CONSTRAINT `team_ibfk_1` FOREIGN KEY (`leagueID`) REFERENCES `league` (`leagueID`),
  CONSTRAINT `team_ibfk_2` FOREIGN KEY (`owner`) REFERENCES `user` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for trade
-- ----------------------------
DROP TABLE IF EXISTS `trade`;
CREATE TABLE `trade` (
  `tradeID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `trade_date` date DEFAULT NULL,
  `team1ID` int(10) unsigned DEFAULT NULL,
  `team2ID` int(10) unsigned DEFAULT NULL,
  `player1ID` int(10) unsigned DEFAULT NULL,
  `player2ID` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`tradeID`),
  KEY `team1ID` (`team1ID`),
  KEY `team2ID` (`team2ID`),
  KEY `player1ID` (`player1ID`),
  KEY `player2ID` (`player2ID`),
  CONSTRAINT `trade_ibfk_1` FOREIGN KEY (`team1ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `trade_ibfk_2` FOREIGN KEY (`team2ID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `trade_ibfk_3` FOREIGN KEY (`player1ID`) REFERENCES `player` (`playerID`),
  CONSTRAINT `trade_ibfk_4` FOREIGN KEY (`player2ID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `full_name` varchar(50) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  `password` varchar(64) NOT NULL,
  `profile_setting` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`profile_setting`)),
  PRIMARY KEY (`userID`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email_address` (`email_address`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Table structure for waiver
-- ----------------------------
DROP TABLE IF EXISTS `waiver`;
CREATE TABLE `waiver` (
  `waiverID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `teamID` int(10) unsigned DEFAULT NULL,
  `playerID` int(10) unsigned DEFAULT NULL,
  `waiver_order` smallint(5) unsigned DEFAULT NULL,
  `waiver_status` char(1) DEFAULT NULL,
  `pickup_date` date DEFAULT NULL,
  PRIMARY KEY (`waiverID`),
  KEY `teamID` (`teamID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `waiver_ibfk_1` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `waiver_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

