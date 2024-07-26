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
### Emisor y Receptor CRC-32
1. Ejecutar el emisor en Python:
    ```bash
    python Emisor-CRC32.py
    ```
2. Proporcionar el mensaje en texto a enviar cuando se solicite.
3. Ejecutar el receptor en Java:
    ```bash
    java CRC32
    ```
4. Ingresar el mensaje recibido con CRC-32 cuando se solicite.

### Emisor y Receptor Hamming
1. Ejecutar el emisor en Python:
    ```bash
    python Emisor-Hamming.py
    ```
2. Proporcionar el mensaje en binario a enviar cuando se solicite.
3. Ejecutar el receptor en Java:
    ```bash
    java ReceptorHamming
    ```
4. Ingresar el mensaje recibido cuando se solicite.

## Ejemplos de Entrada y Salida
### CRC-32
- **Entrada:** hola
- **Salida Emisor:** Mensaje con CRC32: 0110100001101111011011000110000101101111101000001111100110001000
- **Salida Receptor:** El mensaje recibido es correcto. Mensaje: hola
### Hamming
- **Entrada:** 0100001
- **Salida Emisor:** Mensaje codificado: 10011001001
- **Salida Receptor:** No se detectaron errores. Mensaje original: Mensaje binario: 1100001, Caracter ASCII: a

