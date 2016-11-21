Armadito WebUI
==============

Armadito WebUI s'appuie sur les technologies Web récentes pour fournir une interface graphique multiplateforme pour l'antivirus Armadito.
Les sources sont accessibles au public sur github.com, vous pouvez les obtenir avec la commande suivante:

::

   $ git clone https://github.com/armadito/armadito-web-ui.git -b DEV

Prérequis
---------

Pour exécuter l'interface utilisateur graphique Armadito, vous avez besoin de:

- bower

Installation de bower (doit être effectué en tant que root aussi):

::

	npm install -g bower


Installation des dépendances
----------------------------

::

	cd /home/joebar/armadito-web-ui
	bower install

Configuration
-------------

Une fois le repo cloné, vous devez initialiser la compilation en utilisant automake et autoconf.
Un script shell **autogen.sh** est fourni pour faciliter cette étape:

::

    $ ./autogen.sh
    + aclocal --force
    + automake --foreign --add-missing --force-missing --copy
    + autoconf --force

Cela générera les fichiers **Makefile.in** et le script **configure**.

** configure ** script prend les options utiles suivantes:

    --prefix=PREFIX         install architecture-independent files in PREFIX [default is /usr/local]

Le répertoire **PREFIX** sera utilisé par **make install**.
Son utilisation est obligatoire, à moins de construire un paquet et d'installer dans les répertoires système.

L'appel typique du script de configuration est:

::

    $ /home/joebar/armadito-web-ui/configure --prefix=/home/joebar/install


Compilation
-----------

::

    $ make


Installation
------------

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires du **PREFIX** défini au moment de la configuration.


Lancement de l'interface
------------------------

Tout d'abord, le daemon Armadito doit être lancé.

Ouvrez votre navigateur Web et accédez à l'URL suivante :

`<http://localhost:8888/app/index.html>`_


Débogage de l'interface
-----------------------

Une fois l'interface lancée :

- cliquez avec le bouton droit de la souris dans la fenêtre pour afficher le menu de débogage et sélectionnez «Inspecter» ou appuyez sur F12
- dans la fenêtre de l'inspecteur, sélectionnez l'onglet "console"


Compilation avec grunt
----------------------

Installer grunt :

::

         npm install -g grunt-cli

Exécuter `grunt` pour compiler et `grunt serve` pour l'aperçu.

Vous pouvez utiliser l'option "--force" si vous voulez compiler avec des warnings.
