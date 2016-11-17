Compilation sur Windows
======================

.. danger:: L'interface utilisateur graphique est en cours de refonte et la nouvelle version n'est pas encore portée à Windows. Ce sera réglé dès que possible.

Sous Windows, vous pouvez compiler des sources Armadito AV avec Visual Studio.
Cela a été testé avec Visual Studio 2013.
Vous devrez peut-être appliquer certaines modifications concernant la version de Visual Studio que vous utilisez.

Testé sur: Windows 7 64 bits avec Service Pack 1.

Armadito solution pour Visual Studio est divisé dans les sous-projets suivants:

- Chauffeur
	- ArmaditoGuard (sources pilotes)
	- Forfait ArmaditoGuard (forfait conducteur)
- Libarmadito
	- libarmadito (bibliothèque principale d'armadito)
- Modules
	- clamav_a6o (module clamav)
	- moduleH1 (module heuristique)
	- modulePDF (module PDF)
- Service
	- ArmaditoSvc (service d'analyse)
- Installer
	- ArmaditoGuard-setup (installation du pilote)
	- Armadito-db-setup (projet d'installation pour les bases de données des modules)
	- Armadito-setup (projet d'installation pour armadito)
.. toctree::

   core.rst
   clamav.rst
   modulePDF.rst
   moduleH1.rst
   driver.rst
   gui.rst
   
   
