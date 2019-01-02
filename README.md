# SalesAdminOdoo
Primero se descarga vmware para hacer la instalación de ubuntu.
Al hacer esto se instala postgresql, git y las dependencias de python para poder empezar a trabajar.
Posterior a todo esto ya podemos descargar del repositorio de git odoo.
El Módulo esta creado en una carpeta local con la ruta Odoo/customaddons/sales ejecutándolo con el siguiente comando:
./odoo.py --addons-path=customaddons,addons -d sales -u sales
