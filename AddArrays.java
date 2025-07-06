public class AddArrays {
    public static void main(String[] args) {
        int[] list1 = {3, 3, 4};
        int[] list2 = {4, 2, 2};

        int[] result = new int[list1.length];

        for (int i = 0; i < list1.length; i++) {
            result[i] = list1[i] + list2[i];
        }

        System.out.print("Result: ");
        for (int a : result) {
            System.out.print(a + " ");
        }
    }
}
