Installation sur Windows
=======================

Conditions préalables
*********************

Packages redistribuables Visual C++ for Visual Studio 2013:
	- vcredist_x64.exe
	- vcredist_x86.exe

**URL** : https://www.microsoft.com/fr-fr/download/details.aspx?id=40784


Installation avec l'installateur MSI
************************************

1. Téléchargez et installez les prérequis (voir la section précédente)

2. Télécharger armadito-av msi:

	- Armadito-db-setup-0.10.0.msi
	- Armadito-setup-0.10.0.msi

3. Installer les bases de données des modules armadito-av:

	Lancez l'installeur Armadito-db-setup-0.10.0.msi

4. Installez armadito-av (service d'analyse + interface utilisateur grapique)

	Lancez le programme d'installation Armadito-setup-0.10.0.msi

Installation à partir de sources
********************************

1. Créez les sources armadito-av à partir du projet de solution Visual Studio.

Suivez les instructions de la section ** Compilation **> ** Compilation sous Windows ** de cette documentation.

2. Copiez les fichiers de bases de données du module dans le référentiel:

::

    SOMEWHERE\\armadito-av\\build\\windows\\VS\\Armadito-AV\\out\\[build_mode]\\modules\\DB

3. Installez le pilote en exécutant la commande suivante dans une invite en tant qu'administrateur:

::

    ArmaditoGuard-setup --install

4. Installez le service d'analyse en exécutant la commande suivante dans une invite en tant qu'administrateur:

::

    ArmaditoSvc --installBoot (service started at system start)

ou

::

    ArmaditoSvc --install (service started on demand)

.. toctree::

