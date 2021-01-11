#
# TABLE STRUCTURE FOR: authors
#

DROP TABLE IF EXISTS `authors`;

CREATE TABLE `authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `birthdate` date NOT NULL,
  `added` timestamp NOT NULL DEFAULT current_timestamp(),
  `api_key` varchar(63) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `api_key` (`api_key`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `authors` (`id`, `first_name`, `last_name`, `email`, `birthdate`, `added`, `api_key`) VALUES (1, 'Kenneth', 'Howe', 'kasandra.schmeler@example.com', '1996-03-13', '2007-11-03 15:11:39', 'sogY5KACCsaCemwOnadLmcIu9RONN4mgFdGCQujWDkZ');
INSERT INTO `authors` (`id`, `first_name`, `last_name`, `email`, `birthdate`, `added`, `api_key`) VALUES (2, 'Lucas', 'Cartwright', 'buckridge.alexandre@example.net', '1977-07-06', '2019-11-09 12:55:56', 'q49mVyvZbdbURY9vz5G-7t6_nDOtA7SQBtcg0PQvSOz');
INSERT INTO `authors` (`id`, `first_name`, `last_name`, `email`, `birthdate`, `added`, `api_key`) VALUES (3, 'Julien', 'TOUTAIN', 'toutainj@gmail.com', '1989-02-25', '2020-01-09 12:55:56', 'q49mVyvZbdbURY9vz5G-7t6_nDOtA7SQBtcgQujWDkZ');

#
# TABLE STRUCTURE FOR: posts
#

DROP TABLE IF EXISTS `posts`;

CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `title` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `content` text COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (1, 1, 'Hic tenetur in est beatae tempora consequatur beatae.', 'Qui ut nam et numquam. Eveniet ipsam dolorem aut. Ipsam harum adipisci aliquid ea tempore harum repellendus. Autem magnam quos ducimus.', 'Rerum est ipsa temporibus id. Ea tenetur voluptatem incidunt laborum. Asperiores ut optio culpa temporibus.', '2015-07-10');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (2, 2, 'Quibusdam odio sit et error dolorem delectus est.', 'Provident quod repellat excepturi sit autem neque. Eum mollitia non sequi temporibus sed.', 'Ut id ad harum est non placeat. Ab omnis nobis nostrum qui quae velit dolor. Modi velit qui esse. Sint cumque impedit quo totam illum minus.', '1999-12-10');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (3, 3, 'Quae sit rerum necessitatibus unde tempore.', 'Dolorum aspernatur illo fuga nesciunt sapiente. Sunt mollitia facere fugit hic tempore cupiditate. Consequatur rem eos qui ratione.', 'Asperiores commodi assumenda est perferendis. Accusamus voluptates delectus rerum enim. Nisi minima quisquam cupiditate quam. Vel suscipit qui quas architecto eum eos.', '1998-03-06');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (4, 1, 'In doloribus ut explicabo voluptatem.', 'Aut id dicta consequuntur. Eum nisi quod voluptas. Omnis dolorem aut dolores quo nam.', 'Officiis maiores expedita nihil. Corrupti maxime sit tenetur sit laborum totam recusandae voluptatem. Totam sit quidem distinctio et laborum et molestias.', '1980-02-06');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (5, 2, 'Fuga sit ut quae et sunt natus mollitia.', 'Harum ex quos dolore ullam dolor est. Sunt ullam perspiciatis amet est iusto quos. Illo voluptate commodi voluptas. Facere laboriosam non similique et in quos ut.', 'Dolorum aperiam consequatur nihil quos repellendus quo. Iusto et est id aspernatur rerum expedita est. Unde qui eos expedita neque voluptatibus ut.', '1976-01-15');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (6, 3, 'Ut modi doloribus aut aperiam pariatur qui ducimus.', 'Quia et culpa qui qui. Corrupti qui dicta inventore assumenda accusantium. Tempora sit qui explicabo.', 'Totam aliquid et voluptas minus doloremque consequatur qui. Vel pariatur et aut sed qui. Doloribus dolores quas libero aut voluptatem. Voluptates est non ex qui.', '1977-05-22');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (7, 1, 'Voluptas est totam ut eveniet eos.', 'Occaecati adipisci dolores animi quibusdam. Esse at temporibus quas aspernatur. Non debitis quo repellendus molestias velit dolorem aut deserunt.', 'Facilis optio repellat voluptatem sit. Maxime id cupiditate qui dolorem consequatur et similique velit. Ut soluta eligendi unde quia.', '1973-01-28');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (8, 2, 'Dignissimos magnam voluptatem adipisci repellendus qui vero.', 'Reiciendis eum libero ipsa necessitatibus voluptates reiciendis sequi. Provident natus sequi ut expedita. Est et assumenda aut dolore exercitationem porro.', 'Maxime et dolor enim laudantium eaque repellat. Necessitatibus et doloremque fuga iusto animi. Ullam error cumque harum.', '1998-06-12');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (9, 3, 'Ut facilis molestiae libero officia velit nisi.', 'Corporis atque iure et accusantium est odit. Nisi porro officia aut est quidem cupiditate sint. Velit sunt consectetur qui itaque eveniet ipsum. Sed excepturi reiciendis officia tempora magnam nesciunt saepe sequi.', 'Sint totam vel suscipit id consequuntur dignissimos aut. Itaque eos maiores quae et rem. Itaque ea quis at.', '1985-10-23');
INSERT INTO `posts` (`id`, `author_id`, `title`, `description`, `content`, `date`) VALUES (10, 1, 'Esse natus id ut qui.', 'Et ratione aperiam sit non et voluptatibus. Quasi itaque et quo quia at. Quia cum recusandae odit fugiat recusandae est minima.', 'Aliquid repudiandae porro sint est harum. Neque cum accusantium officia nemo corrupti. Distinctio ex ea reiciendis et quia et.', '1971-01-27');


