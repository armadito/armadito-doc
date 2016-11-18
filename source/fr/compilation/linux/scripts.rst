Préparer la compilation
***********************

Tout d'abord, vous devez télécharger des sources de notre github public. La prochaine chose que vous devez faire est de définir la variable OS_V dans le script principal "compile_all.sh".
Il correspond au nom du sous-répertoire out où seront stockés les éléments de compilation.

Par exemple, dans ** compile_all.sh **:
::

   OS_V=ubuntu-14.04-64


Compiler tout
*************

Si vous souhaitez tout compiler:
::

   $ cd armadito-av/scripts/
   $ ./compile_all.sh



Compiler module par module
**************************

Si vous souhaitez compiler un seul module, ou core:
::

   $ cd armadito-av/scripts/
   $ ./compile_all.sh PACKAGE


** PACKAGE ** pourrait être l'un des suivants:

* core (libarmadito)
* clamav (armadito-mod-clamav)
* moduleH1 (armadito-mod-moduleH1)
* modulePDF (armadito-mod-PDF)

Résultats de la compilation
***************************

Par défaut, les résultats de la compilation sont situés dans ** armadito-av / out / build / $ OS_V **.

L'étape suivante est l'installation, c'est-à-dire avec "make install".
