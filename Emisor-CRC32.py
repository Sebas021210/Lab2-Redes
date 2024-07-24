'''
Universidad del Valle de Guatemala
CC3067 - Redes
Laboratorio No. 2 - Esquemas de detección y corrección de errores
Emisor con CRC32

Integrantes:
 - Sebastián Juarez
 - Sebastián Solorzano
'''

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

def main():
    message = input("Ingrese el mensaje a enviar: ")
    message_bytes = int(message, 2).to_bytes((len(message) + 7) // 8, byteorder='big')

    # Calculo del CRC32
    crc = crc32(message_bytes)

    # Mensaje a enviar con CRC32
    crc_binnary = format(crc, '032b')

    print(f"Mensaje original: {message}")
    print(f"CRC32: {crc_binnary}")
    print(f"Mensaje con CRC32: {message + crc_binnary}")

if __name__ == "__main__":
    main()
