Armadito gui
============

.. danger:: L'interface utilisateur graphique est en cours de refonte et la nouvelle version n'est pas encore portée à Windows. Ce sera réglé dès que possible.


Installation de prérequis
-------------------------

Les conditions préalables sont les suivantes:

* node.js
* Git (nécessaire par bower)
* bower

Installation d'un noeud et d'une façade
---------------------------------------

Tout d'abord, téléchargez node.js depuis https://nodejs.org/en/download/, en utilisant l'installateur .msi ou le programme d'installation .exe, à votre choix.

Pendant l'installation, les choix de configuration par défaut sont OK.

Une fois le nœud installé, lancez une ligne de commande.

Vérification de l'installation:

::

	npm --version
	2.15.1

Puis installez bower en utilisant:

::

	npm install -g bower

Installer git
-------------

Pour utiliser bower, vous devez d'abord installer git.

Git pour windows est disponible ici: https://git-for-windows.github.io/

Vérification de l'installation:

::

	git version 2.8.1.windows.1


Installation des modules dans l'arborescence des sources
--------------------------------------------------------


Exécutez le bower à partir du répertoire ** armadito-av / gui ** pour installer les modules nécessaires:

::

         cd SOMEWHERE/armadito-av/gui
	 bower install
	 npm install

Cela devrait générer beaucoup de messages


Installation de Webkit de noeud
-------------------------------

Téléchargez l'archive à partir de: http://nwjs.io/downloads/

Assurez-vous de télécharger le SDK.

Extrayez l'archive à l'aide de l'explorateur de fichiers Windows.


Exécution de l'interface
------------------------
Tout d'abord, le service Armadillo doit être lancé.
L'interface utilisateur peut être lancée avec:

::

	cd SOMEWHERE\ng-armadito
	SOMEWHEREELSE\nwjs-sdk-v0.14.0-win-x64\nw.exe .

Débogage de l'interface
-----------------------

Une fois l'interface lancée:

- cliquez avec le bouton droit de la souris dans la fenêtre pour afficher le menu de débogage et sélectionnez «Inspecter» ou appuyez sur F12
- dans la fenêtre de l'inspecteur, sélectionnez l'onglet "console"

Construire avec grunt
---------------------

Installer grunt:

::

         npm install -g grunt-cli

Exécuter `grunt` pour la construction et` grunt servir `pour l'aperçu.

Vous pouvez utiliser "--force" si vous voulez construire avec des avertissements.

.. note:: Ce projet est généré avec [yo génération angulaire] version 0.15.1.

