/*
* Universidad del Valle de Guatemala
* CC3067 - Redes
* Laboratorio No. 2 - Esquemas de detección y corrección de errores
* Receptor con CRC32
* Integrantes:
* - Sebastián Juarez
* - Sebastián Solorzano
*/

import java.util.Scanner;

public class CRC32 {
    private static final int POLY = 0xEDB88320;
    private static final int CRC = 0xFFFFFFFF;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("\nIngrese el mensaje recibido con CRC-32: ");
        String messageReceived = sc.nextLine();
        sc.close();

        String message = messageReceived.substring(0, messageReceived.length() - 32);
        String crc = messageReceived.substring(messageReceived.length() - 32);
        byte[] messageBytes = new byte[message.length() / 8];
        
        for (int i = 0; i < message.length(); i += 8) {
            messageBytes[i / 8] = (byte) Integer.parseInt(message.substring(i, i + 8), 2);
        }

        int calculatedCRC = crc32(messageBytes);

        if (calculatedCRC == Integer.parseUnsignedInt(crc, 2)) {
            System.out.println("El mensaje recibido es correcto. Mensaje: " + binaryToText(message));
        } else {
            System.out.println("El mensaje recibido es incorrecto: Se detectaron errores.");
        }
    }

    private static int crc32(byte[] bytes) {
        int crc = CRC;
        for (byte b : bytes) {
            crc ^= b & 0xFF;
            for (int i = 0; i < 8; i++) {
                if ((crc & 1) != 0) {
                    crc = (crc >>> 1) ^ POLY;
                } else {
                    crc = crc >>> 1;
                }
            }
        }
        return crc ^ CRC;
    }

    private static String binaryToText(String binary) {
        StringBuilder text = new StringBuilder();
        for (int i = 0; i < binary.length(); i += 8) {
            int charCode = Integer.parseInt(binary.substring(i, i + 8), 2);
            text.append((char) charCode);
        }
        return text.toString();
    }
    
}
