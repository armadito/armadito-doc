Installation sur Linux
=====================

Installation à partir de sources
-------------------------

Lorsque vous installez Armadito AV à partir de sources (soit tarball ou git clone), vous devez d'abord le construire. Reportez-vous à la section **Compilation**> **Compilation sur Linux** de cette documentation pour obtenir des instructions détaillées.

Après la bonne configuration et la construction des différentes parties (noyau, modules, gui), chaque partie est simplement installée par la commande suivante:

::

    $ make install

Cela installera les bibliothèques, les outils, les fichiers d'en-tête ... dans les sous-répertoires du **PREFIX**
Répertoire défini au moment de la configuration.

Cette commande doit être répétée pour chaque répertoire (core /, modules / * /, gui /).

Il faut prendre soin de configurer chaque partie avec le même **préfixe** afin que les différents composants soient installés à leurs emplacements respectifs.


Installation à partir de paquets
--------------------------

Distributions Ubuntu
~~~~~~~~~~~~~~~~~~~~

Les packages pour les distributions Ubuntu sont disponibles à l'adresse suivante:

**URL**: <https://launchpad.net/~armadito/+archive/ubuntu/armadito-av>

::

      sudo add-apt-repository ppa:armadito/armadito-av


Notez que ce PPA est expérimental et que l'interface utilisateur graphique n'est pas encore emballée de manière propre.


.. toctree::
