Armadito ClamAV module
======================

Le module Armadito ClamAV correspond à l'intégration de la bibliothèque libclamav dans Armadito-av.
Sous Windows, après la construction, une bibliothèque appelée ** clamav_a6o.dll ** sera générée. Il vise à interagir avec ** libarmadito.dll ** et ** libclamav.dll **.


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

Ensuite, sélectionnez le projet ** modules \\ clamav_a6o ** dans l'Explorateur de solutions et construisez-le.


En dehors
---------

Out dossier pourrait être l'un de ces:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

ou

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release

Si build a été un succès, vous devriez avoir ces fichiers:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\modules\clamav_a6o.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libclamav.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libeay32.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\ssleay32.dll


