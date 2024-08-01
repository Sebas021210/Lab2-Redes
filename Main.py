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

def solicitar_mensaje():
    return input("Ingrese el mensaje a enviar: ")

def recibir_resultado():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12348))
        s.listen()
        conn, addr = s.accept()
        with conn:
            resultado = conn.recv(1024).decode()
            return resultado

def main():
    message = solicitar_mensaje()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_emisor:
        s_emisor.connect(('localhost', 12346))
        s_emisor.sendall(message.encode())
    
    resultado = recibir_resultado()
    print(f"Resultado recibido: {resultado}")

if __name__ == "__main__":
    main()
