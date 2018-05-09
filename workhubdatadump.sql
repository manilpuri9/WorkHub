-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: myflaskapp
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Danny Dee','dannydee@gmail.com','dannydee','$5$rounds=535000$F4oUsICU7S0OSRp/$LrxyTyawfjCKINlBfnPZyVBaWQ1IBo97SjTx53o8Ow.'),('manil puri','manilpuri9@gmail.com','manilpuri9','hello');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workerD`
--

DROP TABLE IF EXISTS `workerD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workerD` (
  `username` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(500) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `jobtitle` varchar(40) NOT NULL,
  `experiance` text NOT NULL,
  `description` text NOT NULL,
  `likes` int(10) DEFAULT NULL,
  `dislikes` int(10) DEFAULT NULL,
  `availability` int(1) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `workerD_ibfk_1` FOREIGN KEY (`username`) REFERENCES `workers` (`username`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workerD`
--

LOCK TABLES `workerD` WRITE;
/*!40000 ALTER TABLE `workerD` DISABLE KEYS */;
INSERT INTO `workerD` VALUES ('manilpuri9','manil puri','manilpuri9@gmail.com','Kathmandu,Nepal','IT','Web Developer','3','Great coder',100,4,1,NULL),('yogesh123','Yogesh Manni','yogesh_manni21@gmail.com','Chitkara University Himachal Pradesh, Barautiwala Highway Baddi','blaaaa','blaaaa','1','good Driver',12345,12,1,7580);
/*!40000 ALTER TABLE `workerD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workerR`
--

DROP TABLE IF EXISTS `workerR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workerR` (
  `username` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `comment` text,
  PRIMARY KEY (`username`),
  CONSTRAINT `workerR_ibfk_1` FOREIGN KEY (`username`) REFERENCES `workers` (`username`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workerR`
--

LOCK TABLES `workerR` WRITE;
/*!40000 ALTER TABLE `workerR` DISABLE KEYS */;
INSERT INTO `workerR` VALUES ('manilpuri9','jackson','he is highly skilled');
/*!40000 ALTER TABLE `workerR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workers`
--

DROP TABLE IF EXISTS `workers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workers` (
  `username` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(180) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workers`
--

LOCK TABLES `workers` WRITE;
/*!40000 ALTER TABLE `workers` DISABLE KEYS */;
INSERT INTO `workers` VALUES ('manilpuri9','manil puri','manilpuri9@gmail.com',''),('yogesh123','Yogesh Manni','yogesh_manni21@gmail.com','$5$rounds=535000$4f2LERibDMCCkxL2$6Im2GzA4ohnPRjbpKbVr.nQOJGY6zxI/3RIG39M.9KD');
/*!40000 ALTER TABLE `workers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-09 18:16:38
