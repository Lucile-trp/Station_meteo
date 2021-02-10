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

INSERT INTO users (`id`, `name`, `firstname`, `email`, `token`) VALUES (1, 'Lucile', 'TRIPIER', 'tripier.lucile@gmail.com', 'blabla67');

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

INSERT INTO sonde (`id`, `pos_latitude`, `pos_longitude`, `sonde_name`, `active`) VALUES (1, 20.30 , 30.20 , 'test value', FALSE );


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

INSERT INTO mesure (`id`, `id_sonde` , `temperature`, `humidity`, `added_at`) VALUES (1, 1, 23, 60, '2007-11-03 15:11:39');



alter table mesure add constraint FK_realiser foreign key (id_sonde)
      references sonde (id) on delete restrict on update restrict;