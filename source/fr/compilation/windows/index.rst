Compilation sur Windows
=======================

.. danger:: L'interface graphique est en cours de refonte et la nouvelle version n'est pas encore portée pour Windows.

Sous Windows, vous pouvez compiler des sources Armadito AV avec Visual Studio.
Cela a été testé avec Visual Studio 2013.
Vous devrez peut-être appliquer certaines modifications concernant la version de Visual Studio que vous utilisez.

Testé sur: Windows 7 64 bits avec Service Pack 1.

La solution Armadito pour Visual Studio est constitué des sous-projets suivants:

- Driver
	- ArmaditoGuard (sources)
	- ArmaditoGuard Package (installeur)
- Libarmadito
	- libarmadito (Armadito core)
- Modules
	- clamav_a6o (module clamav)
	- moduleH1 (module heuristique)
	- modulePDF (module PDF)
- Service
	- ArmaditoSvc (service d'analyse)
- Installer
	- ArmaditoGuard-setup (installation du driver)
	- Armadito-db-setup (projet d'installation pour les bases de données des modules)
	- Armadito-setup (projet d'installation pour armadito)

.. toctree::

   core.rst
   clamav.rst
   modulePDF.rst
   moduleH1.rst
   driver.rst
   webui.rst


