import json
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_resultados(filepath='resultados.json'):
    with open(filepath, 'r') as f:
        return json.load(f)

def analizar_resultados(resultados):
    exitos = sum(1 for r in resultados if "correcto" in r['resultado'])
    errores = len(resultados) - exitos
    tasa_exito = exitos / len(resultados)
    
    print(f"Total de mensajes: {len(resultados)}")
    print(f"Mensajes correctos: {exitos}")
    print(f"Mensajes con errores: {errores}")
    print(f"Tasa de éxito: {tasa_exito:.2%}")

    return tasa_exito, errores

def graficar_resultados(resultados):
    longitudes = [r['longitud'] for r in resultados]
    exitos = ["Correcto" if "correcto" in r['resultado'] else "Error" for r in resultados]
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=longitudes, kde=True, bins=30)
    plt.title('Distribución de Longitudes de Mensajes')
    plt.xlabel('Longitud del Mensaje')
    plt.ylabel('Frecuencia')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(x=exitos)
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
