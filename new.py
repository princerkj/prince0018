import random
class Cricket_Game:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.teamA_wins = 0
        self.teamB_wins = 0

    def _stimulate_matches(self):

        winner = random.choice([self.teamA, self.teamB])
        if winner == self.teamA:
            self.teamA_wins += 1
        else:
            self.teamB_wins += 1
        return winner

    def _stimulate_series(self, num_matches):

        for _ in range(num_matches):
            self._stimulate_matches()

        if self.teamA_wins > self.teamB_wins:
            return {
                'winner': self.teamA,
                'matches_won': self.teamA_wins
            }

        elif self.teamA_wins < self.teamB_wins:
            return {
                'winner': self.teamB,
                'matches_won': self.teamB_wins
            }

        else:
            return {
                'winner': "Draw",
                'matches_won': None
            }


def get_series_winner(num_matches):
    game = Cricket_Game("TeamA", "TeamB")
    result = game._stimulate_series(num_matches)
    return result


print(f"Enter the number of matches played :")
num_matches = int(input())



series_result = get_series_winner(num_matches)
#print(series_winner: {series_winner['winner']})
#print(matches_won: {series_winner['matches_won']})
print(f"series_winner: {series_result['winner']}")
print(f"matches_won: {series_result['matches_won']}")
