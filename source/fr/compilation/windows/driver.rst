Pilote Windows Armadito
=======================

Armadito Windows Driver est responsable de la protection sur l'accès de l'antivirus Armadito.

Conditions préalables
---------------------

* Microsoft Visual Studio 2013 (édition communautaire ou plus)
* Armadito fenêtres dépendances archives (deps.zip)
* Kit de pilotes Windows 8.1

Pour obtenir Windows Driver Kit 8.1: <https://www.microsoft.com/en-us/download/details.aspx?id=42273>

.. warning:: Windows Driver Kit 8.1 va ** seulement ** avec MS Visual Studio 2013. Vous devez obtenir le WDK compatible avec votre version de Visual Studio.


Signature du conducteur
-----------------------

Ajoutez votre certificat au magasin local
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ouvrez l'outil Certificate Manager (certmgr.msc)
- Allez à ** Certificats - Utilisateur actuel **> ** Particulier **> ** Certificats **
- Cliquez avec le bouton droit de la souris sur le dossier et choisissez ** Toutes les tâches **> ** Import **
- Ensuite, suivez l'assistant pour importer votre certificat.


Signer avec votre certificat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ouvrez la solution Armadito-av dans Visual Studio.
- Cliquez avec le bouton droit de la souris sur le projet ** ArmaditoGuard ** et sélectionnez ** Propriétés **.
- Accédez à ** Propriétés de configuration **> ** Signature du pilote **> ** Général **.
- ** Signe mode **> ** Signe du produit **.
- ** Certificat de production **> ** Sélectionnez dans le magasin ** et sélectionnez votre certificat précédemment ajouté.
- Répétez les étapes précédentes pour le projet ** ArmaditoGuard Package **.

Construire
----------

Ouvrez la solution armadillo-av VS à l'emplacement:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\Armadito-AV.sln

Firstly, select **Driver\ArmaditoGuard** project in Solution Explorer and build it.

Then, select **Driver\\ArmaditoGuard Package** project in Solution Explorer and build it.

Finally, select **Setup\\ArmaditoGuard-setup** project in Solution Explorer and build it.

Out
---

Out dossier pourrait être l'un de ces:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Debug

or

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\Release

Si build a été un succès, vous devriez avoir ce fichier:

::

   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\armaditoguard.cat
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\armaditoguard.inf
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\armaditoguard.sys
   SOMEWHERE\armadito-av\build\windows\VS12\Armadito-AV\out\[build_mode]\driver\ArmaditoGuard-setup.exe

.. toctree::


