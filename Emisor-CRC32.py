'''
Universidad del Valle de Guatemala
CC3067 - Redes
Laboratorio No. 2 - Esquemas de detección y corrección de errores
Emisor con CRC32
Integrantes:
 - Sebastián Juarez
 - Sebastián Solorzano
'''

import random
import socket

def convertBinary(message):
    return ''.join(format(ord(i), '08b') for i in message)

def crc32(bytes):
    poly = 0xEDB88320
    crc = 0xFFFFFFFF

    for byte in bytes:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1

    return crc ^ 0xFFFFFFFF

def calcular_integridad(binary_message):
    message_bytes = int(binary_message, 2).to_bytes((len(binary_message) + 7) // 8, byteorder='big')
    crc = crc32(message_bytes)
    crc_binary = format(crc, '032b')
    return binary_message + crc_binary

def ruido(binary_message, probabilidad_error=0.01):
    noisy_message = ""
    for bit in binary_message:
        if random.random() < probabilidad_error:
            noisy_message += '0' if bit == '1' else '1'
        else:
            noisy_message += bit
    return noisy_message

def enviar_informacion(mensaje, host='localhost', puerto=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, puerto))
        s.sendall(mensaje.encode())

def main():
    message = input("Ingrese el mensaje a enviar: ")
    message_binary = convertBinary(message)
    message_bytes = calcular_integridad(message_binary)
    message_noisy = ruido(message_bytes)
    enviar_informacion(message_noisy)

    print(f"Mensaje con CRC32: {message_bytes}")
    print(f"Mensaje con ruido: {message_noisy}")

if __name__ == "__main__":
    main()
