import socket
import random

def Pariedad(bits, posiciones):
    conteo = 0
    for pos in posiciones:
        if (pos - 1) < len(bits) and bits[pos - 1] == '1':
            conteo += 1
    return '0' if conteo % 2 == 0 else '1'

def codificar_hamming(mensaje):
    
    mensaje = mensaje.zfill(7)
    bits = list(mensaje)
    p1 = Pariedad(bits, [1, 2, 4, 5, 7])
    p2 = Pariedad(bits, [1, 3, 4, 6, 7])
    p3 = Pariedad(bits, [2, 3, 4])
    p4 = Pariedad(bits, [5, 6, 7])
    return p1 + p2 + bits[0] + p3 + ''.join(bits[1:4]) + p4 + ''.join(bits[4:7])

def aplicar_ruido(mensaje_codificado, probabilidad_error=0.05):
    return ''.join('1' if bit == '0' and random.random() < probabilidad_error else '0' if bit == '1' and random.random() < probabilidad_error else bit for bit in mensaje_codificado)

def texto_a_binario(texto):
    return ''.join(format(ord(c), '07b') for c in texto)

def main():
    host = 'localhost'
    port = 12345
    receptor_port = 12349  # Puerto para el Receptor Java

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, port))
        servidor.listen()
        print(f"Emisor Hamming escuchando en {host}:{port}")

        while True:
            conn, addr = servidor.accept()
            print(f"Conexión aceptada desde {addr}")
            with conn:
                data = conn.recv(1024)
                if not data:
                    print("No se recibieron datos. Cerrando conexión.")
                    break
                mensaje = data.decode('utf-8')
                print(f"Mensaje recibido: {mensaje}")

                mensaje_total_codificado = ''
                for caracter in mensaje:
                    binario = texto_a_binario(caracter)
                    mensaje_codificado = codificar_hamming(binario)
                    mensaje_con_ruido = aplicar_ruido(mensaje_codificado)
                    mensaje_total_codificado += mensaje_con_ruido

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_receptor:
                    s_receptor.connect((host, receptor_port))
                    s_receptor.sendall((mensaje_total_codificado + "\n").encode('utf-8'))

if __name__ == "__main__":
    main()
