# Planificador de Instalación de Sistemas Operativos
Este script en Python ayuda a los administradores de sistemas a evaluar de forma automatizada y rápida si un equipo informático cumple con los requisitos de hardware necesarios para albergar una instalación o migración de un nuevo sistema operativo.

## Requisitos del Sistema
El script requiere Python 3.x y el uso de la biblioteca de control de hardware `psutil`.

## Librerías Utilizadas
* **`psutil`**: Utilizada de forma obligatoria para realizar llamadas al sistema y extraer datos de hardware en tiempo real (RAM total, núcleos de CPU y espacio libre en disco).
* **`os`**: Manejo interno de rutas de archivos de salida.

## Instalación de dependencias
Para instalar la librería externa debes ejecutar el siguiente comando en la terminal:
```bash
pip install psutil