Armadito core
=============

Armadito core corresponds to libarmadito library. Symbols exported from this library allows all modules to use same API.
On Windows, after build, a library called **libarmadito.dll** will be generated.
For more simplicity, dependencies have been regrouped into a single zip archive automatically generated.

Prerequisites
-------------

* Microsoft Visual Studio 2013 (Community edition or more)
* Armadito windows dependencies archive (deps-x.zip)

Uncompress **deps-x.zip** in armadito-av sources root directory. You should have then these exact dependencies paths :

::

   SOMEWHERE\armadito-av\deps\glib\...
   SOMEWHERE\armadito-av\deps\json-c\...

Build
-----

Open the armadito-av VS solution at location :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln


Select project you intend to build in Solution's Explorer :

* **Core** : Lib-armadito\\libarmadito
* **Module clamav** : modules\\clamav_a6o
* **Module PDF** : modules\\modulePDF
* **Module H1** : modules\\moduleH1

Then, launch the build (Run).

Out folder could be one of these :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

or

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release


If build has been successful, you should have these files :

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
