Armadito Windows Driver
=======================

Armadito Windows Driver est responsable de la protection en temps réel de l'antivirus Armadito.

Pré-requis
----------

* Microsoft Visual Studio 2013 (édition communautaire ou plus)
* Armadito windows dependencies archive (deps-x.zip)
* Windows Driver Kit 8.1

Pour obtenir Windows Driver Kit 8.1: <https://www.microsoft.com/en-us/download/details.aspx?id=42273>

.. warning:: Windows Driver Kit 8.1 va **seulement** avec MS Visual Studio 2013. Vous devez obtenir le WDK compatible avec votre version de Visual Studio.


Signature du driver
-------------------

Ajout de votre certificat au magasin local
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ouvrez l'outil Certificate Manager (certmgr.msc)
- Allez à **Certificats - Utilisateur actuel** > **Particulier** > **Certificats**
- Cliquez avec le bouton droit de la souris sur le dossier et choisissez **Toutes les tâches** > **Importer**
- Ensuite, suivez l'assistant pour importer votre certificat.


Signature avec votre certificat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ouvrez la solution Armadito-AV dans Visual Studio.
- Cliquez avec le bouton droit de la souris sur le projet **ArmaditoGuard** et sélectionnez **Propriétés**.
- Accédez à **Propriétés de configuration** > **Signature du pilote** > **Général**.
- **Signature mode** > **Signature du produit**.
- **Certificat de production** > **Sélectionnez dans le magasin** et sélectionnez votre certificat précédemment ajouté.
- Répétez les étapes précédentes pour le projet **ArmaditoGuard Package**.

Construire
----------

Ouvrez la solution Armadito-AV à l'emplacement suivant :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Premièrement, séléctionnez le projet **Driver\ArmaditoGuard** et lancez la compilation.

Puis, séléctionnez le projet **Driver\\ArmaditoGuard Package** et lancez la compilation.

Enfin, séléctionnez le projet **Setup\\ArmaditoGuard-setup** et lancez la compilation.


Le résultat de la compilation devrait se trouver dans le dossier suivant :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

or

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release


Si la compilation a été un succès, vous devriez avoir les fichiers correspondants :

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\armaditoguard.cat
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\armaditoguard.inf
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\armaditoguard.sys
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\ArmaditoGuard-setup.exe

.. toctree::


