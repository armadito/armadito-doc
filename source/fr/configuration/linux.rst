Configuration sous Linux
========================

Armadillo AVs configuration sur Linux est stocké dans deux fichiers:

* /etc/armadillo/armadillo.conf
* /etc/armadito/conf.d/on-access-linux.conf

.. note:: Si vous avez compilé à partir de sources, ces fichiers de configuration se trouvent dans votre répertoire PREFIX.

.. warning:: La configuration présentée dans ce document est utilisée uniquement à des fins d'illustration.

Analyse à la demande
~~~~~~~~~~~~~~~~~~~~

Vous pouvez configurer le fonctionnement de l'analyse à la demande dans ** / etc / armadito / armadito.conf **:

::

   [on-demand]
   white-list-dir = "/boot"; "/dev"; "/etc"; "/proc"; "/run"; "/sys"; "/var"
   mime-types="*"
   modules="clamav"; "moduleH1"
   max-size = 10048576

* **white-list-dir** : Liste des répertoires exclus de l'analyse à la demande.
* **mime-types** : Types de fichiers MIME analysés lors d'une analyse à la demande.
* **modules** : Modules utilisés par l'analyse à la demande.
* **max-size** : Taille maximale des fichiers numérisés lors de l'analyse à la demande.

Numérisation à l'accès
~~~~~~~~~~~~~~~~~~~~~~


L'analyse à l'accès d'Armadito AV s'appuie principalement sur l'API fanotify.
Vous pouvez trouver plus d'informations sur la façon dont il fonctionne en lisant la page de manuel: `fanotify man7 <http://man7.org/linux/man-pages/man7/fanotify.7.html>` _.

La configuration de l'analyse à l'accès peut être effectuée en modifiant ** / etc / armadito / conf.d / on-access-linux.conf **:

::

   [on-access]
   enable=1
   enable-permission=1
   enable-removable-media=1
   mount="/home"
   directory="/var/tmp"; "/tmp"
   white-list-dir = "/bin"; "/boot"; "/dev"; "/etc"; "/lib"; "/lib32"; "/lib64"
   mime-types = "application/x-executable"; "application/pdf"; "application/zip"
   modules = "clamav"
   max-size = 10048576


* **activer** : Activez (1) ou désactivez (0) l'analyse à l'accès.
* **enable-permission**: validation (1) ou désactivation (0) vérification d'autorisation.

   * Si **activé**, les fichiers détectés comme malveillants seront bloqués par Armadito AV.
   * Si **désactivé**, les fichiers détectés comme malveillants ne seront notifiés.
* **enable-removable-media**: active (1) ou désactive (0) la surveillance des médias amovibles.

  * Si **activé**, des points de montage de supports amovibles seront ajoutés à la volée à la liste de surveillance.
* **mount**: liste des répertoires qui seront surveillés par des points de montage. C'est à dire. En utilisant FAN_MARK_MOUNT.
* **répertoire**: liste des répertoires qui seront surveillés par un marquage récursif de tous les sous-répertoires.
* **white-list-dir**: liste des répertoires exclus de l'analyse à la demande.
* **mime-types**: Types de fichiers MIME analysés lors d'une analyse à la demande.
* **modules**: Modules utilisés par l'analyse à la demande.
* **max-size**: Taille maximale des fichiers numérisés lors d'une analyse à la demande.


Alertes de virus
~~~~~~~~~~~~~~~~

Lorsqu'un virus est détecté par Armadito AV, un rapport d'alerte est généré et stocké dans un emplacement défini.
Cela peut être configuré en modifiant **/ etc / armadito / armadito.conf**:

::

   [alert]
   alert-dir = "/var/spool/armadito"

* **alert-dir** : Dans lequel les alertes d'analyse seront stockées.

Quarantaine
~~~~~~~~~~~

Pour isoler les fichiers infectés, Armadito AV peut placer les fichiers détectés en quarantaine.
**/ etc / armadito / armadito.conf** contient la configuration de la quarantaine:

::

   [quarantine]
   enable = 0
   quarantine-dir = "/var/lib/armadito/quarantine"

* **enable**: active (1) ou désactive (0) la quarantaine.
* **quarantine-dir**: répertoire où seront déplacés les fichiers mis en quarantaine.


.. toctree::


