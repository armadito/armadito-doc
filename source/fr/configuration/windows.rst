Configuration sur Windows
========================

La configuration de l'antivirus sur Windows peut être modifié dans le fichier suivant:

* <**install_dir**>\\Armadito-av\\conf\\armadito.conf

.. note:: By default, **install_dir** is *C:\\Program Files\\Teclib*.


Analyse à la demande
~~~~~~~~~~~~~~~~~~~~

Vous pouvez configurer le fonctionnement de l'analyse à la demande dans **<install_dir>\\Armadito-av\\conf\\armadito.conf** :

::

   [on-demand]
   white-list-dir = "C:\\wl-dir1\\"; "C:\\wl-dir2\\"
   mime-types="*"
   modules="clamav"; "moduleH1"
   max-size = 10048576

* **white-list-dir** : Liste des répertoires exclus de l'analyse à la demande (non encore implémentée).
* **mime-types** : Types de fichiers MIME analysés lors d'une analyse à la demande.
* **modules** : Modules utilisés par l'analyse à la demande.
* **max-size** : Taille maximale des fichiers numérisés lors de l'analyse à la demande.


Analyse en temps réel
~~~~~~~~~~~~~~~~~~~~~

Vous pouvez configurer le fonctionnement de l'analyse en temps réel dans **<install_dir>\\Armadito-av\\conf\\armadito.conf** :

::

   [on-access]
   enable = 0
   mime-types="*"
   modules="clamav"

* **enable**: activer (1) ou désactiver (0) la protection en temps réel.
* **mime-types**: Types de fichiers MIME numérisés lors de l'analyse en temps réel.
* **modules**: Modules utilisés par la protection en temps réel.


Alertes de virus
~~~~~~~~~~~~~~~~

Pas encore implémenté.

Quarantaine
~~~~~~~~~~~

Pour isoler les fichiers infectés, Armadito AV peut placer les fichiers détectés en quarantaine.
**<dir_installation>\\Armadito-av\\conf\\armadito.conf** contient la configuration de la quarantaine :

::

   [quarantine]
   enable = 0
   quarantine-dir = "quarantine"

* **enable** : Activer (1) ou désactiver (0) la quarantaine.
* **quarantine-dir** : Sous-répertoire où seront déplacés les fichiers mis en quarantaine.


.. toctree::


