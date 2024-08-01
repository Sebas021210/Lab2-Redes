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

def ruido(binary_message, probabilidad_error=0.005):
    noisy_message = ""
    for bit in binary_message:
        if random.random() < probabilidad_error:
            noisy_message += '0' if bit == '1' else '1'
        else:
            noisy_message += bit
    return noisy_message

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12346))
        s.listen()
        print("Esperando conexión...")
        while True:
            conn, addr = s.accept()
            with conn:
                message = conn.recv(1024).decode()
                print("Conexión establecida.")
                print(f"\nMensaje recibido: {message}")

                message_binary = convertBinary(message)
                message_with_crc = calcular_integridad(message_binary)
                message_noisy = ruido(message_with_crc)

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_receptor:
                    s_receptor.connect(('localhost', 12347))
                    s_receptor.sendall(message_noisy.encode())
                    print(f"Mensaje CRC32: {message_with_crc}")
                    print(f"Mensaje enviado: {message_noisy}")

if __name__ == "__main__":
    main()
