CREATE DATABASE IF NOT EXISTS TP_STATION_METEO;

CREATE TABLE IF NOT EXISTS `values` (
 `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 `temperature` tinyint COLLATE utf8_unicode_ci NOT NULL, 
 `humidity` tinyint COLLATE utf8_unicode_ci NOT NULL, 
 `added_at` timestamp NOT NULL DEFAULT current_timestamp()
)CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE IF NOT EXISTS `users` (
 `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 `name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
 `firstname` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
 `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
 `token` varchar(40) NOT NULL,
 UNIQUE KEY `email` (`email`),
 UNIQUE KEY `api_key` (`api_key`)
) CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `users` (`id`, `name`, `firstname`, `email`, `token`) VALUES (1, 'Lucile', 'TRIPIER', 'tripier.lucile@gmail.com', 'blabla67');