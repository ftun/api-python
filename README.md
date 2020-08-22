
Instalar python

- sudo apt update
- sudo apt -y upgrade
- python3 -V
- sudo apt install -y python3-pip
- sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
- sudo apt install -y python3-pip

Intalar paquetes (Una ves corriendo el entorno de desarrollo)

- pip3 install [package_name]

Instalar herremientas desarrollo:

- sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
- sudo apt install -y python3-venv

Crear entorno virtual

- (Posicionarse en el directorio de la aplicacion)
- python3 -m venv my_env
- ls my_env

Correr el entorno de desarrollo:

- source my_env/bin/activate
- deactivate (salir del ambiente)
