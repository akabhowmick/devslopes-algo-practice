
import java.util.*;

public class LeagueOrder {

    public static int[] computeRanks(int number, int[][] games) {
        List<Team> teams = new ArrayList<>();
        for (int id = 0; id < number; id++) {
            teams.add(new Team(id));
        }
        for (int[] game : games) {
            Team home = teams.get(game[0]);
            Team visi = teams.get(game[1]);
            Result homeResult = home.getResults().get(visi.getId());
            if (homeResult == null) {
                homeResult = new Result();
                home.getResults().put(visi.getId(), homeResult);
            }
            homeResult.takeGame(game[2], game[3]);
            Result visiResult = visi.getResults().get(home.getId());
            if (visiResult == null) {
                visiResult = new Result();
                visi.getResults().put(home.getId(), visiResult);
            }
            visiResult.takeGame(game[3], game[2]);
        }
        int[] result = new int[number];
        translateGroup(teams, 1, result);
        return result;
    }

    public static void translateGroup(List<Team> teams, int index, int[] result) {
        if (teams.size() == 1) {
            result[teams.get(0).getId()] = index;
            return;
        }
        Set<Integer> ids = new HashSet<>();
        for (Team team : teams) {
            ids.add(team.getId());
        }
        for (Team team : teams) {
            team.calculateGlobalResult(ids);
        }
        Collections.sort(teams);
        Map<Integer, List<Team>> groups = new HashMap<>();
        int idx = index;
        List<Team> group = new ArrayList<>();
        group.add(teams.get(0));
        for (int i = 1; i < teams.size(); i++) {
            if (teams.get(i).compareTo(teams.get(i - 1)) == 0) {
                group.add(teams.get(i));
            } else {
                groups.put(idx, new ArrayList<>(group));
                group = new ArrayList<>();
                group.add(teams.get(i));
                idx = index + i;
            }
        }
        if (!group.isEmpty()) {
            groups.put(idx, group);
        }
        if (groups.size() == 1) {
            List<Team> same = groups.get(idx);
            for (Team team : same) {
                result[team.getId()] = idx;
            }
            return;
        }
        for (Map.Entry<Integer, List<Team>> entry : groups.entrySet()) {
            translateGroup(entry.getValue(), entry.getKey(), result);
        }
    }

}

class Team implements Comparable<Team> {

    private final int id;
    private final Map<Integer, Result> results = new HashMap<>();
    private Result globalResult = null;

    Team(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public Map<Integer, Result> getResults() {
        return results;
    }

    public void calculateGlobalResult(Set<Integer> ids) {
        globalResult = new Result();
        for (Map.Entry<Integer, Result> entry : results.entrySet()) {
            if (ids.contains(entry.getKey())) {
                globalResult.mergeResult(entry.getValue());
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append(id).append("x");
        result.append(globalResult);
        return result.toString();
    }

    @Override
    public int compareTo(Team o) {
        return globalResult.compareTo(o.globalResult);
    }
}

class Result implements Comparable<Result> {

    private int pts;
    private int gs;
    private int gc;

    Result() {
    }

    public void takeGame(int gs, int gc) {
        this.gs += gs;
        this.gc += gc;
        if (gs > gc) {
            pts += 2;
        }
        if (gs == gc) {
            pts += 1;
        }
    }

    public void mergeResult(Result result) {
        pts += result.pts;
        gs += result.gs;
        gc += result.gc;
    }

    @Override
    public String toString() {
        return pts + ":" + gs + "-" + gc;
    }

    @Override
    public int compareTo(Result o) {
        if (pts > o.pts) {
            return -1;
        }
        if (pts < o.pts) {
            return 1;
        }
        int diff1 = gs - gc;
        int diff2 = o.gs - o.gc;
        if (diff1 > diff2) {
            return -1;
        }
        if (diff1 < diff2) {
            return 1;
        }
        if (gs > o.gs) {
            return -1;
        }
        if (gs < o.gs) {
            return 1;
        }
        return 0;
    }
}
