# Notebooks finaux du stage de Master 1 portant sur les couvertures de neige dans les Alpes (et au Pamir) 

Ce travail est le regroupement de l'ensemble de mes fiigures utilent pour mon stage de M1 STPE SCAHC a l'UGA (sous Gricad).

L'ensemble des données utilisées sont disponibles soit sur /bettik/PROJECTS/pr-regional-climate/mougina/ 

ou sur /home/mougina/mes_analyses_neige/

et pour les modèles : /bettik/castelli/data/MAR-ERA5/MAR3.14/EUo/daily/  et /bettik/castelli/data/MAR-ERA5/MAR3.14/EUo/ (Alpes)

/bettik/PROJECTS/pr-regional-climate/santolam/MARout_post/GRp/spin2/work/daily/ et /home/santolam/ (Pamir)

Tout cela depuis le cluster Dahu ou, pour ce qui est sur bettik, aussi Kraken (kcpu) (GRICAD).


Dans ces notebooks, j'utilise les données SNOW-CCI V4 gap-filled par l'ESA, ainsi que les données V2 et V4 sans gap-filling et, enfin, les données V2 gap-filled par Mickaël Lalande.
De plus, l'objectif étant de réaliser une comparaison pour les Alpes comme pour le Pamir, j'utilise MAR forcé par la réanalyse ERA5 car le stage s'est fait avec seulement 5 ans de données V4 gap-filled (référence) ; ces simulations m'ont été données 
par Maria Santolaria (Pamir) et Ian Castellanos (Alpes). 

Le notebook "Figure M1 avant correction" utilise toutes ces données afin de plot mes premières figures n'ayant pas de correction sur MAR.

Ensuite, les notebooks "Corrections" suivent une structure similaire, n'utilisant que les données V4 gap-filled et MAR ERA5 dans le but de corriger ce dernier modèle de plusieurs manières. Attention, ces notebooks sont organisés en deux parties 
dépendant toutes deux de la première ouverture des fichiers, mais il n'est pas possible de faire tourner les deux à la suite car pour la vérification de la correction (cross-validation) il nous faut 2016-2019, alors que pour l'application, il faut 2016-2021 ;
donc il faut changer au besoin. Sinon, ces trois notebooks... 

Enfin, le notebook "Figure analyse Pamir" a pour but de faire la même chose que les notebooks précédents mais sans cross-validation, donc pas de problème comme pour les corrections alpines ; il suit les mêmes étapes, mais avec beaucoup moins de présentation et une seule correction simple.
