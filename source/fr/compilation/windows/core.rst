Armadito core
=============

Armadito core correspond à libarmadito. Les symboles exportés depuis cette bibliothèque permettent à toutes les  modules d'utiliser la même API.
Sous Windows, le résultat de la compilation est une DLL : ** libarmadito.dll **.

Pré-requis
----------

* Microsoft Visual Studio 2013 (Community edition or more)
* Armadito windows dependencies archive (deps-x.zip)

Décompresser **deps-x.zip** dans le répertoire racine des sources armadito-av. Vous devriez avoir ces chemins de dépendances exactes:

::

   SOMEWHERE\armadito-av\deps\glib\...
   SOMEWHERE\armadito-av\deps\json-c\...

Compilation
-----------

Ouvrez la solution armadito-av VS à l'emplacement:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Ensuite, sélectionnez le projet **Lib-armadito\\libarmadito** dans l'Explorateur de solutions et lancez la compilation.

Le résultat de la compilation devrait se trouver dans le dossier suivant :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

ou

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release


Si la compilation a été un succès, vous devriez avoir ces fichiers:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\conf\armadito.conf
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\glib-2-vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\gmodule-2.vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\gthread-2.vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libarmadito.dll
