Armadito module H1
==================

Le module Armadito H1 est un module de balayage dédié à l'analyse des binaires (PE et ELF).
Sous Windows, après la génération, une bibliothèque appelée ** moduleH1.dll ** sera générée.


Conditions préalables
---------------------

* Microsoft Visual Studio 2013 (édition communautaire ou plus)
* Armadito fenêtres dépendances archives (deps.zip)

Uncompress ** deps-x.zip ** dans le répertoire racine des sources armadito-av. Vous devriez avoir ces chemins de dépendances exactes:

::

   SOMEWHERE\armadito-av\deps\glib\...
   SOMEWHERE\armadito-av\deps\json-c\...

Construire
----------
Ouvrez la solution armadillo-av VS à l'emplacement:
::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Ensuite, sélectionnez le module **modules \\ moduleH1** dans l'Explorateur de solutions et construisez-le.


En dehors
---------

Out dossier pourrait être l'un de ces:
::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

ou

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release

Si build a été un succès, vous devriez avoir ce fichier:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\modules\moduleH1.dll


