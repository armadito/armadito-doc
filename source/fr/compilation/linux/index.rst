Compilation sur Linux
=====================

Sur linux, les sources de l'antivirus sont compilées en utilisant automake et autoconf pour générer les fichiers Makefiles.
Vous pouvez compiler chaque partie séparément par nous-mêmes.

Les sources sont accessibles publiquement sur github, dans des dépôts git séparés:

* Core : `<https://github.com/armadito/armadito-av>`_
* WebUI : `<https://github.com/armadito/armadito-web-ui>`_
* SystrayUI : `<https://github.com/armadito/armadito-systray-ui>`_
* Module Clamav : `<https://github.com/armadito/armadito-mod-clamav>`_
* Module PDF : `<https://github.com/armadito/armadito-mod-pdf>`_
* Module H1 : `<https://github.com/armadito/armadito-mod-h1>`_

.. toctree::
   :maxdepth: 2

   core.rst
   clamav.rst
   modulePDF.rst
   moduleH1.rst
   webui.rst
   systrayui.rst
