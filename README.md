# Lab2-Redes
Para esta fase se implementaron dos algoritmos, de los cuales uno debe de ser de corrección de errores y uno de detección de errores. Cada algoritmo debe ser implementado para el emisor y el receptor.

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

## Ejemplos de Entrada y Salida
### CRC-32
- **Entrada:** hola
- **Salida Emisor:** Mensaje con CRC32: 0110100001101111011011000110000101101111101000001111100110001000
- **Salida Receptor:** El mensaje recibido es correcto. Mensaje: hola
