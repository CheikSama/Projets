-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mer. 10 avr. 2019 à 00:41
-- Version du serveur :  10.1.37-MariaDB
-- Version de PHP :  7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `prosopographie`
--

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `creation_peinture`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `creation_peinture` (
`nom` varchar(20)
,`prenom` varchar(20)
,`Titre` varchar(128)
,`theme_aborde` varchar(30)
);

-- --------------------------------------------------------

--
-- Structure de la table `critique`
--

CREATE TABLE `critique` (
  `Id_critique` int(2) NOT NULL,
  `Prenom` varchar(20) DEFAULT NULL,
  `Nom` varchar(20) DEFAULT NULL,
  `Annee_de_naissance` int(4) DEFAULT NULL,
  `Annee_de_mort` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `critique`
--

INSERT INTO `critique` (`Id_critique`, `Prenom`, `Nom`, `Annee_de_naissance`, `Annee_de_mort`) VALUES
(1, 'Guillaume', 'Appolinaire', 1880, 1918),
(2, 'Henri', 'Focillon', 1881, 1983),
(3, 'Leonce', 'Benedite', 1859, 1925),
(4, 'Leon', 'Rosenthal', 1870, 1932),
(5, 'Maurice', 'Denis', 1870, 1943),
(6, 'Frantz', 'Jourdain', 1847, 1935),
(7, 'Elie', 'Faure', 1873, 1937),
(8, 'Josephin', 'Peladan', 1858, 1918),
(9, 'Felix', 'Feneon', 1861, 1944),
(10, 'Gustave', 'Soulier', 1872, 1937);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `domaine_litterature`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `domaine_litterature` (
`nom` varchar(20)
,`prenom` varchar(20)
,`Diplome` varchar(30)
);

-- --------------------------------------------------------

--
-- Structure de la table `editeur`
--

CREATE TABLE `editeur` (
  `Id_editeur` int(2) NOT NULL,
  `Nom_editeur` varchar(64) NOT NULL,
  `Ville` varchar(10) NOT NULL,
  `Opinion` varchar(20) DEFAULT NULL,
  `Id_critique` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `editeur`
--

INSERT INTO `editeur` (`Id_editeur`, `Nom_editeur`, `Ville`, `Opinion`, `Id_critique`) VALUES
(1, 'La revue blanche', 'Paris', 'Anarchisme', 1),
(2, 'L Intransigeant', 'Paris', 'Droite', 1),
(3, 'Chez Paul Guillaume', 'Paris', 'Communisme', 1),
(4, 'Le Petit Messager des Arts et des Artistes, et des Industries d ', 'Paris', 'Ouvrier', 1),
(5, 'Chez Paul Guillaume', 'Paris', 'Gauche', 1),
(6, 'La France libre', 'Paris', 'Gauche', 2),
(7, 'Le Démocrate', 'Montbeliar', 'Gauche', 2),
(8, 'La Revue de l art ancien et moderne', 'Paris', 'Non renseigné', 2),
(9, 'La Revue de l art ancien et moderne', 'Paris', 'Non renseigné', 3),
(10, 'Gazette des beaux-arts', 'Paris', 'Non renseigné', 3),
(11, 'La France libre', 'Paris', 'Gauche', 4),
(12, 'L Amour de l art', 'Paris', 'Non renseigné', 4),
(13, 'Le Rappel des travailleurs des villes et des campagnes', 'Paris', 'Gauche', 4),
(14, 'Mercure de France', 'Paris', 'Gauche', 5),
(15, 'L Occident', 'Paris', 'Non renseigné', 5),
(16, 'Beaux-Arts', 'Paris', 'Non renseigné', 5),
(17, 'L Amour de l art', 'Paris', 'Non renseigné', 5),
(18, 'L Architecte', 'Paris', 'Non renseigné', 6),
(19, 'L Art décoratif', 'Paris', 'Non renseigné', 6),
(20, 'L architecture au Champ de Mars', 'Paris', 'Non renseigné', 6),
(21, 'L Aurore', 'Paris', 'Gauche', 7),
(22, 'La Grande Revue', 'Paris', 'Non renseigné', 7),
(23, 'L Amour de l art', 'Paris', 'Non renseigné', 7),
(24, 'Mercure de France', 'Paris', 'Gauche', 8),
(25, 'Le soleil', 'Paris', 'Non renseigné', 8),
(26, 'l artiste', 'Paris', 'Non renseigné', 8),
(27, 'Bulletin de la vie artistique', 'Paris', 'Non renseigné', 9),
(28, 'L Art moderne', 'Paris', 'Non renseigné', 9),
(29, 'L Art décoratif', 'Paris', 'Non renseigné', 10);

-- --------------------------------------------------------

--
-- Structure de la table `formation`
--

CREATE TABLE `formation` (
  `Id_formation` int(2) NOT NULL,
  `Pays` varchar(20) NOT NULL,
  `Ville` varchar(10) NOT NULL,
  `Diplome` varchar(30) NOT NULL,
  `Domaine` varchar(20) DEFAULT NULL,
  `Nom_ecole` varchar(128) DEFAULT NULL,
  `Annee_obtention` int(4) DEFAULT NULL,
  `Id_critique` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `formation`
--

INSERT INTO `formation` (`Id_formation`, `Pays`, `Ville`, `Diplome`, `Domaine`, `Nom_ecole`, `Annee_obtention`, `Id_critique`) VALUES
(1, 'France', 'Paris', 'sténographie', 'Littérature', '', 1900, 1),
(2, 'France', 'Paris', 'Aggregation', 'Littérature', 'La Sorbonne', 1908, 2),
(3, 'Italie', 'Rome', 'Licence', 'Littérature', 'La Sorbonne', 1906, 2),
(4, 'France', 'Paris', 'Doctorat', 'Littérature', 'La Sorbonne', 1918, 2),
(5, 'France', 'Lyon', 'Licence', 'Droit', 'Universite de Lyon', 1882, 3),
(6, 'France', 'Paris', 'Aggregation', 'Histoire', 'Ecole normale superieure', 1892, 4),
(7, 'France', 'Paris', 'Baccalaureat', 'Histoire', ' lycée Condorce', 1889, 5),
(8, 'France', 'Paris', 'Aggregation', 'Art', 'Ecole normale superieure des beaux-Arts', 1868, 6),
(9, 'France', 'Paris', 'Doctorat', 'Medecine', 'Faculté de Paris', 1899, 7),
(10, 'France', 'Nimes', 'Baccalaureat', '', 'Lycee de Nimes', 0, 8),
(11, 'France', 'Macon', 'Concours de redacteur', 'Littérature', 'Ministère de la Guerre', 1881, 9),
(12, 'France', 'Paris', 'Aggregation', 'Art', 'Ecole normale supérieure des beaux arts', 1896, 10);

-- --------------------------------------------------------

--
-- Structure de la table `localisation`
--

CREATE TABLE `localisation` (
  `Id_localisation` int(3) NOT NULL,
  `Pays` varchar(20) NOT NULL,
  `Ville` varchar(10) NOT NULL,
  `Date_arrivee` int(4) NOT NULL,
  `Date_depart` int(4) DEFAULT NULL,
  `Id_critique` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `localisation`
--

INSERT INTO `localisation` (`Id_localisation`, `Pays`, `Ville`, `Date_arrivee`, `Date_depart`, `Id_critique`) VALUES
(1, 'France', 'Paris', 1900, 1914, 1),
(2, 'France', 'Nice', 1914, 1916, 1),
(3, 'France', 'Paris', 1917, 1918, 1),
(4, 'France', 'Lyon', 1913, 1924, 2),
(5, 'Italie', 'Rome', 1906, 1908, 2),
(6, 'France', 'Paris', 1924, 0, 2),
(7, 'France', 'Paris', 1882, 1906, 3),
(8, 'Etats-Unis', 'New-York', 1920, 1921, 3),
(9, 'Italie', 'Venise', 1906, 1919, 3),
(10, 'France', 'Paris', 1918, 1924, 4),
(11, 'France', 'Lyon', 1924, 1932, 4),
(12, 'France', 'Nancy', 1904, 1909, 4),
(13, 'France', 'Paris', 1875, 0, 5),
(14, 'France', 'Paris', 1847, 0, 6),
(15, 'France', 'Paris', 1888, 0, 7),
(16, 'France', 'Paris', 1874, 0, 8),
(17, 'France', 'Paris', 1881, 1944, 9),
(18, 'Italie', 'Florence', 1900, 1937, 10);

-- --------------------------------------------------------

--
-- Structure de la table `oeuvre`
--

CREATE TABLE `oeuvre` (
  `Id_oeuvre` int(2) NOT NULL,
  `Titre` varchar(128) NOT NULL,
  `Date` varchar(4) NOT NULL,
  `Theme_aborde` varchar(30) NOT NULL,
  `Type` varchar(10) NOT NULL,
  `Id_critique` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `oeuvre`
--

INSERT INTO `oeuvre` (`Id_oeuvre`, `Titre`, `Date`, `Theme_aborde`, `Type`, `Id_critique`) VALUES
(1, 'Gazette d art. Le Pergamon à Berlin', '1902', 'Sculpture', 'Article', 1),
(2, 'Le Vernissage des Artistes français. La recette, pour l aviation militaire, est bonne', '1912', 'Peinture', 'Article', 1),
(3, 'Exposition de Natalie de Gontcharowa et Michel Larionow', '1914', 'exposition', 'Preface', 1),
(4, 'L art vivant et la guerre', '1915', 'Guerre', 'Article', 1),
(5, 'À propos de l art des Noirs', '1917', 'Sculpture', 'Preface', 1),
(6, 'Socrate et la guerre', '1918', 'Guerre', 'Article', 2),
(7, 'Le Dernier romantique', '1907', 'Amour', 'Article', 2),
(8, 'Une Loi démocratique', '1907', 'Politique', 'Article', 2),
(9, 'Les Mosquées du Caire', '1933', 'Religion', 'Article', 2),
(10, 'Le Problème des Primitifs français et la peinture clunisienne', '1932', 'Peinture', 'Article', 2),
(11, 'Les Salons de 1899. La Sculpture', '1899', 'Sculpture', 'Article', 3),
(12, 'Après les Salons. Quelques réflexions sur la sculpture', '1920', 'Sculpture', 'Article', 3),
(13, 'Les Salons de 1906. La Sculpture', '1906', 'Sculpture', 'Article', 3),
(14, 'La vie artistique pendant la guerre', '1916', 'Guerre', 'Article', 3),
(15, 'Notes d art, La France libre, 28 novembre 1920, p. 2', '1920', 'Actualite artistique', 'Article', 4),
(16, 'Notes d art, La France libre, 19 juin 1921, p. 2', '1921', 'Actualite artistique', 'Article', 4),
(17, 'Les Livres d art, L Amour de l art, t. VIII, septembre 1927, p. 342.', '1927', 'actualite artistique', 'Article', 4),
(18, 'Elections municipales et socialisme', '1904', 'Politique', 'Article', 4),
(19, 'La question religieuse. Enquête internationale', '1907', 'Religion', 'Article', 5),
(20, 'Enquête sur les tendances actuelles des arts plastiques', '1905', 'Actualite artistique', 'Article', 5),
(21, 'Un chef d œuvre inconnu de la peinture française au XVe siècle', '1904', 'Peinture', 'Article', 5),
(22, 'État actuel de l art religieux', '1933', 'Religion', 'Article', 5),
(23, 'La saleté des tableaux du Louvre', '1930', 'Peinture', 'Article', 5),
(24, 'L art du décor, L Architecture, t. VII, n° 24, 16 juin 1894, p. 185-187.', '1894', 'Architecture', 'Article', 6),
(25, 'L orme de Scutari, L Architecture, t. XII, n° 28, 15 juillet 1899, p. 264-266.', '1899', 'Architecture', 'Article', 6),
(26, 'La villa Majorelle à Nancy', '1902', 'Architecture', 'Article', 6),
(27, 'L architecture au Champ de Mars, La Construction moderne, t. VII, 07 mai 1892, p. 361-362.', '1892', 'Architecture', 'Article', 6),
(28, 'Au Pays Basque', '1899', 'exposition', 'Article', 7),
(29, 'L âme islamique, La Grande revue, t. CXXXIX, septembre 1932.', '1932', 'Religion', 'Article', 7),
(30, 'L art moderne. L’Agonie de la peinture', '1931', 'Peinture', 'Article', 7),
(31, 'Art moderne. Agonie de la peinture. Conclusion d’une polémique', '1932', 'Peinture', 'Article', 7),
(32, 'La question religieuse. Enquête internationale', '1907', 'Religion', 'Article', 8),
(33, 'De l inutilité de la réforme protestante', '1908', 'Religion', 'Article', 8),
(34, 'Le politicien', '1908', 'Politique', 'Article', 8),
(35, 'L Esthétique à l Exposition Nationale des Beaux-arts', '1883', 'exposition', 'Article', 8),
(36, 'Les poèmes de Laforgue', '1887', 'Peinture', 'Article', 9),
(37, 'Des peintres et leur modèle', '1921', 'Peinture', 'Article', 9),
(38, 'L Exposition des Artistes indépendants', '1889', 'exposition', 'Article', 9),
(39, 'L Exposition de Turin.', '1902', 'exposition', 'Article', 10);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `opinion_gauche`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `opinion_gauche` (
`nom` varchar(20)
,`prenom` varchar(20)
,`Opinion` varchar(20)
);

-- --------------------------------------------------------

--
-- Structure de la table `profession`
--

CREATE TABLE `profession` (
  `Id_profession` int(2) NOT NULL,
  `Metier_exerce` varchar(64) NOT NULL,
  `Date_debut` int(4) NOT NULL,
  `Date_fin` int(4) NOT NULL,
  `Classe_sociale` varchar(30) NOT NULL,
  `Id_critique` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `profession`
--

INSERT INTO `profession` (`Id_profession`, `Metier_exerce`, `Date_debut`, `Date_fin`, `Classe_sociale`, `Id_critique`) VALUES
(1, 'Employé de banque', 1902, 1907, 'Classe moyenne', 1),
(2, 'Journaliste', 1908, 1914, 'Classe moyenne', 1),
(3, 'Brigadier', 1914, 1916, 'Classe moyenne', 1),
(4, 'Ecrivain', 1917, 1918, 'Classe moyenne', 1),
(5, 'Enseignant', 1908, 1938, 'Bourgoisie', 2),
(6, 'Conservateur de musee', 1913, 1924, 'Bourgoisie', 2),
(7, 'Boursier', 1906, 1908, 'Bourgoisie', 2),
(8, 'Enseignant', 1908, 1938, 'Bourgoisie', 2),
(9, 'Conservateur de musee', 1892, 1906, 'Bourgoisie', 3),
(10, 'président du jury international de la Biennale', 1906, 1919, 'Bourgoisie', 3),
(11, 'Enseignant', 1900, 1932, 'Bourgoisie', 4),
(12, 'Historien de l art', 1909, 1932, 'Bourgoisie', 4),
(13, 'Peintre', 1890, 1943, 'Classe moyenne', 5),
(14, 'Architecte', 1868, 1935, 'Bourgoisie', 6),
(15, 'Medecin', 1896, 1937, 'Bourgoisie', 7),
(16, 'Historien de l art', 1905, 1937, 'Bourgoisie', 7),
(17, 'Ecrivain', 1884, 1918, 'Bourgoisie', 8),
(18, 'Employé de banque', 1884, 1918, 'Bourgoisie', 8),
(19, 'Ecrivain', 1881, 1944, 'Bourgoisie', 9),
(20, 'Journaliste', 1902, 1944, 'Bourgoisie', 9),
(21, 'Enseignant', 1897, 1937, 'Bourgoisie', 10);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `sejour_etranger`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `sejour_etranger` (
`nom` varchar(20)
,`prenom` varchar(20)
,`pays` varchar(20)
);

-- --------------------------------------------------------

--
-- Structure de la vue `creation_peinture`
--
DROP TABLE IF EXISTS `creation_peinture`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `creation_peinture`  AS  select `critique`.`Nom` AS `nom`,`critique`.`Prenom` AS `prenom`,`oeuvre`.`Titre` AS `Titre`,`oeuvre`.`Theme_aborde` AS `theme_aborde` from (`critique` join `oeuvre` on((`critique`.`Id_critique` = `oeuvre`.`Id_critique`))) where (`oeuvre`.`Theme_aborde` = 'Peinture') ;

-- --------------------------------------------------------

--
-- Structure de la vue `domaine_litterature`
--
DROP TABLE IF EXISTS `domaine_litterature`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `domaine_litterature`  AS  select `critique`.`Nom` AS `nom`,`critique`.`Prenom` AS `prenom`,`formation`.`Diplome` AS `Diplome` from (`critique` join `formation` on((`critique`.`Id_critique` = `formation`.`Id_critique`))) where (`formation`.`Domaine` = 'Littérature') ;

-- --------------------------------------------------------

--
-- Structure de la vue `opinion_gauche`
--
DROP TABLE IF EXISTS `opinion_gauche`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `opinion_gauche`  AS  select `critique`.`Nom` AS `nom`,`critique`.`Prenom` AS `prenom`,`editeur`.`Opinion` AS `Opinion` from (`critique` join `editeur` on((`critique`.`Id_critique` = `editeur`.`Id_critique`))) where (`editeur`.`Opinion` = 'Gauche') ;

-- --------------------------------------------------------

--
-- Structure de la vue `sejour_etranger`
--
DROP TABLE IF EXISTS `sejour_etranger`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `sejour_etranger`  AS  select `critique`.`Nom` AS `nom`,`critique`.`Prenom` AS `prenom`,`localisation`.`Pays` AS `pays` from (`critique` join `localisation` on((`critique`.`Id_critique` = `localisation`.`Id_critique`))) where (`localisation`.`Pays` <> 'France') ;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `critique`
--
ALTER TABLE `critique`
  ADD PRIMARY KEY (`Id_critique`);

--
-- Index pour la table `editeur`
--
ALTER TABLE `editeur`
  ADD PRIMARY KEY (`Id_editeur`),
  ADD KEY `Fk_Critique_Id_critique_Editeur` (`Id_critique`);

--
-- Index pour la table `formation`
--
ALTER TABLE `formation`
  ADD PRIMARY KEY (`Id_formation`),
  ADD KEY `fk_Critique_Id_critique_Formation` (`Id_critique`);

--
-- Index pour la table `localisation`
--
ALTER TABLE `localisation`
  ADD PRIMARY KEY (`Id_localisation`),
  ADD KEY `fk_Critique_Id_critique` (`Id_critique`);

--
-- Index pour la table `oeuvre`
--
ALTER TABLE `oeuvre`
  ADD PRIMARY KEY (`Id_oeuvre`),
  ADD KEY `fk_Critique_Id_critique_Oeuvre` (`Id_critique`);

--
-- Index pour la table `profession`
--
ALTER TABLE `profession`
  ADD PRIMARY KEY (`Id_profession`),
  ADD KEY `Fk_Critique_Id_critique_Profession` (`Id_critique`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `critique`
--
ALTER TABLE `critique`
  MODIFY `Id_critique` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `editeur`
--
ALTER TABLE `editeur`
  MODIFY `Id_editeur` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT pour la table `formation`
--
ALTER TABLE `formation`
  MODIFY `Id_formation` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `localisation`
--
ALTER TABLE `localisation`
  MODIFY `Id_localisation` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT pour la table `oeuvre`
--
ALTER TABLE `oeuvre`
  MODIFY `Id_oeuvre` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT pour la table `profession`
--
ALTER TABLE `profession`
  MODIFY `Id_profession` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `editeur`
--
ALTER TABLE `editeur`
  ADD CONSTRAINT `Fk_Critique_Id_critique_Editeur` FOREIGN KEY (`Id_critique`) REFERENCES `critique` (`Id_critique`);

--
-- Contraintes pour la table `formation`
--
ALTER TABLE `formation`
  ADD CONSTRAINT `fk_Critique_Id_critique_Formation` FOREIGN KEY (`Id_critique`) REFERENCES `critique` (`Id_critique`);

--
-- Contraintes pour la table `localisation`
--
ALTER TABLE `localisation`
  ADD CONSTRAINT `fk_Critique_Id_critique` FOREIGN KEY (`Id_critique`) REFERENCES `critique` (`Id_critique`);

--
-- Contraintes pour la table `oeuvre`
--
ALTER TABLE `oeuvre`
  ADD CONSTRAINT `fk_Critique_Id_critique_Oeuvre` FOREIGN KEY (`Id_critique`) REFERENCES `critique` (`Id_critique`);

--
-- Contraintes pour la table `profession`
--
ALTER TABLE `profession`
  ADD CONSTRAINT `Fk_Critique_Id_critique_Profession` FOREIGN KEY (`Id_critique`) REFERENCES `critique` (`Id_critique`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
