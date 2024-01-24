package adventofcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Day5 {
    private final long[] seeds;
    private final ArrayList<ArrayList<long[]>> maps = new ArrayList<>();

    public Day5(String data) {
        String[] dataArr = data.split("\n");
        this.seeds = Arrays.stream(
            dataArr[0]
            .split(": ")[1]
            .split(" ")
            ).mapToLong(Long::parseLong)
            .toArray();
        int i = -1;
        for (String line: dataArr) {
            if (line.isEmpty());
            else if (line.charAt(0) >= '0' && line.charAt(0) <= '9') {
                this.maps.get(i).add(Arrays.stream(line.split(" ")).mapToLong(Long::parseLong).toArray());
            } else {
                this.maps.add(new ArrayList<>());
                i++;
            }
        }
    }

    private long locate(long seed, boolean reverse) {
        ArrayList<ArrayList<long[]>> maps = new ArrayList<>();
        for (ArrayList<long[]> map: this.maps) {
            maps.add(new ArrayList<>(map));
        }
        if (reverse) {
            Collections.reverse(maps);
        }
        for (ArrayList<long[]> map: maps) {
            for (long[] submap: map) {
                if (reverse) {
                    submap = new long[]{submap[1], submap[0], submap[2]};
                }
                if (seed >= submap[1] && seed < submap[1] + submap[2]) {
                    seed += submap[0] - submap[1];
                    break;
                }
            }
        }
        return seed;
    }

    private long findRanged(long start, long end, long step) {
        if (step == 0) {
            return end;
        }
        for (long loc = start; loc <= end; loc += step) {
            for (int s = 0; s < this.seeds.length; s += 2) {
                if (locate(loc, true) >= this.seeds[s] && locate(loc, true) < this.seeds[s] + this.seeds[s + 1]) {
                    return findRanged(loc - step, loc, step / 10);
                }
            }
        }
        throw new RuntimeException("No solution found");
    }

    public void run() {
        long single = Integer.MAX_VALUE;
        for (long seed: this.seeds) {
            seed = locate(seed, false);
            single = Math.min(single, seed);
        }
        long ranged = findRanged(0, this.seeds[0] + this.seeds[1], (long) Math.pow(10, 7));
        System.out.println("Part 1: " + single);
        System.out.println("Part 2: " + ranged);
    }
}
