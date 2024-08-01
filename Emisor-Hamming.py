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
    mensaje_final = p1 + p2 + bits[0] + p3 + ''.join(bits[1:4]) + p4 + ''.join(bits[4:7])
    return mensaje_final

def aplicar_ruido(mensaje_codificado, probabilidad_error=0.05):
    mensaje_con_ruido = ''
    for bit in mensaje_codificado:
        if random.random() < probabilidad_error:
            bit_alterado = '1' if bit == '0' else '0'
            mensaje_con_ruido += bit_alterado
        else:
            mensaje_con_ruido += bit
    return mensaje_con_ruido

def main():
    host = 'localhost'
    port = 12345
    receptor_port = 12347  # Port for Java Receptor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, port))
        servidor.listen()
        print("Emisor Hamming escuchando en {}:{}".format(host, port))

        while True:
            conn, addr = servidor.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    mensaje = data.decode()
                    mensaje_codificado = codificar_hamming(mensaje)
                    mensaje_con_ruido = aplicar_ruido(mensaje_codificado)

                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_receptor:
                        s_receptor.connect((host, receptor_port))
                        s_receptor.sendall(mensaje_con_ruido.encode())
                        resultado = s_receptor.recv(1024).decode()
                        conn.sendall(resultado.encode())

if __name__ == "__main__":
    main()
