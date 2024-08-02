import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Base64;

public class ReceptorHamming {

    public static int calcularParidad(int[] bits, int[] posiciones) {
        int conteo = 0;
        for (int pos : posiciones) {
            if (pos - 1 < bits.length && bits[pos - 1] == 1) {
                conteo++;
            }
        }
        return conteo % 2;
    }

    public static String decodificarHamming(String mensajeCodificado) {
        int[] bits = mensajeCodificado.chars().map(c -> c - '0').toArray();
        System.out.println("Decodificando el mensaje: " + mensajeCodificado);
    
        int[] posicionesP1 = {1, 3, 5, 7, 9, 11};
        int[] posicionesP2 = {2, 3, 6, 7, 10, 11};
        int[] posicionesP3 = {4, 5, 6, 7};
        int[] posicionesP4 = {8, 9, 10, 11};
    
        int p1 = calcularParidad(bits, posicionesP1);
        int p2 = calcularParidad(bits, posicionesP2);
        int p3 = calcularParidad(bits, posicionesP3);
        int p4 = calcularParidad(bits, posicionesP4);
    
        int posicionError = p1 * 1 + p2 * 2 + p3 * 4 + p4 * 8;
    
        
        if (posicionError != 0 && posicionError <= 11) {
            bits[posicionError - 1] = 1 - bits[posicionError - 1]; 
            return "Error corregido en la posicion: " + posicionError + ". " + extraerMensaje(bits);
        }
        return "No se detectaron errores. " + extraerMensaje(bits);
    }

    public static String extraerMensaje(int[] bits) {
        String binario = "" + bits[2] + bits[4] + bits[5] + bits[6] + bits[8] + bits[9] + bits[10];
        char asciiChar = binarioAAscii(binario);
        return asciiChar + " [" + binario + "]";
    }

    public static char binarioAAscii(String binario) {
        int valorDecimal = Integer.parseInt(binario, 2);
        return (char) valorDecimal;
    }

    public static void main(String[] args) {
        int port = 12349;
        StringBuilder messageBuilder = new StringBuilder();

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Receptor Hamming listo y escuchando en el puerto " + port);

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))) {
                     
                    System.out.println("Conexión aceptada desde " + clientSocket.getRemoteSocketAddress());
                    String allData = in.readLine();
                    if (allData != null) {
                        for (int i = 0; i + 11 <= allData.length(); i += 11) {
                            String segment = allData.substring(i, i + 11);
                            System.out.println("Segmento recibido: '" + segment + "'");
                            if (!segment.matches("[01]{11}")) {
                                System.out.println("Segmento inválido.");
                                continue;
                            }
                            String resultado = decodificarHamming(segment);
                            messageBuilder.append(resultado).append(" ");
                        }

                        String finalMessage = messageBuilder.toString();
                        messageBuilder.setLength(0);
                        System.out.println("Palabra completa decodificada: " + finalMessage);

                        String encodedMessage = Base64.getEncoder().encodeToString(finalMessage.getBytes("UTF-8"));
                        try (Socket mainSocket = new Socket("localhost", 12348);
                             PrintWriter out = new PrintWriter(mainSocket.getOutputStream(), true)) {
                            out.println(encodedMessage);
                            System.out.println("Palabra completa en Base64 enviada a main.py: " + encodedMessage);
                        }
                    }
                } catch (IOException e) {
                    System.out.println("Error en la conexión con el cliente: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println("No se pudo abrir el puerto " + port);
            e.printStackTrace();
        }
    }
}
