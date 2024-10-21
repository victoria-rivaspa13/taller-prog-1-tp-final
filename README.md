# Trabajo Práctico Final Taller de Programación 1

El objetivo de este trabajo es desarrollar un pequeño "pipeline" de análisis de logs de un servidor web. Usarán bash para manipular archivos, expresiones regulares para filtrar información, git para el control de versiones y python para analizar los datos.

Un servidor web genera archivos de log con información sobre los accesos de los usuarios. Estos logs incluyen direcciones ip, la página accedida, el código de estado HTTP, y la fecha del acceso. Tienen que procesar esos registros y generar un pequeño análisis para extraer la información útil.

# Consigna

Hacer un fork de este repositorio, la entrega constara de entregar al (los) profesor(es) el link a su repositorio de Github.

Se deberá entregar:

1. Un script de bash que descargue el archivo .zip de la siguiente url: https://gist.githubusercontent.com/sebiglesias/ea2faa92f4b25a79f811104584e91efb/raw/02378f041ae64d3d021031efeb1572cbddfc2fc7/test-web-server-log.txt
   1. El script debe descargar el archivo, y generar dos nuevos archivos a partir del mismo, uno que tendrá todas las líneas de registros con código 200 `ok.txt` y otro archivo con todas las lineas que tengan un código 500 `errors.txt`.
   2. Pueden utilizar `curl`, `grep` y el operador `>>`

2. Un archivo de python que imprima por consola:
    1. Las IPs que visitaron el sitio y cuántas veces cada IP accedió
    2. Indique cuales son las 3 páginas más visitadas
    3. El porcentaje de accesos exitosos (codigos 200). 

3. Un archivo Jupyter con:
   1. Un gráfico de barras con las IPs que visitaron el sitio y la cantidad de veces que accedió al sitio (pueden utilizar `matplotlib` https://matplotlib.org/)
   2. Un gráfico circular que indique la proporción de los diferentes códigos HTTP.
   3. Una celda markdown que explique lo que indican los gráficos
