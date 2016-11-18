Armadito core
=============

Armadito core correspond à libarmadito bibliothèque. Les symboles exportés depuis cette bibliothèque permettent à toutes les bibliothèques de modules d'utiliser les mêmes API.
Sous Windows, après la construction, une librairie appelée ** libarmadito.dll ** sera générée.

Conditions préalables
---------------------

* Microsoft Visual Studio 2013 (Community edition or more)
* Armadito windows dependencies archive (deps-x.zip)

Uncompress ** deps-x.zip ** dans le répertoire racine des sources armadito-av. Vous devriez avoir ces chemins de dépendances exactes:

::

   SOMEWHERE\armadito-av\deps\glib\...
   SOMEWHERE\armadito-av\deps\json-c\...

Construire
----------

Ouvrez la solution armadito-av VS à l'emplacement:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Ensuite, sélectionnez le projet ** Lib-armadito \\ libarmadito ** dans l'Explorateur de solutions et créez-le.


En dehors
---------

Out dossier pourrait être l'un de ces:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

or

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release

Si build a été un succès, vous devriez avoir ces fichiers:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\conf\armadito.conf
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\glib-2-vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\gmodule-2.vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\gthread-2.vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libarmadito.dll
