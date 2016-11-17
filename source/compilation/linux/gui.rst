Armadito gui
============

Armadito gui s'appuie sur les technologies Web récentes pour fournir une interface graphique multiplateforme pour l'antivirus Armadito.

Les sources sont accessibles au public sur github.com, vous pouvez l'obtenir avec la commande suivante:

::

   $ git clone https://github.com/armadito/armadito-gui.git -b DEV

Prérequis
-------------

Pour exécuter l'interface utilisateur graphique Armadito, vous avez besoin de:

- bower
- node.js


Installation d'un noeud et d'une façade
---------------------------------------


Les installations sont effectuées en tant que root.

Installation node.js:

::

	apt-get install nodejs-legacy

Vérification de l'installation:

::

	npm --version
	1.4.21

Installation du bower (doit être effectué en tant que root aussi):

::

	npm install -g bower


Installation de modules dans sourcetree
---------------------------------

Après le clonage du référentiel, l'arborescence des sources de l'interface utilisateur doit être configurée:

::

	cd /home/joebar/armadito-av/gui
	bower install
	npm install

Configuration
-------------

Une fois git repo cloné, vous devez initialiser la construction en utilisant automake, autoconf et des outils.
Un script shell ** autogen.sh ** est fourni pour faciliter cette étape:

::

    $ ./autogen.sh 
    + aclocal --force
    + automake --foreign --add-missing --force-missing --copy
    + autoconf --force

Cela générera les fichiers ** Makefile.in ** et le script ** configure **.

** configure ** script prend les options utiles suivantes:

    --prefix=PREFIX         install architecture-independent files in PREFIX [default is /usr/local]
    
Le répertoire ** PREFIX ** sera utilisé par ** make install **. Son utilisation est obligatoire, à moins de construire un paquet et d'installer dans les répertoires système, puisque les modules de balayage et l'interface utilisateur graphique aura besoin d'un libarmadito correctement installé.

L'appel typique du script de configuration est:

::

    $ /home/joebar/armadito-av/gui/configure --prefix=/home/joebar/install

Le construction
--------

Une fois configuré, la construction est facile:

::

    $ make


Installation
----------


Après la construction, l'installation se fait par:

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires du ** PREFIX **
Répertoire défini au moment de la configuration.

Exécution de l'interface
---------------------

Tout d'abord, le démon Armadillo doit être lancé. Reportez-vous à la documentation d'Armadillo pour obtenir des instructions.
Ouvrez votre navigateur Web préféré et accédez à l'URL suivante: http://localhost:8888/app/index.html

Débogage de l'interface
-----------------------

Une fois l'interface lancée:

- cliquez avec le bouton droit de la souris dans la fenêtre pour afficher le menu de débogage et sélectionnez «Inspecter» ou appuyez sur F12
- dans la fenêtre de l'inspecteur, sélectionnez l'onglet "console"

Construire avec grunt
----------------

Installer grunt :

:: 

         npm install -g grunt-cli

Exécuter `grunt` pour la construction et` grunt servir `pour l'aperçu.

Vous pouvez utiliser "--force" si vous voulez construire avec des avertissements.

.. note:: Ce projet est généré avec [yo angular generator] version 0.15.1.

