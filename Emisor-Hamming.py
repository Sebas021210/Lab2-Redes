# Formula para el calculo de los bits de pariedad
def Pariedad(bits, posiciones):
    conteo = 0
    for pos in posiciones:
        if (pos - 1) < len(bits) and bits[pos - 1] == '1':
            conteo += 1
    return '0' if conteo % 2 == 0 else '1'

# Funcion para codificar el mensaje
def codificar_hamming(mensaje):
    # Asegurar que el mensaje tenga exactamente 7 bits
    mensaje = mensaje.zfill(7)
    
    # Lista de bits
    bits = list(mensaje)
    
    # Calcular los bits de paridad
    p1 = Pariedad(bits, [1, 2, 4, 5, 7])
    p2 = Pariedad(bits, [1, 3, 4, 6, 7])
    p3 = Pariedad(bits, [2, 3, 4])
    p4 = Pariedad(bits, [5, 6, 7])
    
    # Se insertan los bits de paridad
    mensaje_final = p1 + p2 + bits[0] + p3 + ''.join(bits[1:4]) + p4 + ''.join(bits[4:7])
    return mensaje_final

binario = input("Ingrese el mensaje en binario (7 bits): ")
codificado = codificar_hamming(binario)
print("Mensaje codificado:", codificado)
