import os
import psutil

# Diccionario con requisitos mínimos reales de sistemas operativos. RAM se muestra en GB, Disco se muestra en GB
REQUISITOS_SO = {
    "Ubuntu 24.04 LTS": {
        "ram_minima": 4.0,
        "disco_minimo": 25.0,
        "cpu_nucleos": 2
    },
    "Debian 13": {
        "ram_minima": 4.0,
        "disco_minimo": 25.0,
        "cpu_nucleos": 2
    },
    "Windows 11": {
        "ram_minima": 4.0,
        "disco_minimo": 64.0,
        "cpu_nucleos": 2
    }
}

#Escanea automáticamente el equipo y con psutil se convierten los valores de bytes a Gigabytes (GB).
def obtener_recursos_equipo():
    # RAM Total
    ram_total_gb = psutil.virtual_memory().total / (1024 ** 3)
    
    # Espacio libre en disco (en la partición principal)
    disco_libre_gb = psutil.disk_usage('/').free / (1024 ** 3)
    
    # Núcleos lógicos de la CPU
    cpu_nucleos = psutil.cpu_count()
    
    return {
        "ram": round(ram_total_gb, 2),  # Redondeamos a 2 decimales.
        "disco_libre": round(disco_libre_gb, 2),  # Redondeamos a 2 decimales.
        "cpu_nucleos": cpu_nucleos if cpu_nucleos else 1  # En caso de que psutil no pueda detectar el número de núcleos, se asume 1 núcleo como mínimo.
    }

#Función para la generación del informe.
def generar_informe(so_activo, recursos_equipo):
    #Compara los recursos disponibles frente a los requisitos mínimos y genera un informe detallado por pantalla y en archivo TXT.
    requisitos = REQUISITOS_SO[so_activo]
    
    # Variables booleanas para evaluar cada requisito de RAM, Disco y CPU.
    cumple_ram = recursos_equipo["ram"] >= requisitos["ram_minima"]
    cumple_disco = recursos_equipo["disco_libre"] >= requisitos["disco_minimo"]
    cumple_cpu = recursos_equipo["cpu_nucleos"] >= requisitos["cpu_nucleos"]
    
    # Si las tres variables son True, entonces la instalación es viable.
    viable = cumple_ram and cumple_disco and cumple_cpu
    
    # Escribimos tanto los requisitos que se cumplen como los que no, y al final hay una conclusión clara sobre la instalación.
    informe = []
    informe.append("==================================================")
    informe.append("   INFORME DE VIABILIDAD DE INSTALACIÓN DE SO     ")
    informe.append("==================================================")
    informe.append(f"Sistema Operativo a evaluar: {so_activo}\n")
    
    informe.append("1. RECURSOS DETECTADOS EN EL EQUIPO:")
    informe.append(f"   - Memoria RAM Total: {recursos_equipo['ram']} GB")
    informe.append(f"   - Espacio en Disco Libre: {recursos_equipo['disco_libre']} GB")
    informe.append(f"   - Núcleos de CPU: {recursos_equipo['cpu_nucleos']}\n")
    
    informe.append("2. REQUISITOS MÍNIMOS DEL SISTEMA OPERATIVO:")
    informe.append(f"   - Memoria RAM requerida: {requisitos['ram_minima']} GB")
    informe.append(f"   - Espacio en Disco requerido: {requisitos['disco_minimo']} GB")
    informe.append(f"   - Núcleos de CPU requeridos: {requisitos['cpu_nucleos']}\n")
    
    informe.append("3. EVALUACIÓN DE REQUISITOS:")
    informe.append(f"   - [ {'OK' if cumple_ram else 'X'} ] Memoria RAM")
    informe.append(f"   - [ {'OK' if cumple_disco else 'X'} ] Espacio en Disco")
    informe.append(f"   - [ {'OK' if cumple_cpu else 'X'} ] Núcleos de CPU\n")
    
    # Si la instalación fuera o no viable, lo indicaría.
    informe.append("--------------------------------------------------")
    if viable:
        informe.append("CONCLUSIÓN: LA INSTALACIÓN ES VIABLE ✅")
        informe.append("El equipo cumple o supera todos los requisitos mínimos.")
    else:
        informe.append("CONCLUSIÓN: LA INSTALACIÓN NO ES VIABLE ❌")
        informe.append("El equipo NO cumple con algunos de los requisitos mínimos.")
    informe.append("==================================================")
    
    # Convertir lista (variable informe) a formato texto (variable texto_informe).
    texto_informe = "\n".join(informe)
    
    # Imprimir por pantalla el informe completo.
    print(texto_informe)
    
    # Guardar en un archivo TXT (Ampliación opcional).
    nombre_archivo = f"informe_{so_activo.replace(' ', '_').lower()}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(texto_informe)
    print(f"\n[INFO] Informe guardado con éxito en: {nombre_archivo}")

    # Función inicial encargada de interactuar con el usuario por consola.
def ejecutar_planificador():
    print("--- PLANIFICADOR DE INSTALACIÓN DE SISTEMAS OPERATIVOS ---")
    print("Seleccione el Sistema Operativo que desea evaluar:")
    
    # Se muestran todos los sistemas operativos disponibles en el diccionario.
    opciones = list(REQUISITOS_SO.keys())
    for i, so in enumerate(opciones, start=1):
        print(f"{i}. {so}")
        
    # Manejo de error para entrada no válida.
    try:
        seleccion = int(input("\nIntroduzca el número de su opción: "))
        if 1 <= seleccion <= len(opciones):
            so_elegido = opciones[seleccion - 1]
            print("\nAnalizando el hardware del sistema actual...\n")
            
            # Obtenemos los recursos de nuestro equipo y los comparamos con los requisitos del SO elegido. Luego, se genera el informe detallado.
            recursos = obtener_recursos_equipo()
            generar_informe(so_elegido, recursos)
            
        else:
            print("[ERROR] Opción inválida. Por favor, ejecute el programa de nuevo.")
    except ValueError:
        print("[ERROR] Debe introducir un número entero válido.")

# Inicio del programa.
ejecutar_planificador()