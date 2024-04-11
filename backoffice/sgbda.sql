
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



-- Base de données : `sgbda`

-- Structure de la table `compte_rendu`
--

DROP TABLE IF EXISTS `compte_rendu`;
CREATE TABLE IF NOT EXISTS `compte_rendu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rapport` text,
  `date_creation` date DEFAULT NULL,
  `auteur` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `compte_rendu`
--

INSERT INTO `compte_rendu` (`id`, `rapport`, `date_creation`, `auteur`) VALUES
(1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', '2024-01-22', 'RP');

-- --------------------------------------------------------

--
-- Structure de la table `events`
--

DROP TABLE IF EXISTS `events`;
CREATE TABLE IF NOT EXISTS `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `pv`
--

DROP TABLE IF EXISTS `pv`;
CREATE TABLE IF NOT EXISTS `pv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `personne` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `contenu` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `pv`
--

INSERT INTO `pv` (`id`, `personne`, `date`, `contenu`) VALUES
(1, 'RP', '2024-01-22', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.');

-- --------------------------------------------------------

--
-- Structure de la table `rapports`
--

DROP TABLE IF EXISTS `rapports`;
CREATE TABLE IF NOT EXISTS `rapports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `personne` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `rapport` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `rapports`
--

INSERT INTO `rapports` (`id`, `personne`, `date`, `rapport`) VALUES
(1, 'chef de departement', '2012-03-23', 'jejfewnovnoiewnvonenvewnfoiwn');

-- --------------------------------------------------------

--
-- Structure de la table `table_name`
--

DROP TABLE IF EXISTS `table_name`;
CREATE TABLE IF NOT EXISTS `table_name` (
  `id` int NOT NULL AUTO_INCREMENT,
  `column_name1` varchar(255) DEFAULT NULL,
  `column_name2` varchar(255) DEFAULT NULL,
  `column_name3` varchar(255) DEFAULT NULL,
  `column_name4` varchar(255) DEFAULT NULL,
  `event_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `table_name`
--

INSERT INTO `table_name` (`id`, `column_name1`, `column_name2`, `column_name3`, `column_name4`, `event_date`) VALUES
(1, '', '', '', '', '2024-04-10');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `name`, `password`, `email`, `role`) VALUES
(1, 'Admin', 'pass', 'admin@email.com', 'admin'),
(4, 'abi', 'passer', 'abi@emai.com', 'user'),
(7, 'adja fall', 'pass', 'rc@email.com', 'RC(responsable de classe)'),
(14, 'fallou', 'passer', 'fallou@emai.com', 'RP'),
(16, 'gerrard', 'passer', 'gerard@emai.com', 'chef de departement');



COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
