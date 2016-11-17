Armadito module PDF
===================

Armadito module PDF est un module heuristique pour l'analyse de documents PDF.
Sur Windows, après la construction, une bibliothèque appelée ** modulePDF.dll ** sera générée.


Conditions préalables
-------------

* Microsoft Visual Studio 2013 (édition communautaire ou plus)
* Armadito fenêtres dépendances archives (deps.zip)
* Armadito PDF sources de github référentiel

Uncompress ** deps-x.zip ** dans le répertoire racine des sources armadito-av. Vous devriez avoir ces chemins de dépendances exactes:

::
    
   SOMEWHERE\armadito-av\deps\glib\...
   SOMEWHERE\armadito-av\deps\json-c\...

Afin d'obtenir des sources PDF Armadillo, vous devez cloner le dépôt public armadillo-pdf:

::
   
   cd SOMEWHERE\armadito-av\modules\modulePDF
   git clone https://github.com/armadito/armadito-pdf -b DEV


Construire
-----

Ouvrez la solution armadillo-av VS à l'emplacement:
 
::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Ensuite, sélectionnez le module ** modules \\ modulePDF ** dans l'Explorateur de solutions et créez-le.


En dehors
---

Out dossier pourrait être l'un de ces:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

ou 

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release

Si build a été un succès, vous devriez avoir ce fichier:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\modules\modulePDF.dll

