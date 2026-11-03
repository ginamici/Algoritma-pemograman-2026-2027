public class Contoh {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        // Operator aritmatika
        System.out.println(a + b);   // 13
        System.out.println(a - b);   // 7
        System.out.println(a * b);   // 30
        System.out.println(a / b);   // 3 (pembagian bulat karena kedua operand int)
        System.out.println(a % b);   // 1

        // Operator perbandingan
        System.out.println(a > b);   // true
        System.out.println(a == b);  // false
        System.out.println(a != b);  // true

        // Operator logika
        System.out.println(a > 5 && b < 5);   // true
        System.out.println(a < 5 || b < 5);   // true
        System.out.println(!(a > b));         // false

        // Operator penugasan dan increment
        a += 5;     // a = 15
        b++;        // b = 4

        // Ekspresi gabungan
        int hasil = (a + b) * 2 - 4;
        System.out.println(hasil);   // 34
    }
}