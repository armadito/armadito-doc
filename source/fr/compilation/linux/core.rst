Armadito core
=============

**Armadito core** correspond à la librairie libarmadito. Les symboles exportés depuis cette bibliothèque permettent à toutes les bibliothèques de modules d'utiliser les mêmes API.

Les sources sont accessibles au public sur github.com, vous pouvez l'obtenir avec la commande suivante:

::

   $ git clone https://github.com/armadito/armadito-av.git -b DEV

Les prérequis
-------------

Pour construire libarmadito, vous avez besoin des outils suivants:

- automake / autoconf
- Fabrication GNU
- Compilateur C
- glib, libmagic, libxml2, libmicrohttpd, bibliothèques libcurl et en-têtes

Pour installer les en-têtes nécessaires:

- Ubuntu:

::

     apt-get install automake autoconf libtool libglib2.0-dev libmagic-dev libxml2-dev libjson-c-dev libmicrohttpd-dev libcurl4-openssl-dev

- Fedora:

::

     dnf install automake autoconf libtool glib2-devel file-devel libxml2-devel json-c-devel libmicrohttpd-devel libcurl-devel


Configuration
-------------

Une fois git repo cloné, vous devez initialiser la construction en utilisant automake, autoconf et des outils.
Un script shell **autogen.sh** est prévu pour faciliter cette étape :

::

    $ ./autogen.sh
    + aclocal --force
    + libtoolize --force --automake --copy
    + autoheader --force
    + automake --foreign --add-missing --force-missing --copy
    + autoconf --force

Cela **Makefile.in** fichiers et les **configure** script.

**configure** script prend les options utiles suivantes:

    --prefix=PREFIX         install architecture-independent files in PREFIX [default is /usr/local]
    --enable-debug          enable debugging [default is yes]

Le répertoire ** PREFIX ** sera utilisé par ** make install **. Son utilisation est obligatoire, sauf si
La construction d'un paquetage et l'installation dans les répertoires système,
Les modules de balayage et l'interface utilisateur graphique aura besoin d'un libarmadito correctement
Installé.

Bâtir dans un répertoire distinct est fortement recommandé, sauf si vous voulez vraiment
Pour gifler l'arbre source avec des objets, des bibliothèques, des binaires et d'autres choses.

::

    $ mkdir /home/joebar/build/libarmadito

L'appel typique du script de configuration est:

::

    $ /home/joebar/armadito-av/libarmadito/configure --prefix=/home/joebar/install --enable-debug


Construction
------------

Une fois configuré, la construction est facile:

::

    $ make

Installation
------------

Après la construction, l'installation se fait par:

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires du ** PREFIX **
Répertoire défini au moment de la configuration.

.. toctree::
