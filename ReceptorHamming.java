import java.util.Scanner;

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
            return "Error corregido en la posición: " + posicionError + ". Mensaje corregido: " + extraerMensaje(bits);
        }
        return "No se detectaron errores. Mensaje original: " + extraerMensaje(bits);
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
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese un caracter codificado de 11 bits: ");
        String mensajeCodificado = scanner.nextLine();
        scanner.close();
        
        
        if (mensajeCodificado.length() != 11 || !mensajeCodificado.matches("[01]+")) {
            System.out.println("Error: El mensaje debe ser de 11 bits.");
        } else {
            System.out.println(decodificarHamming(mensajeCodificado));
        }
    }
}
