'''
Universidad del Valle de Guatemala
CC3067 - Redes
Laboratorio No. 2 - Esquemas de detección y corrección de errores
Main
Integrantes:
 - Sebastián Juarez
 - Sebastián Solorzano
'''

import socket
import base64

def solicitar_mensaje():
    return input("Ingrese el mensaje a enviar: ")

def algoritmo():
    opcion = input("Ingrese el algoritmo a utilizar (1 - Hamming, 2 - CRC32): ")
    while opcion not in ['1', '2']:
        opcion = input("Opción inválida. Ingrese el algoritmo a utilizar (1 - Hamming, 2 - CRC32): ")
    return opcion

def recibir_resultado():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12348))
        s.listen()
        conn, addr = s.accept()
        with conn:
            resultado = conn.recv(1024).decode('utf-8')  # Recibir como UTF-8

            try:
                resultado_decodificado = base64.b64decode(resultado).decode('utf-8')
            except Exception as e:
                resultado_decodificado = resultado

            return resultado_decodificado

def main():
    while True: 
        message = solicitar_mensaje()
        algoritmo_elegido = algoritmo()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_emisor:
            if algoritmo_elegido == '1':
                s_emisor.connect(('localhost', 12345))
                s_emisor.sendall(message.encode())
            else:
                s_emisor.connect(('localhost', 12346))
                s_emisor.sendall(message.encode())

        resultado = recibir_resultado()
        print(f"Resultado recibido: {resultado}")

        continuar = input("¿Desea enviar otro mensaje? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
