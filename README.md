# Ejercicio 1 - Planificador de Instalación de Sistemas Operativos
Este proyecto es una herramienta en Python para evaluar si un equipo cumple los requisitos mínimos de hardware para instalar sistemas operativos comunes.

## Descripción general
El programa escanea el hardware del equipo actual, compara los recursos disponibles con los requisitos definidos para varios sistemas operativos y genera un informe de viabilidad.

## Estructura del proyecto
- `main.py`: archivo principal que contiene toda la lógica de evaluación.
- `README.md`: documentación del proyecto.

## Componentes del programa
### 1. Datos de requisitos (`REQUISITOS_SO`)
El diccionario `REQUISITOS_SO` recoge los requisitos mínimos de cada sistema operativo soportado:
- `ram_minima`: memoria RAM en GB.
- `disco_minimo`: espacio libre en disco en GB.
- `cpu_nucleos`: número mínimo de núcleos de CPU.

Actualmente soporta:
- Ubuntu 24.04 LTS
- Debian 13
- Windows 11

### 2. Lectura de recursos del equipo (`obtener_recursos_equipo`)
Esta función usa `psutil` para obtener:
- RAM total disponible.
- Espacio libre en la partición raíz (`/`).
- Número de núcleos lógicos de CPU.

Los valores de RAM y disco se convierten de bytes a gigabytes y se redondean a dos decimales.

### 3. Generación de informe (`generar_informe`)
Esta función compara los recursos detectados con los requisitos del sistema operativo elegido.
- Evalúa cada criterio: RAM, disco y CPU.
- Determina si la instalación es viable sólo si se cumplen los tres requisitos.
- Muestra el resultado en pantalla.
- Guarda un informe de texto en un archivo con nombre `informe_<sistema_operativo>.txt`.

### 4. Interacción con el usuario (`ejecutar_planificador`)
Esta función es la entrada principal del programa:
- Presenta una lista de sistemas operativos disponibles.
- Solicita al usuario que seleccione una opción mediante un número.
- Valida la entrada y ejecuta la evaluación.
- Informa de errores en caso de selección inválida o entrada no numérica.

### 5. Inicio del programa
Al final de `main.py` se invoca directamente:
```python
ejecutar_planificador()
```
Esto inicia el flujo de ejecución al ejecutar `python main.py`.

## Dependencias
- Python 3.x
- `psutil`

Instalación:
```bash
pip install psutil
```

## Uso
Ejecuta el script con:
```bash
python main.py
```

El programa mostrará un menú interactivo y, tras la selección, imprimirá en pantalla un informe de viabilidad.

## Salida
El informe se presenta en dos formatos:
- Consola: resumen de recursos, requisitos, evaluación y conclusión.
- Archivo de texto: `informe_<sistema_operativo>.txt`.

## Detalles adicionales
- La partición analizada para el espacio en disco es la raíz `/`.
- Si `psutil` no logra detectar el número de núcleos de CPU, el programa asume al menos 1 núcleo.
- El módulo `os` está importado en `main.py` y puede utilizarse en el futuro para gestionar rutas o nombres de archivos de forma más completa.

## Extensiones posibles
- Añadir más sistemas operativos y requisitos.
- Soportar evaluación de discos en particiones específicas.
- Incluir comprobación de versión de Python o arquitectura del sistema.
- Añadir una interfaz gráfica o generar HTML en lugar de TXT.
