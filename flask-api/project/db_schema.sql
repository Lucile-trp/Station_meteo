DROP TABLE IF EXISTS sonde;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS mesure;

#
# TABLE STRUCTURE FOR: user
#

CREATE TABLE users (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `firstname` varchar(40) NOT NULL,
  `email` varchar(100) NOT NULL,
  `token` varchar(40) NOT NULL,
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `token` (`token`),
  PRIMARY KEY (`id`)
);

INSERT INTO users (`id`, `name`, `firstname`, `email`, `token`) VALUES (1, 'root', 'root', 'toortoor@toot.com', 'jesuisuntoken');

#
# TABLE STRUCTURE FOR : sonde
#

CREATE TABLE sonde ( 
  `id` int NOT NULL AUTO_INCREMENT,
  `pos_latitude` float(20) NOT NULL,
  `pos_longitude` float(20) NOT NULL,
  `sonde_name` varchar(40) NOT NULL,
  `active` boolean NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO sonde (`id`, `pos_latitude`, `pos_longitude`, `sonde_name`, `active`) VALUES (1, 49.386954 , 1.074300 , 'SI7021', FALSE );


#
# TABLE STRUCTURE FOR: mesure
#



CREATE TABLE mesure (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_sonde` int NOT NULL,
  `temperature` float NOT NULL, 
  `humidity` float NOT NULL, 
  `added_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO mesure (`id_sonde` , `temperature`, `humidity`, `added_at`) 
(1, 5, 80, '2021-02-06 00:00:00'),
(1, 7, 70, '2021-02-06 03:00:00'),
(1, 9, 75, '2021-02-06 06:00:00'),
(1, 10, 80, '2021-02-06 09:00:00'),
(1, 11, 70, '2021-02-06 12:00:00'),
(1, 11, 65, '2021-02-06 15:00:00'),
(1, 9, 65, '2021-02-06 18:00:00'),
(1, 9, 65, '2021-02-06 21:00:00'),
(1, 5, 65, '2021-02-07 00:00:00'),
(1, 6, 60, '2021-02-07 03:00:00'),
(1, 8, 55, '2021-02-07 06:00:00'),
(1, 10, 50, '2021-02-07 09:00:00'),
(1, 13, 70, '2021-02-07 12:00:00'),
(1, 11, 65, '2021-02-07 15:00:00'),
(1, 9, 65, '2021-02-07 18:00:00'),
(1, 4, 65, '2021-02-07 21:00:00'),
(1, 0, 65, '2021-02-08 00:00:00'),
(1, 6, 60, '2021-02-08 03:00:00'),
(1, 8, 55, '2021-02-08 06:00:00'),
(1, 10, 50, '2021-02-08 09:00:00'),
(1, 9, 70, '2021-02-08 12:00:00'),
(1, 8, 80, '2021-02-08 15:00:00'),
(1, 5, 80, '2021-02-08 18:00:00'),
(1, 4, 80, '2021-02-08 21:00:00'),
(1, -3, 75, '2021-02-09 00:00:00'),
(1, -4, 60, '2021-02-09 03:00:00'),
(1, -3, 55, '2021-02-09 06:00:00'),
(1, 0, 50, '2021-02-09 09:00:00'),
(1, 5, 55, '2021-02-09 12:00:00'),
(1, 6, 50, '2021-02-09 15:00:00'),
(1, 5, 50, '2021-02-09 18:00:00'),
(1, 4, 50, '2021-02-09 21:00:00'),
(1, 0, 50, '2021-02-10 00:00:00'),
(1, -4, 60, '2021-02-10 03:00:00'),
(1, -3, 55, '2021-02-10 06:00:00'),
(1, -5, 50, '2021-02-10 09:00:00'),
(1, -3, 55, '2021-02-10 12:00:00'),
(1, -1, 50, '2021-02-10 15:00:00'),
(1, -1, 50, '2021-02-10 18:00:00'),
(1, -2, 50, '2021-02-10 21:00:00'),
(1, -3, 50, '2021-02-11 00:00:00'),
(1, -4, 60, '2021-02-11 03:00:00'),
(1, -3, 55, '2021-02-11 06:00:00'),
(1, -1, 50, '2021-02-11 09:00:00'),
(1, 3, 55, '2021-02-11 12:00:00'),
(1, 2, 50, '2021-02-11 15:00:00'),
(1, 0, 50, '2021-02-11 18:00:00'),
(1, 0, 50, '2021-02-11 21:00:00'),
(1, 0, 50, '2021-02-12 00:00:00')
;


alter table mesure add constraint FK_realiser foreign key (id_sonde)
      references sonde (id) on delete restrict on update restrict;