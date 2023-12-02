package adventofcode;

public class Day1 {
    private final String[] data;
    public Day1(String data) {
        this.data = data.split("\n");
    }
    private int processDigits(String line, boolean inverted) {
        String[] digits = new String[]{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        if (inverted) {
            line = new StringBuilder(line).reverse().toString();
            for (int i = 0; i < 9; i++) {
                digits[i] = new StringBuilder(digits[i]).reverse().toString();
            }
        }
        for (int i = 0; i < line.length(); i++) {
            if (Character.isDigit(line.charAt(i))) {
                return line.charAt(i) - '0';
            } else {
                for (int j = 0; j < 9; j++) {
                    if (line.substring(i).startsWith(digits[j])) {
                        return j + 1;
                    }
                }
            }
        }
        throw new RuntimeException("No digit found in line " + line);
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
        for (String line: this.data) {
            int result = processDigits(line, true);
            result += 10 * processDigits(line, false);
            sum += result;
        }
        System.out.println("Part 2: " + sum);
    }
}
