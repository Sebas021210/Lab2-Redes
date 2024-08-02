import socket
import random
import string
import time
import json
import base64

def generate_random_message(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

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
    pruebas = [10, 100, 1000, 10000]
    resultados = []

    for prueba in pruebas:
        print(f"Realizando prueba con {prueba} mensajes...")

        for i in range(prueba):
            message = generate_random_message(random.randint(1, 10))

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_emisor:
                try:
                    s_emisor.connect(('localhost', 12345))
                    s_emisor.sendall(message.encode())
                except socket.error as e:
                    print(f"Error al conectar con el emisor: {e}")
                    continue

            resultado = recibir_resultado()
            resultados.append({
                'mensaje': message,
                'resultado': resultado,
                'longitud': len(message)
            })
            
            time.sleep(0.01)

        time.sleep(1)

    with open('resultados-Hamming.json', 'w') as f:
        json.dump(resultados, f)

    print("Pruebas completadas y resultados guardados en resultados.json")

if __name__ == "__main__":
    main()
