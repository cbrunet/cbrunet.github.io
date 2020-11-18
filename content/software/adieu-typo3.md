title: Adieu Typo3, bienvenue Pélican!
tags: pelican
slug: adieu-typo2-bienvenur-pelican
lang: fr
status: draft
summary: Pourquoi j'abandonne Typo3 et pourquoi je choisis Pélican

Je dois admettre que Typo3 est un CMS qui m'a servi durant plusieurs
années. Mais aujourd'hui, il est temps de lui dire au revoir.
Voici pourquoi...


## Pourquoi j'aime Typo3?

Quand j'ai cherché quel CMS adopter à l'époque, j'en ai essayé
plusieurs avant de m'arrêter à Typo3. Même que les premières fois
que j'ai essayé Typo3, je l'ai trouvé bien trop compliqué, et j'ai
bien failli ne jamais l'adopter. Alors, qu'est-ce qui a finalement
déterminé ce choix?

Tout d'abord, parce qu'il est très customizable.
Il n'impose pas de structure ou de modèle prédéterminé pour le site.
Je peux déterminer la structure de menus que je veux,
plusieurs menus différents si je le désire. Je peux coder le
template comme je le veux. Je peux organiser les éléments d'une
page comme je le veux. Je peux avoir des présentations différentes
selon les pages. Je peux structurer le site comme je le veux.

Ensuite, peu de CMS gèrent les sites multi-lingues aussi bien que Typo3.
Je peux traduire une page complète, ou des sections d'une page. Je peux
avoir des pages différentes selon la langue. Et dans tous les cas, j'ai
une interface pour aider à traduire les pages.

Typo3 dispose d'un nombre impressionnant de modules disponible,
pour ajouter des fonctionnalités ou des types de contenu spécialisés.
Il est aussi relativement simple de créer des modules d'extension
pour ajouter de nouvelles fonctionalités au logiciel. 

Enfin, Typo3 est un logiciel sérieux, avec des programmeurs dédiés,
une équipe de sécurité, des mises à jour fréquentes. Il est stable
et sécuritaire.


## Pourquoi je n'aime pas Typo3

Malgré ses qualité, ce logiciel a néanmoins plusieurs défauts.
Plusieurs de ces points ce sont améliorés avec les années

Tout d'abord, son poids et sa complexité. Même si le rendu des pages
demeure rapide, grâce à un système de cache, le backend est toujours
demeuré un peu lourd. De plus, le logiciel demande une configuration
relativement complexe, et fonctionne beaucoup mieux sur un serveur
dédié que sur un hébergement partagé.

Tout est configurable dans Typo3, mais toute configuration demande
un certain travail. Je peux régler les droits d'accès par page, par
bloc, par groupe... Mais quand un accès ne fonctionne pas, je dois
regarder à plusieurs endroits avant de trouver où est-ce que ça
ne passe pas... Je peux créer des layouts différents, pour l'affichage
des pages autant que pour l'entrée des données dans le backend. Mais
il faut prendre le temps de le configurer. Pour que cela soit simple
pour un éditeur, je dois mettre beaucoup de temps à configurer le 
logiciel..

Les mises à jour du logiciel sont souvent complexes.
Le problème, ce sont les modules. Parfois, ils ne sont pas mis à jour
à temps, et on doit donc attendre que le module soit prêt pour
pourvoir mette à jour Typo3. Parfois un module sur lequel on misait
est abandonné, et on doit trouvé une alternative. Souvent, le site
brise lors d'une mise à jour. Il faut donc bien plafinier les mises 
à jour, tester sur une copie du site, réparer les configurations
et modules qui ne fonctionnent plus. Cela est complexe, et prend
du temps...

Ensuite, Typo3 est écrit en PHP. J'ai déjà été très habile avec ce
langage dans le passé, mais aujoud'hui, lui et moi avons évolué
différemment. Disons que je préfère maintenant les serpents
aux éléphants. Alors quand vient le temps de développer un module,
ou de corriger un bug, je suis plutôt perdu, et je dois lire
beaucoup de documentation et d'exemple, et faire beaucoup
d'essaies et d'erreurs...

Enfin, je réalise que peu de gens connaissent Typo3, du moins
dans ma région. Alors quand je dois laisse la gestion d'un site
à quelqu'un d'autre, je n'ai pas de ressource à proposer,
je n'ai personne pour prendre la relève. La meilleure solution
devient alors de créer un nouveau site.



## Quels sont mes besoins aujourd'hui?

Maintenant que je n'ai plus de temps pour gérer les sites des autres
(je n'ai pas plus le temps pour gérer mon propre site, mais
ça, ça a toujours été le cas...), je n'ai plus besoin de bels
interfaces pour entrer les contenus. Je n'ai plus besoin
d'un gros serveur pour héberger des dizaines de sites.
J'ai juste besoin que ça fonctionne, que ça ne coûte pas cher,
et que ça puisse durer dans le temps...


### De dynamique à statique

Alors pourquoi aurais-je besoin d'un CMS?
Je suis le seul qui aurai à entrer du contenu.
Mon contenu reste identique peu importe le visiteur.
Mon site peu bien être statique! 

Statique, mais généré. Je ne veux pas réécrire le menu
sur chaque page, chaque fois que j'ajoute une section.
Je ne veux pas réécrire l'index chaque fois que j'ajoute
une page. Ça, c'est le rôle d'un générateur de site.

Et le gros avantage? C'est que je peux héberger le site gratuitement.
Sur GitHub pages notamment, mais il existe bien d'autres possibilités.


### De PHP à Python

Des CMS en Python, il en existe peu. Du moins, j'en ai jamais trouvé
un qui équivalle à Typo3. Par contre, un générateur de site en Python,
ça existe! Je serai donc bien plus à l'aise, si j'ai besoin de corriger
un bug, de suggérer une amélioration, ou d'écrire un module
pour une fonction particulière.


### Un workflow automatisé

J'écris, je pousse, ça publie. Qu'est-ce qui pourait être plus simple?
De plus, j'ai un historique complet des changements.
Je veux changer la présentation? Je n'ai qu'à changer le template,
et voici la métamorphose! Je veux changer de logiciel générateur?
Les sources ne sont que des fichiers texte. Ce sera facile à
transformer au besoin, à l'aide de quelques scripts.


