#! /usr/bin/env python3
# coding: utf-8


# Projet5

## La startup Pur Beurre et l'utilisation de la base de données 
##  "Open Food Facts"
  Dans le cadre du parcours développeur Python sur OpenClassrooms,
  il nous est demandé de créer un programme qui interagirait avec
  la base Open Food Facts pour en récupérer les aliments, les comparer
  et proposer à l'utilisateur un substitut plus sain à l'aliment
  qui lui fait envie.

## Base de données utilisée:
### _ phpMyAdmin
### http://localhost/phpmyadmin/index.php?route=/database/structure&server=1&db=projet5

## Langage de programmation utilisé:
### _ Python 3.8
### https://www.python.org/downloads/

##Tableau Trello:
### https://trello.com/b/gk49js1Q

## Lien du repository sur Github pour le téléchargement:
### https://github.com/gwen23/Projet5

## Packages nécéssaires:
### 
    - requests 
    - mysql-connector-python  


## Description du programme:
### Les différentes classes :
#### _ Connection (contient les paramètres de connection à la base de données )
#### _ Menu ( contient le menu principal )
#### _ Program ( contient les sous menus 
    _ Choisir une catégorie, voir les choix enregistrés ou quitter. 
    _ Choix d'un produit.
    _ Proposition des substituts et de l'enregistrement du choix ou non. 
#### _ DbCreate (création et remplissage de la database)
#### _ Datacollect ( collecte les données des catégories et produits proposés)
#### _ Category ( pour l'identifiant, le nom et l'URL pour chaque catégorie )
#### _ Product ( pour toutes les caractéristiques des produits ))

## Lancement du programme:
### Depuis le fichier config selctionner puis exécuter:
#### " DbCreation.py " ( Création de la base de données ).
#### " APIreq.py " ( Collecte des données via l'API ).
#### " program.py " ( Exécution du programme ).


## Utilisation du programme:
### Différents menus.
#### _ Menu principal.
#### _ Choix parmi 5 catégories.
#### _ Choix du produit.
### Choix d'un subsitut.
#### _ Enregistrment ou non du substitut.
#### _ Consulter les choix enregistrés.








