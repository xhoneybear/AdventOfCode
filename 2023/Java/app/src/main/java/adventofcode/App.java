package adventofcode;

import java.io.File;
import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        System.out.println("Working Directory = " + System.getProperty("user.dir"));
        Scanner input = new Scanner(System.in);
        String run, data;
        System.out.print("Run solution for day: ");
        run = input.nextLine();
        File file = new File("../../input/input_" + run + ".txt");

        try {
            data = new Scanner(file).useDelimiter("\\A").next();
        } catch (Exception e) {
            System.out.println("No input data for day " + run);
            return;
        }

        switch (run) {
            case "1" -> new Day1(data).run();
            case "2" -> new Day2(data).run();
            // case "3" -> new Day3(data).run();
            // case "4" -> new Day4(data).run();
            case "5" -> new Day5(data).run();
            // case "6" -> new Day6(data).run();
            // case "7" -> new Day7(data).run();
            // case "8" -> new Day8(data).run();
            // case "9" -> new Day9(data).run();
            // case "10" -> new Day10(data).run();
            // case "11" -> new Day11(data).run();
            // case "12" -> new Day12(data).run();
            // case "13" -> new Day13(data).run();
            // case "14" -> new Day14(data).run();
            // case "15" -> new Day15(data).run();
            // case "16" -> new Day16(data).run();
            // case "17" -> new Day17(data).run();
            // case "18" -> new Day18(data).run();
            // case "19" -> new Day19(data).run();
            // case "20" -> new Day20(data).run();
            // case "21" -> new Day21(data).run();
            // case "22" -> new Day22(data).run();
            // case "23" -> new Day23(data).run();
            // case "24" -> new Day24(data).run();
            // case "25" -> new Day25(data).run();
            default -> throw new InputMismatchException("No solution for day " + run);
        }
    }
}
