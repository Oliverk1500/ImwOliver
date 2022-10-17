<center>

# Listado de directorios


</center>

***Nombre:*** Oliver Manuel Gonzalez Diaz
***Curso:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

### ÍNDICE

+ [Sitio web 1](#id1)
+ [Sitio web 2](#id2)
+ [Sitio web 3](#id3)
+ [Sitio web 4](#id4)



#### ***Sitio Web 1***. <a name="id1"></a>

    http://imw.nombre_alumno.me
        
        Debe mostrar una página con la imagen del "Diagrama de unidades de trabajo" de IMW":.
![](./images/10.png)
![](./images/1.png)


http://imw.nombre_alumno.me/mec/

    No utilizar un location.
    Debe mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC (ver moodle de la asignatura).

![](./images/2.png)

#### ***Sitio Web 2***. <a name="id2"></a>

    http://varlib.nombre_alumno.me:9000
    Debe mostrar el listado de ficheros y directorios de /var/lib de la máquina de producción.
    Pensar qué root definir para conseguir el objetivo planteado.

![](./images/11.png)

![](./images/3.png)

#### ***Sitio Web 3***. <a name="id3"></a>

    https://ssl.nombre_alumno.me/students/ (ojo, es https!)
    Debe pedir usuario/clave. Los datos son:
        USUARIO: usuario1
        CLAVE: 2asir
    Debe mostrar una página web con el nombre de todo el alumnado de clase.
    Se debe prohibir explícitamente el acceso al fichero htpasswd

![](./images/12.png)

![](./images/4.png)

![](./images/5.png)


> ***Sitio Web 4*** 

Muestro la pagina terminada.


    http://redirect.nombre_alumno.me

    Se debe redirigir cualquier petición de este dominio a http://target.aluXXXX.me
        http://redirect.nombre_alumno.me/test/ -> http://target.nombre_alumno.me
        http://redirect.nombre_alumno.me/probando/ -> http://target.nombre_alumno.me
        http://redirect.nombre_alumno.me/hola/ -> http://target.nombre_alumno.me
        ...

    Al acceder a http://target.nombre_alumno.me se debe mostrar la página web que se adjunta en el archivo initializr-verekia-4.0.zip.
        Para copiar y descomprimir el fichero initializr.zip se recomienda usar alguna de las siguientes herramientas: curl, wget, scp, unzip.

    Los logfiles deben ser:
        /var/log/nginx/redirect/access.log
        /var/log/nginx/redirect/error.log

![](./images/20.png)

![](./images/21.png)

![](./images/13.png)

![](./images/14.png)

![](./images/6.png)

![](./images/8.png)


