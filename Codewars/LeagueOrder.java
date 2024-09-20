
import java.util.*;

public class LeagueOrder {

    // Team statistics class to hold points, goals for, and against
    static class TeamStats {

        int points;
        int goalsFor;
        int goalsAgainst;

        public TeamStats() {
            this.points = 0;
            this.goalsFor = 0;
            this.goalsAgainst = 0;
        }

        // Goal difference
        public int goalDifference() {
            return goalsFor - goalsAgainst;
        }
    }

    public static int[] computeRanks(int number, int[][] games) {
        // Initialize team statistics
        Map<Integer, TeamStats> teams = new HashMap<>();
        for (int i = 0; i < number; i++) {
            teams.put(i, new TeamStats());
        }

        // Process each game
        for (int[] game : games) {
            int teamA = game[0];
            int teamB = game[1];
            int goalsA = game[2];
            int goalsB = game[3];

            TeamStats statsA = teams.get(teamA);
            TeamStats statsB = teams.get(teamB);

            // Update goals for and against
            statsA.goalsFor += goalsA;
            statsA.goalsAgainst += goalsB;
            statsB.goalsFor += goalsB;
            statsB.goalsAgainst += goalsA;

            // Update points
            if (goalsA > goalsB) {  // Team A wins
                statsA.points += 2;
            } else if (goalsA < goalsB) {  // Team B wins
                statsB.points += 2;
            } else {  // Draw
                statsA.points += 1;
                statsB.points += 1;
            }
        }

        // Create a list of teams and their statistics
        List<int[]> teamStats = new ArrayList<>();
        for (int i = 0; i < number; i++) {
            TeamStats stats = teams.get(i);
            teamStats.add(new int[]{i, stats.points, stats.goalDifference(), stats.goalsFor});
        }

        // Sort the teams by points, goal difference, and goals scored
        teamStats.sort((a, b) -> {
            if (b[1] != a[1]) {
                return Integer.compare(b[1], a[1]);
            }
            if (b[2] != a[2]) {
                return Integer.compare(b[2], a[2]);
            }
            return Integer.compare(b[3], a[3]);
        });

        // Initialize positions
        int[] positions = new int[number];

        // Handle ties and head-to-head comparisons
        int i = 0;
        while (i < teamStats.size()) {
            int j = i;

            // Find the group of tied teams
            while (j < teamStats.size() && Arrays.equals(Arrays.copyOfRange(teamStats.get(i), 1, 4),
                    Arrays.copyOfRange(teamStats.get(j), 1, 4))) {
                j++;
            }

            if (j - i > 1) {
                // There's a tie, apply head-to-head comparison
                List<Integer> tiedTeams = new ArrayList<>();
                for (int k = i; k < j; k++) {
                    tiedTeams.add(teamStats.get(k)[0]);
                }

                // Head-to-head stats
                Map<Integer, TeamStats> headToHeadStats = new HashMap<>();
                for (int team : tiedTeams) {
                    headToHeadStats.put(team, new TeamStats());
                }

                // Calculate head-to-head stats for tied teams
                for (int[] game : games) {
                    int teamA = game[0];
                    int teamB = game[1];
                    int goalsA = game[2];
                    int goalsB = game[3];

                    if (tiedTeams.contains(teamA) && tiedTeams.contains(teamB)) {
                        TeamStats statsA = headToHeadStats.get(teamA);
                        TeamStats statsB = headToHeadStats.get(teamB);

                        statsA.goalsFor += goalsA;
                        statsA.goalsAgainst += goalsB;
                        statsB.goalsFor += goalsB;
                        statsB.goalsAgainst += goalsA;

                        if (goalsA > goalsB) {
                            statsA.points += 2;
                        } else if (goalsA < goalsB) {
                            statsB.points += 2;
                        } else {
                            statsA.points += 1;
                            statsB.points += 1;
                        }
                    }
                }

                // Prepare list of tied teams with head-to-head stats
                List<int[]> tiedTeamStats = new ArrayList<>();
                for (int team : tiedTeams) {
                    TeamStats stats = headToHeadStats.get(team);
                    tiedTeamStats.add(new int[]{team, stats.points, stats.goalDifference(), stats.goalsFor});
                }

                // Sort based on head-to-head comparison
                tiedTeamStats.sort((a, b) -> {
                    if (b[1] != a[1]) {
                        return Integer.compare(b[1], a[1]);  // Compare points

                    }
                    if (b[2] != a[2]) {
                        return Integer.compare(b[2], a[2]);  // Compare goal difference

                    }
                    return Integer.compare(b[3], a[3]);                    // Compare goals scored
                });

                // Assign positions based on head-to-head
                for (int k = 0; k < tiedTeamStats.size(); k++) {
                    positions[tiedTeamStats.get(k)[0]] = i + k + 1;
                }
            } else {
                // No tie, assign the position directly
                positions[teamStats.get(i)[0]] = i + 1;
            }

            i = j;
        }

        return positions;
    }
}
