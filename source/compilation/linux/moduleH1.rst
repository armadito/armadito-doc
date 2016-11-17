Armadito H1 module 
==================

**Armadito H1** module est un module de balayage dédié à l'analyse des binaires (PE et ELF).

Les sources sont accessibles au public sur github.com, vous pouvez l'obtenir avec la commande suivante:

::

   $ git clone https://github.com/armadito/armadito-mod-h1.git -b DEV

Prérequis
-------------

Afin de compiler le module Armadito H1, vous avez besoin des outils suivants:

- automake / autoconf
- Fabrication GNU
- Compilateur C


.. warning:: Assurez-vous d'avoir construit la bibliothèque ** Armadito core ** avant d'essayer de construire ce module.


Configuration
-------------

Pour initialiser la compilation à l'aide de automake, autoconf et tools, un script shell
** autogen.sh ** est fourni pour faciliter cette étape:

::

    $ ./autogen.sh
    + aclocal --force
    + libtoolize --force --automake --copy
    + automake --foreign --add-missing --force-missing --copy
    + autoconf --force

Cela générera les fichiers ** Makefile.in ** et le script ** configure **.

**configure** script prend les options utiles suivantes:

    --prefix=PREFIX         install architecture-independent files in PREFIX
                            [/usr/local]
    --enable-debug          enable debugging [default is yes]

Le répertoire ** PREFIX ** sera utilisé par ** make install **. Son utilisation est obligatoire, sauf si la construction d'un paquet et l'installation dans les répertoires système.

Libarmadito utilise l'utilitaire ** pkg-config ** pour spécifier des options de compilation relatives à Libarmadito. Étant donné que le fichier de spécification ** libarmadito.pc ** pour ** pkg-config ** n'est pas situé
Dans le répertoire standard (habituel ** / usr / lib / pkgconfig **), appelant le script configure doit utiliser la variable d'environnement ** PKG_CONFIG_PATH **.

Bâtir dans un répertoire distinct est fortement recommandé, sauf si vous voulez vraiment pour gifler l'arbre source avec des objets, des bibliothèques, des binaires et d'autres choses.

::

    $ mkdir /home/joebar/build/modules/moduleH1


L'appel typique du script de configuration est:

::

    $ /home/joebar/armadito-av/modules/moduleH1/configure --prefix=/home/joebar/install --enable-debug PKG_CONFIG_PATH=/home/joebar/install/lib/pkgconfig


Notez que le chemin spécifié dans la valeur de ** PKG_CONFIG_PATH ** doit être cohérent avec ** PREFIX ** utilisé dans l'installation libarmadito (voir ** Armadito core ** linux build section).


Bâtiment
......

Une fois configuré, la construction est facile:

::

    $ make


Installation
----------

Après la construction, l'installation se fait par:

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires du ** PREFIX **
Répertoire défini au moment de la configuration.
