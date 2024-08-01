# Lab2-Redes
Para esta fase se implementaron dos algoritmos, de los cuales uno debe de ser de corrección de errores y uno de detección de errores. Cada algoritmo debe ser implementado para el emisor y el receptor.

## Autores
- Sebastián Juarez
- Sebastián Solorzano

## Branch: Corrección de errores
Para la implementación del algoritmo de corrección de errores, se utilizó el código de Hamming, donde el emisor fue desarrollado en Python y el receptor en Java. Esta elección permitió no solo detectar sino también corregir errores de un solo bit en la transmisión de datos. En Python, se generaron los bits de paridad y se añadió la redundancia necesaria al mensaje original. En Java, se implementó la lógica para verificar y corregir errores, asegurando que los datos recibidos sean consistentes y precisos.

## Branch: Detección de errores
Para la implementación del algoritmo de detección de errores, se utilizó CRC-32, donde el emisor fue desarrollado en Python y el receptor en Java. Esta elección permitió aprovechar la eficiencia de CRC-32 en la detección de errores durante la transmisión de datos. Python se utilizó para calcular el CRC-32 y adjuntar el valor al mensaje original, mientras que Java se utilizó para verificar la integridad del mensaje recibido.

## Uso
### Arquitectura de capas
1. Ejecutar los receptores en Java:
    ```bash
    java CRC32
    ```
    ```bash
    java ReceptorHamming
    ```
2. Ejecutar los emisores en Python:
    ```bash
    python Emisor-CRC32.py
    ```
    ```bash
    python Emisor-Hamming.py
    ```
3. Ejecutar Main:
   ```bash
   python Main.py
   ```
5. Proporcionar el mensaje en texto a enviar cuando se solicite.
6. Seleccionar el algoritmo a utilizar.

### Pruebas
1. Ejecutar el receptor para la prueba en Java:
    ```bash
    java CRC32
    ```
    ```bash
    java Emisor-Hamming
    ```
2. Ejecutar el receptor para la prueba en Python:
    ```bash
    python Emisor-CRC32.py
    ```
    ```bash
    python Emisor-Hamming.py
    ```
3. Ejecutar Prueba:
   ```bash
   python Prueba.py
   ```

### Análisis
1. Asegurarse de tener el archivo .json creado después de la prueba
2. Ejecutar Análisis
   ```bash
   python Analisis.py
   ```

## Ejemplos de Entrada y Salida
- **Entrada:** hola
- **Salida:** El mensaje recibido es correcto. Mensaje: hola
