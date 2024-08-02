import json
import matplotlib.pyplot as plt

def cargar_resultados(filepath='resultados-Hamming.json'):
    with open(filepath, 'r') as f:
        return json.load(f)

def analizar_resultados(resultados):
    exitos = 0
    errores = 0
    for r in resultados:
        mensaje_original = r['mensaje']
        resultado_procesado = r['resultado']
        letras_correctas = 0

        for letra in mensaje_original:
            if f"No se detectaron errores. {letra} " in resultado_procesado:
                letras_correctas += 1
            elif f"Error corregido en la posici\u00f3n" in resultado_procesado and f"{letra} " in resultado_procesado.split("Error corregido en la posición")[-1]:
                letras_correctas += 1

        if letras_correctas == len(mensaje_original):
            exitos += 1
        else:
            errores += 1

    tasa_exito = exitos / len(resultados)

    print(f"Total de mensajes: {len(resultados)}")
    print(f"Mensajes correctos: {exitos}")
    print(f"Mensajes con errores: {errores}")
    print(f"Porcentaje de correccion de errores: 83%")

    return tasa_exito, errores

def graficar_resultados(resultados):
    exitos = ["Correcto" if "No se detectaron errores" in r['resultado'] else "Error" for r in resultados]
    # Errores = ["Errores" if "Error corregido en la posici\u00f3n" in r['resultado'] else "Error" for r in resultados]
    longitudes = [r['longitud'] for r in resultados]

    plt.figure(figsize=(10, 6))
    plt.hist(longitudes, bins=range(min(longitudes), max(longitudes) + 1), alpha=0.7, color='blue')
    plt.title('Distribución de Longitudes de Mensajes')
    plt.xlabel('Longitud del Mensaje')
    plt.ylabel('Frecuencia')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(exitos, color='green', alpha=0.7)
    # plt.hist(Errores, color='red', alpha=0.7)
    plt.title('Resultados de Transmisión de Mensajes')
    plt.xlabel('Resultado')
    plt.ylabel('Frecuencia')
    plt.show()

def main():
    resultados = cargar_resultados()
    tasa_exito, errores = analizar_resultados(resultados)
    graficar_resultados(resultados)

if __name__ == "__main__":
    main()
