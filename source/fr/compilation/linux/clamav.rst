Armadito ClamAV module 
======================

**Armadito ClamAV** module correspond à l'intégration de libclamav bibliothèque dans Armadito-av. 

Les sources sont publiquement disponibles sur github.com, vous pouvez l'obtenir avec la commande suivante :

::

   $ git clone https://github.com/armadito/armadito-mod-clamav.git -b DEV

Les prérequis
-------------

Pour compiler le module Armadito ClamAV, vous avez besoin des outils suivants:

- automake/autoconf
- GNU make
- C compiler
- libclamav library and headers

.. warning:: Assurez-vous d'avoir **Armadito core** bibliothèque avant d'essayer de construire ce module.

- Ubuntu: 

::

     apt-get install libclamav-dev

Configuration
-------------


Pour initialiser la construction en utilisant automake, autoconf et tools, un script shell 
**autogen.sh** est prévu pour faciliter cette étape:

::

    $ ./autogen.sh
    + aclocal --force
    + libtoolize --force --automake --copy
    + automake --foreign --add-missing --force-missing --copy
    + autoconf --force

Cela **Makefile.in** fichiers et les scripts de **configuration**.

**configure** script prend les options utiles suivantes:

    --prefix=PREFIX         installe l'architecture-independent de PREFIX
                            [/usr/local]
    --enable-debug          enable debugging [default is yes]

Le répertoire ** PREFIX ** sera utilisé par ** make install **. Son utilisation est obligatoire, sauf si
la construction d'un paquet et l'installation dans les répertoires système.

libarmadito utilise le **pkg-config** pour spécifier les options de compilation relatives à
libarmadito. Depuis **libarmadito.pc** fichier de spécification pour **pkg-config** n'est pas situé
dans le repertoire standard (habituel **/usr/lib/pkgconfig**), appel du script configure 
doit utiliser le **PKG_CONFIG_PATH** environnement variable.

Bâtir dans un répertoire distinct est fortement recommandé, sauf si vous voulez vraiment
à clobber le sourcetree avec des objets, des bibliothèques, des binaires et d'autres choses.

::

    $ mkdir /home/joebar/build/modules/clamav

L'appel typique du script de configuration est:

::

    $ /home/joebar/armadito-av/modules/clamav/configure --prefix=/home/joebar/install --enable-debug PKG_CONFIG_PATH=/home/joebar/install/lib/pkgconfig

Notez que le chemin spécifié dans la valeur de**PKG_CONFIG_PATH** doit être cohérent
avec le **PREFIX** utilisé dans l'installation libarmadito (voir **Armadito core** section de construction linux).


Bâtiment
--------

Une fois configuré, la construction est facile:

::

    $ make


Installation
----------

Après la construction, l'installation se fait par:

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires de la **PREFIX**
défini au moment de la configuration. 

