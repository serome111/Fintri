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


# lluvia de ideas

Cambio de color el panel o personalizacion
Saldo en cartera que es el total sin ahorro
El ahorro deberia tener un tipo, asi si no tiene tipo asignado se pueden dar sugerencias, para que invierta el miserable.
Sugerencias por tipo de ingresos, Dado que x ingreso es mejor que este sugerir aumentar inversiones en x tipo de ingreso, y recomendar diversificacion
Hoja de resumenes anual segun mes seleccionado, para ver
En que me gasto mi dinero? (Chat gpt modulo para dividir informacion)
https://gratu.co/collections/planeadores-1/products/planeador-financiero-digital
Envio de correos para notificar pagos, una ves se registre cree notificaciones de pagos pendientes
cituacio
analisis de cuanto gastas en promedio en mercado u otros productos
Decir si es mas facil arrendar o comprar y cual es el precio de vivienda segun tu ingreso que puedes aspirar
Si soy perfil independiente calcular pago de planillas basado en ingresos como empleado
cuanto debo y cuanto voy pagando= Pago de deudas
	TIPO2=cdt,nu,fiducia,bono….
	tipo3- fijjo o no fijo
Ahorros en parejas para el software que hago
Cuanto has pagado cuento debes
https://www.youtube.com/watch?v=-_gjUHS3nWU
Administrar panel, editar ocultar o mover como se ve mi mi menu
Conectar con algun banco o billetera telefonica
https://youtu.be/Uj64fpTNe8s
https://youtu.be/wacQPTem7Uc


# WEBgrafia
https://medium.com/bitgrit-data-science-publication/forget-pip-install-use-this-instead-754863c58f1e
https://ryxcommar.com/2024/02/15/how-to-cut-your-python-docker-builds-in-half-with-uv/