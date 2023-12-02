package adventofcode;

public class Day2 {
    private final String[] data;
    public Day2(String data) {
        this.data = data.split("\n");
    }
    public void run() {
        int limited = 0;
        int power = 0;
        for (int i = 0; i < this.data.length; i++) {
            String[] line = data[i]
                .split(":")[1]
                .split(";");

            int[] rgb_min = new int[]{0, 0, 0};
            boolean impossible = false;

            for (String game: line) {
                String[] turn = game.split(",");
                for (String cubes: turn) {
                    int n = Integer.parseInt(cubes.split(" ")[1]);

                    if (cubes.endsWith("red")) {
                        if (n > rgb_min[0]) {
                            rgb_min[0] = n;
                        }
                    } else if (cubes.endsWith("green")) {
                        if (n > rgb_min[1]) {
                            rgb_min[1] = n;
                        }
                    } else if (cubes.endsWith("blue")) {
                        if (n > rgb_min[2]) {
                            rgb_min[2] = n;
                        }
                    }
                }
            }
            for (int j = 0; j < rgb_min.length; j++) {
                if (rgb_min[j] > 12 + j) {
                    impossible = true;
                }
            }
            power += rgb_min[0] * rgb_min[1] * rgb_min[2];
            if (!impossible) {
                limited += i + 1;
            }
        }
        System.out.println("Part 1: " + limited);
        System.out.println("Part 2: " + power);
    }
}
