package adventofcode;

public class Day1 {
    private final String[] data;
    public Day1(String data) {
        this.data = data.split("\n");
    }
    public void run() {
        int sum = 0;
        for (String line: this.data) {
            line = line.replaceAll("[^0-9]", "");
            if (line.length() != 0) {
                sum += Integer.parseInt(line.charAt(0) + "" + line.charAt(line.length() - 1));
            }
        }
        System.out.println("Part 1: " + sum);

        sum = 0;
        String[] digits = new String[]{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (String line: this.data) {
            String result = "";
            for (int i = 0; i < line.length(); i++) {
                if (Character.isDigit(line.charAt(i))) {
                    result = result + line.charAt(i);
                    continue;
                }
                for (int j = 0; j < digits.length; j++) {
                    if (line.substring(i).startsWith(digits[j])) {
                        result = result + (j + 1);
                        break;
                    }
                }
            }

            if (result.length() != 0) {
                sum += Integer.parseInt(result.charAt(0) + "" + result.charAt(result.length() - 1));
            }
        }
        System.out.println("Part 2: " + sum);
    }
}
