__author__ = 'Rashed'

TABLES = {}
TABLES['movies'] = (
    "CREATE TABLE `movies` ("
    "  `id` int(50) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(50) NOT NULL,"
    "  `geners` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['links'] = (
    "CREATE TABLE `links` ("
    "  `id` int(50) NOT NULL,"
    "  `imdbid` int(50) NOT NULL,"
    "  `tmdbid` int(50) NOT NULL,"
    "  `movie_id` int(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
