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

        if (posicionError != 0) {
            bits[posicionError - 1] = 1 - bits[posicionError - 1];
            return "Error corregido en la posición: " + posicionError + ". " + extraerMensaje(bits);
        }
        return "No se detectaron errores. " + extraerMensaje(bits);
    }

    public static String extraerMensaje(int[] bits) {
        String binario = "" + bits[2] + bits[4] + bits[5] + bits[6] + bits[8] + bits[9] + bits[10];
        return "Mensaje binario: " + binario + ", Carácter ASCII: " + binarioAAscii(binario);
    }

    public static char binarioAAscii(String binario) {
        int valorDecimal = Integer.parseInt(binario, 2);
        return (char) valorDecimal;
    }

     public static void main(String[] args) {
        int port = 12349;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Receptor Hamming listo y escuchando en el puerto " + port);

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))) {
                     
                    System.out.println("Conexión aceptada desde " + clientSocket.getRemoteSocketAddress());
                    String mensajeCodificado = in.readLine();
                    System.out.println("Mensaje recibido: '" + mensajeCodificado + "'");

                    if (mensajeCodificado == null || mensajeCodificado.length() != 11 || !mensajeCodificado.matches("[01]+")) {
                        System.out.println("Rechazo por formato inválido.");
                    } else {
                        System.out.println("Procesando mensaje...");
                        String resultado = decodificarHamming(mensajeCodificado);
                        String encodedResult = Base64.getEncoder().encodeToString(resultado.getBytes("UTF-8"));
                        
                        // Envío directo al main.py en el puerto 12348
                        try (Socket mainSocket = new Socket("localhost", 12348);
                             PrintWriter out = new PrintWriter(mainSocket.getOutputStream(), true)) {
                            out.println(encodedResult);
                            System.out.println("Resultado codificado y enviado directamente a main.py: " + encodedResult);
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
