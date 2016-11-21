Armadito WebUI
==============

.. danger:: L'interface utilisateur graphique est en cours de refonte et la nouvelle version n'est pas encore portée à Windows. Ce sera réglé dès que possible.


Pré-requis
----------

Les outils nécessaires sont les suivants :

* node.js
* Git
* bower


Installer node.js et bower
--------------------------

Tout d'abord, téléchargez node.js depuis https://nodejs.org/en/download/, en utilisant l'installateur .msi ou le programme d'installation .exe, à votre choix.

Pendant l'installation, les choix de configuration par défaut sont OK.

Vérification de l'installation:

::

	$ npm --version
	2.15.1

Puis installez bower en utilisant:

::

	$ npm install -g bower


Installer git
-------------

Pour utiliser bower, vous devez d'abord installer git.

Git pour windows est disponible ici: https://git-for-windows.github.io/

Vérification de l'installation:

::

	$ git version
    2.8.1.windows.1



Installation des modules dans l'arborescence des sources
--------------------------------------------------------

Utiliser bower à partir du répertoire **armadito-web-ui** pour installer les modules nécessaires:

::

     $ cd SOMEWHERE/armadito-web-ui
	 $ bower install
	 $ npm install


Exécution de l'interface
------------------------

Tout d'abord, le daemon Armadito doit être lancé.

Si c'est le cas, ouvrez votre navigateur Web et accédez à l'URL suivante :

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

         $ npm install -g grunt-cli

Exécuter `grunt` pour compiler et `grunt serve` pour l'aperçu.

Vous pouvez utiliser l'option "--force" si vous voulez compiler avec des warnings.

