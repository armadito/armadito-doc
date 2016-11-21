Compilation on Windows
======================

.. danger:: Graphical user interface is under redesign and new version is not yet ported to Windows. That will be fixed as soon as possible.

On Windows, you can compile Armadito AV sources with Visual Studio.
This has been tested with Visual Studio 2013.
You might have to apply some modifications regarding to which Visual Studio's version you use.

Tested on : Windows 7 64 bit with Service Pack 1.

Armadito solution for Visual Studio is divided in the following subprojects :

- Driver
	- ArmaditoGuard (driver sources)
	- ArmaditoGuard Package (driver package)
- Libarmadito
	- libarmadito (armadito core library)
- Modules
	- clamav_a6o (clamav module)
	- moduleH1	(heuristic module)
	- modulePDF (PDF module)
- Service
	- ArmaditoSvc (analysis service)
- Setup
	- ArmaditoGuard-setup (driver installation)
	- Armadito-db-setup (setup project for module databases)
	- Armadito-setup (setup project for armadito)

.. toctree::

   core_and_modules.rst
   driver.rst
   webui.rst


