[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18155601&assignment_repo_type=AssignmentRepo)
<h1>Author</h1>
<p1>Carlos Eduardo Escarzaga Vazquez - 215024</p1>

<head>
  <title>Sistema de Gestion de Citas</title>
</head>

<div>
  <h1>Sistema de Gestion de Citas - Centro de Psicologia</h1>
  <p>>Este proyecto es un sistema web desarrollado en Django que permite la gestión de citas de un centro de psicología.<br>
    Las recepcionistas pueden registrarse, iniciar sesión, agendar citas, ver citas registradas, editar o eliminar citas.</p>
  
  <hr>

  <h2>Requisitos del sistema</h2>
  <ul>
    <li><strong>1. Registro de recepcionistas</strong><br>El sistema debe permitir que recepcionistas nuevas se registren con nombre, apellido, email, teléfono y contraseña.</li>
    <li><strong>2. Inicio de sesion</strong><br>El sistema debe permitir que una recepcionista pueda iniciar sesión utilizando su correo electrónico y contraseña.</li>
    <li><strong>3. Cierre de sesion</strong><br>El sistema debe permitir que la recepcionista pueda cerrar sesión en cualquier momento.</li>
    <li><strong>4. Agendar cita</strong><br>El sistema debe permitir registrar una nueva cita, ingresando nombre del paciente, teléfono, fecha, hora y motivo.</li>
    <li><strong>5. Lista de citas</strong><br>El sistema debe mostrar a la recepcionista todas las citas agendadas asociadas a su cuenta.</li>
    <li><strong>6. Busqueda de citas</strong><<br>El sistema debe permitir buscar citas por el nombre del paciente.</li>
    <li><strong>7. Editar citas</strong><br>El sistema debe permitir modificar los datos de una cita ya agendada.</li>
    <li><strong>8. Eliminar citas</strong><br>El sistema debe permitir eliminar citas registradas.</li>
    <li><strong>9. Proteccion de vistas</strong><br>El sistema debe restringir el acceso a la gestión de citas solo a usuarios autenticados.</li>
    <li><strong>10. Mensajes de confirmacion y error</strong><br>El sistema debe mostrar mensajes de éxito o error en acciones como login y logout</li>
  </ul>

  <hr>

  <h2>Funcionalidades del sistema</h2>

  <ul>
    <li>Registro de recepcionistas.</li>
    <li>Inicio de sesión y cierre de sesión de recepcionistas.</li>
    <li>Agendado de nuevas citas (con datos de paciente, fecha, hora y motivo).</li>
    <li>Edición de citas agendadas.</li>
    <li>Eliminación de citas registradas.</li>
    <li>Búsqueda de citas por nombre de paciente.</li>
    <li>Sistema de mensajes de confirmación y error</li>
    <li>Protección de vistas: solo usuarios autenticados pueden gestionar citas.</li>
  </ul>

  <hr>

  <h2>Requisitos del sistema</h2>
  <ul>
    <li>Python 3.13+</li>
    <li>Django 5.2</li>
  </ul>

  <h2>Instalación del proyecto</h2>
    <ol>
        <li>Clonar el repositorio:
            <pre><code>git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO</code></pre>
        </li>
        <li>Crear y activar un entorno virtual:
            <pre><code>pip install virtualenv
source venv/Scripts/activate  # En Windows</code></pre>
        </li>
        <li>Instalar dependencias:
            <pre><code>pip install django</code></pre>
        </li>
        <li>Crear las migraciones y migrar la base de datos:
            <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
        </li>
        <li>Levantar el servidor:
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li>Acceder a:
            <pre><code>http://localhost:8000</code></pre>
        </li>
    </ol>
</div>
