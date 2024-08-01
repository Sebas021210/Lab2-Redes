/*
* Universidad del Valle de Guatemala
* CC3067 - Redes
* Laboratorio No. 2 - Esquemas de detección y corrección de errores
* Receptor con CRC32
* Integrantes:
* - Sebastián Juarez
* - Sebastián Solorzano
*/

import java.io.*;
import java.net.*;

public class CRC32 {
    private static final int POLY = 0xEDB88320;
    private static final int CRC = 0xFFFFFFFF;

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            System.out.println("\nEsperando conexión...");
            Socket socket = serverSocket.accept();
            System.out.println("Conexión establecida.");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String noisyMessage = in.readLine();
            
            String message = noisyMessage.substring(0, noisyMessage.length() - 32);
            String crc = noisyMessage.substring(noisyMessage.length() - 32);
            byte[] messageBytes = new byte[message.length() / 8];
            
            for (int i = 0; i < message.length(); i += 8) {
                messageBytes[i / 8] = (byte) Integer.parseInt(message.substring(i, i + 8), 2);
            }

            int calculatedCRC = calcularCRC32(messageBytes);

            if (calculatedCRC == Integer.parseUnsignedInt(crc, 2)) {
                String decodedMessage = decodificarMensaje(message);
                mostrarMensaje(decodedMessage);
            } else {
                System.out.println("El mensaje recibido es incorrecto: Se detectaron errores.");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int calcularCRC32(byte[] bytes) {
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

    private static String decodificarMensaje(String binaryMessage) {
        StringBuilder text = new StringBuilder();
        for (int i = 0; i < binaryMessage.length(); i += 8) {
            int charCode = Integer.parseInt(binaryMessage.substring(i, i + 8), 2);
            text.append((char) charCode);
        }
        return text.toString();
    }

    private static void mostrarMensaje(String mensaje) {
        System.out.println("Mensaje recibido: " + mensaje);
    }
}
