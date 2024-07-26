# Lab2-Redes
Para esta fase se implementaron dos algoritmos, de los cuales uno debe de ser de corrección de errores y uno de detección de errores. Cada algoritmo debe ser implementado para el emisor y el receptor.

## Uso
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
### Hamming
- **Entrada:** 0100001
- **Salida Emisor:** Mensaje codificado: 10011001001
- **Salida Receptor:** No se detectaron errores. Mensaje original: Mensaje binario: 1100001, Caracter ASCII: a
