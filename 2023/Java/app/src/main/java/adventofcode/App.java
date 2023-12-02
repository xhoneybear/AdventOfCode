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
            System.out.println("Input file for day " + run + " not found");
            return;
        }

        switch (run) {
            case "1" -> new Day1(data).run();
            default -> throw new InputMismatchException("Solution for day " + run + " not found");
        }
    }
}
