Armadito modules
================

La compilation est relativement la même pour les différents modules d'analyse de l'antivirus Armadito.
Il n'est pas nécessaire de compiler/installer tous les modules pour utiliser l'antivirus.
Le choix des modules est en effet totalement libre.

.. warning:: Assurez-vous d'avoir compilé **libarmadito** (core) avant de compiler un de ces modules.

Les prérequis
-------------

Pour compiler un module, vous avez besoin des outils suivants:

- automake/autoconf
- GNU make
- C compiler
- libarmadito (core)

Certains modules ont des dépendances supplémentaires :

armadito-mod-clamav :
 - libclamav library and headers. Ubuntu : libclamav-dev

armadito-mod-yara :
 - libyara library and headers. Ubuntu : libyara-dev

armadito-mod-h1 :
 - pas de dépendances supplémentaires

armadito-mod-pdf :
 - pas de dépendances supplémentaires

Clone
-----

::

    git clone -b DEV https://github.com/armadito/armadito-mod-clamav.git
    git clone -b DEV https://github.com/armadito/armadito-mod-yara.git
    git clone -b DEV https://github.com/armadito/armadito-mod-h1.git
    git clone -b DEV https://github.com/armadito/armadito-mod-pdf.git


Configuration
-------------

Une fois le repo cloné, vous devez initialiser la compilation en utilisant automake et autoconf. Un script shell
**autogen.sh** est d'ailleurs prévu pour faciliter cette étape:

::

    $ ./autogen.sh
    + aclocal --force
    + libtoolize --force --automake --copy
    + automake --foreign --add-missing --force-missing --copy
    + autoconf --force

Cela générera les fichiers **Makefile.in** et **configure**.

**configure** script prend les options suivantes:

    --prefix=PREFIX         installe l'architecture-independent de PREFIX
                            [/usr/local]
    --enable-debug          enable debugging [default is yes]

Le répertoire **PREFIX** sera utilisé par **make install**. Son utilisation est obligatoire, sauf pour
la création d'un paquet ou l'installation dans les répertoires du système.

libarmadito utilise **pkg-config** pour spécifier les options de compilation relatives à
libarmadito. Puisque le fichier de spécification **libarmadito.pc** pour **pkg-config** n'est pas situé
dans le repertoire standard (habituel **/usr/lib/pkgconfig**), l'appel du script configure
doit inclure la variable d'environnement **PKG_CONFIG_PATH**.

Compiler dans un répertoire distinct est fortement recommandé, sauf si vous voulez vraiment
ajouter dans les sources des objets, des bibliothèques, des binaires et d'autres choses.

Par exemple :

::

    $ REPO_GIT/configure --prefix=/home/joebar/install --enable-debug PKG_CONFIG_PATH=/home/joebar/install/lib/pkgconfig

Notez que le chemin spécifié dans la valeur de **PKG_CONFIG_PATH** doit être cohérent
avec le **PREFIX** utilisé dans l'installation libarmadito (voir **Armadito core** compilation sur linux).


Compilation
-----------

::

    $ make


Installation
------------

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires du chemin **PREFIX**
défini au moment de la configuration. Exemple: /home/joebar/install/...

