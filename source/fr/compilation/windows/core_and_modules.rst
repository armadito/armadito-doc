Libarmadito et modules
======================

Les symboles exportés par libarmadito permettent à tous les  modules d'utiliser la même API.
Sous Windows, le résultat de la compilation est une DLL : ** libarmadito.dll **.
Pour plus de simplicité, nous avons regroupé les dépendances windows dans une archive générée de manière automatique.


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

Ouvrez la solution Armadito-AV à l'emplacement:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Sélectionnez le projet correspondant dans l'Explorateur de solutions selon ce que vous souhaitez compiler :

* **Core** : Lib-armadito\\libarmadito
* **Module clamav** : modules\\clamav_a6o
* **Module PDF** : modules\\modulePDF
* **Module H1** : modules\\moduleH1


Enfin, lancez la compilation (Run).


Le résultat de la compilation devrait se trouver dans le dossier suivant :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

ou

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release


Si la compilation a été un succès, vous devriez avoir les fichiers correspondants :

Core :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\conf\armadito.conf
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\glib-2-vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\gmodule-2.vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\gthread-2.vs12.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libarmadito.dll


Module clamav :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\modules\clamav_a6o.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libclamav.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\libeay32.dll
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\ssleay32.dll


Module PDF :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\modules\modulePDF.dll

Module H1 :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\modules\moduleH1.dll

