# Fintri
Fintri es la aplicación perfecta para quienes buscan controlar y optimizar sus finanzas de manera personalizada y eficiente. Ofrece un panel de control dinámico y personalizable, con la posibilidad de cambiar colores para reflejar tu estilo. Con un enfoque en la gestión integral de tu cartera, Fintri te permite ver tu saldo total, excluyendo ahorros, y asignar tipos a tus ahorros para recibir sugerencias personalizadas de inversión.

Con Fintri, puedes:

* Visualizar sugerencias de inversión: Según el tipo de ingresos que percibes, te recomendamos las mejores estrategias de inversión, promoviendo la diversificación y el aumento de tus activos.

* Generar resúmenes anuales: Accede a hojas de resumen que te muestran, mes a mes, el estado de tus finanzas y cómo has distribuido tus gastos.

* Analizar tus gastos: ¿Te preguntas en qué te gastas el dinero? Fintri incluye un módulo, asistido por IA, que divide tu información para brindarte un análisis detallado.

* Notificaciones y alertas: Recibe correos electrónicos que te notifican de pagos pendientes y movimientos importantes en tu cartera, manteniéndote siempre al día.

* Comparar precios de vivienda: Fintri te ayuda a decidir si es mejor arrendar o comprar, sugiriendo precios de vivienda según tu nivel de ingresos y permitiéndote ajustar tus metas.

* Gestión de deudas: Mantén un registro de cuánto debes y cómo avanzas en el pago de tus deudas, ya sean en productos como CDT, fiducias, bonos, o cualquier otro tipo de instrumento financiero.

* Ahorros en pareja: Si manejas tus finanzas con tu pareja, Fintri te permite visualizar cuánto han ahorrado juntos y el estado de sus compromisos financieros compartidos.

Además, la aplicación ofrece una plataforma intuitiva donde puedes gestionar tu menú, editar, ocultar o mover los elementos para adaptarlos a tus necesidades, y controlar cada aspecto de tus finanzas, ya seas independiente o empleado.

#Instalacion

creamos nuestro entorno
```uv venv```
```
source .venv/bin/activate
```

### ejecución en docker

el comando construira el contenedor docker para correr en entorno docker

```
docker-compose up --build

docker compose build

bajar y borrar los volumenes 

docker-compose down -v #comando para desmontar y eliminar volumnes para cambios y pruebas
```
una vez construido lo ponemos a corer en un deamon de docker 
```
docker compose up -d
```
para ver que esta corriendo solo ponemos
```docker ps```
vera algo como esto
```shell
CONTAINER ID IMAGE          COMMAND                 CREATED        STATUS                                 PORTS                   NAMES
0012b25e4973 fintri-api     "uvicorn app.main:ap…"  0 seconds ago  Up 4 seconds                           0.0.0.0:8000->8000/tcp  fintri_api
bfe920519745 postgres:16.3  "docker-entrypoint.s…"  0 seconds ago  Restarting (1) Less than a second ago                          postgres_db
```
---

### si deseo conectarme a base de datos
conectarme a la db desde consola 

```docker exec -it postgres_db psql -U p_finanzas -d finanzas```



# WEBgrafia
https://medium.com/bitgrit-data-science-publication/forget-pip-install-use-this-instead-754863c58f1e
https://ryxcommar.com/2024/02/15/how-to-cut-your-python-docker-builds-in-half-with-uv/