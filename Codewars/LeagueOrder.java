
import java.util.*;

public class LeagueOrder {

    // Team class to store the stats of each team
    static class Team {

        int id;         // Team ID
        int points;     // Total points
        int goalsFor;   // Goals scored
        int goalsAgainst; // Goals conceded
        int goalDifference; // Goal differential
        int matchesPlayed; // Track if the team has played any match

        public Team(int id) {
            this.id = id;
            this.points = 0;
            this.goalsFor = 0;
            this.goalsAgainst = 0;
            this.goalDifference = 0;
            this.matchesPlayed = 0;
        }

        // Method to update the stats based on the result of a match
        public void updateStats(int goalsFor, int goalsAgainst) {
            this.goalsFor += goalsFor;
            this.goalsAgainst += goalsAgainst;
            this.goalDifference = this.goalsFor - this.goalsAgainst;
            this.matchesPlayed++;  // Team has played a match

            if (goalsFor > goalsAgainst) {
                this.points += 2; // 2 points for a win
            } else if (goalsFor == goalsAgainst) {
                this.points += 1; // 1 point each for a draw
            }
            // No points for a loss
        }

        // Method to check if teams are tied by main criteria
        public boolean isTied(Team other) {
            return this.points == other.points
                    && this.goalDifference == other.goalDifference
                    && this.goalsFor == other.goalsFor;
        }

        @Override
        public String toString() {
            return "Team " + id + ": Points=" + points + ", GD=" + goalDifference + ", GF=" + goalsFor + ", Played=" + matchesPlayed;
        }
    }

    // Comparator to sort teams based on criteria
    static Comparator<Team> teamComparator = (Team a, Team b) -> {
        // First criteria: Points
        if (b.points != a.points) {
            return b.points - a.points;
        }
        // Second criteria: Goal difference
        if (b.goalDifference != a.goalDifference) {
            return b.goalDifference - a.goalDifference;
        }
        // Third criteria: Goals scored
        if (b.goalsFor != a.goalsFor) {
            return b.goalsFor - a.goalsFor;
        }
        // Otherwise, return 0 for equality
        return 0;
    };

    // Main method to compute ranks
    public static int[] computeRanks(int number, int[][] games) {
        Team[] teams = new Team[number];
        for (int i = 0; i < number; i++) {
            teams[i] = new Team(i);
        }

        // Process all games
        for (int[] game : games) {
            int teamA = game[0];
            int teamB = game[1];
            int goalsA = game[2];
            int goalsB = game[3];

            // Update stats for both teams
            teams[teamA].updateStats(goalsA, goalsB);
            teams[teamB].updateStats(goalsB, goalsA);
        }

        // Sort teams based on points, goal difference, and goals scored
        Arrays.sort(teams, teamComparator);

        // Handle teams with no matches separately
        handleNoMatches(teams);

        // Create the result array based on sorted teams
        int[] result = new int[number];
        for (int i = 0; i < number; i++) {
            result[teams[i].id] = i + 1; // Rank is the index + 1
        }

        return result;
    }

    // Function to handle ties using head-to-head comparisons
    private static void resolveTies(Team[] teams, int[][] games) {
        int n = teams.length;
        List<Team> tieGroup = new ArrayList<>();
        for (int i = 0; i < n;) {
            tieGroup.clear();
            tieGroup.add(teams[i]);

            // Group teams that are tied
            int j = i + 1;
            while (j < n && teams[i].isTied(teams[j])) {
                tieGroup.add(teams[j]);
                j++;
            }

            // If there is more than one team tied, apply head-to-head
            if (tieGroup.size() > 1) {
                List<Team> sortedTieGroup = breakTieByHeadToHead(tieGroup, games);
                for (int k = 0; k < sortedTieGroup.size(); k++) {
                    teams[i + k] = sortedTieGroup.get(k);
                }
            }

            i = j; // Move to the next group of teams
        }
    }

    // Handle teams that have not played any matches
    private static void handleNoMatches(Team[] teams) {
        int currentRank = 1;
        for (int i = 0; i < teams.length; i++) {
            if (teams[i].matchesPlayed == 0) {
                teams[i].points = Integer.MIN_VALUE;  // Ensure unplayed teams rank at the bottom
            } else {
                currentRank = i + 1;  // Keep track of the correct rank
            }
        }

        // Now assign proper rank to the unplayed teams
        for (Team team : teams) {
            if (team.matchesPlayed == 0) {
                team.points = currentRank;
            }
        }
    }

    // Function to handle head-to-head tie-breaking for tied teams
    private static List<Team> breakTieByHeadToHead(List<Team> tieGroup, int[][] games) {
        // Map team id to head-to-head stats (points, goalsFor, goalsAgainst)
        Map<Integer, Team> h2hStats = new HashMap<>();
        for (Team team : tieGroup) {
            h2hStats.put(team.id, new Team(team.id));
        }

        // Process only games between tied teams
        for (int[] game : games) {
            if (h2hStats.containsKey(game[0]) && h2hStats.containsKey(game[1])) {
                int teamA = game[0];
                int teamB = game[1];
                int goalsA = game[2];
                int goalsB = game[3];

                h2hStats.get(teamA).updateStats(goalsA, goalsB);
                h2hStats.get(teamB).updateStats(goalsB, goalsA);
            }
        }

        // Create a list of teams with head-to-head stats and sort them
        List<Team> sortedTieGroup = new ArrayList<>(tieGroup.size());
        for (Team team : tieGroup) {
            sortedTieGroup.add(h2hStats.get(team.id));
        }

        // Sort using the same comparator
        sortedTieGroup.sort(teamComparator);

        return sortedTieGroup;
    }

}
