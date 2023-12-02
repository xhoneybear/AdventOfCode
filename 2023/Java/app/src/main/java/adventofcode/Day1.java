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
        for (String line: this.data) {
            String[] digits = new String[]{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
            StringBuilder sb = new StringBuilder();
            StringBuilder buffer = new StringBuilder();
            for (int i = 0; i < line.length(); i++) {
                boolean clear = true;
                if (Character.isDigit(line.charAt(i))) {
                    sb.append(line.charAt(i));
                } else {
                    buffer.append(line.charAt(i));
                    for (int j = 0; j < 9; j++) {
                        if (digits[j].equals(buffer.toString())) {
                            sb.append(j + 1);
                            buffer = new StringBuilder();
                            clear = false;
                            break;
                        } else if (digits[j].startsWith(buffer.toString())) {
                            clear = false;
                        }
                    }
                }
                if (clear) {
                    buffer = new StringBuilder();
                    buffer.append(line.charAt(i));
                }
            }
            String result = sb.toString();
            sum += Integer.parseInt(result.charAt(0) + "" + result.charAt(result.length() - 1));
        }
        System.out.println("Part 2: " + sum);
    }
}
