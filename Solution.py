import numpy as np


class Cricket:

    def __init__(self, runs, overs):
        self.runs = runs
        self.overs = overs
    # Function to change the strike

    def changestrike(self, playing):
        return playing[::-1]

    # Function to generate a random number based on given probabilities
    def random_runs(self, probs, playing):
        return np.random.choice(np.arange(8), p=probs[playing[0]])

    def print_ball(self, over, ball, player, score):
        if score == 1:
            print(str(over) + "." + str(ball + 1) + " " +
                  str(player) + " scores " + str(score) + " run")
        else:
            print(str(over) + "." + str(ball + 1) + " " +
                  str(player) + " scores " + str(score) + " runs")

    def start(self):
        # DECLARATIONS

        # Number of overs
        overs = self.overs
        # Number of runs
        runs = self.runs
        # Number of wickets gone. Used as flag to check if all players are out
        wickets = 0
        # Number of balls in an over
        balls = 6
        # List of players
        players = ["Kirat Boli", "NS Nodhi", "R Rumrah", "Shashi Henra"]
        # List of remaining players (Since 1st two are on field)
        remaining = players[2:]
        # Scores for players, with an out flag
        # If the player hasn't been on the field yet, their scores will not be present here
        scores = {players[0]: {"Score": 0, "Balls": 0, "Out": False},
                  players[1]: {"Score": 0, "Balls": 0, "Out": False}}
        # Storing the probabilities of 0,1,2,3,4,5,6 and out in a dictionary
        # for the given players
        probs = {players[0]: [0.05, 0.30, 0.25, 0.10, 0.15, 0.01, 0.09, 0.05],
                 players[1]: [0.10, 0.40, 0.20, 0.05, 0.10, 0.01, 0.04, 0.10],
                 players[2]: [0.20, 0.30, 0.15, 0.05, 0.05, 0.01, 0.04, 0.20],
                 players[3]: [0.30, 0.25, 0.05, 0.00, 0.05, 0.01, 0.04, 0.30]}
        # Current players (1st and 2nd on the field)
        playing = [players[wickets], players[wickets + 1]]

        for over in range(overs):
            print()
            print(str(overs - over) + " overs left. " +
                  str(runs) + " runs to win")
            print()
            for ball in range(balls):
                # Using numpy to get random values between 0 and 7
                # p are the probability values, used to select random values
                randno = self.random_runs(probs, playing)
                # Increasing balls played for the player on strike
                scores[playing[0]]["Balls"] += 1
                # randno being 7 means out
                if randno != 7:
                    # Reducing number of runs remaining
                    runs = runs - randno
                    # Increasing the score of the player
                    scores[playing[0]]["Score"] += randno
                    # Print the score for that ball
                    self.print_ball(over, ball, playing[0], randno)
                    # If the no. of runs is odd then change strike
                    if randno % 2 != 0:
                        playing = self.changestrike(playing)
                    else:
                        pass
                    # More than given runs made, Lengaburu wins
                    if runs <= 0:
                        print()
                        print("Lengaburu won by " + str(3 - wickets) + " wickets and " +
                              str(((overs - 1 - over) * 6) +
                                  (5 - ball)) + " balls remaining")
                        self.print_scores(scores)
                        return
                else:
                    # If randno is 7 and the player is out
                    wickets += 1
                    # Set the player status to Out
                    scores[playing[0]]['Out'] = True
                    print(str(over) + "." + str(ball) +
                          " " + str(playing[0]) + " Out!")
                    # If all players are out, Lengaburu lost
                    if wickets == 3:
                        print()
                        print("Lengaburu lost by " + str(runs) + " runs")
                        self.print_scores(scores)
                        return
                    else:
                        # Put the next player on strike
                        playing = [remaining[0], playing[1]]
                        scores[remaining[0]] = {
                            "Score": 0, "Balls": 0, "Out": False}
                        # Remove onstrike player from remaining players list
                        remaining.remove(remaining[0])
            # At the end of an over, change strike
            playing = self.changestrike(playing)
        print()
        # If all balls are over and the score is 0 then the game is tied
        if runs == 0:
            print("Match tied!")
        # If runs scored are less than 40 and balls are over
        else:
            print("Lengaburu lost by " + str(runs) + " runs")
        self.print_scores(scores)
        return

    # FUNCTION TO PRINT THE SCORES FOR ALL THE PLAYERS WHO PLAYED ON FIELD

    def print_scores(self, scores):
        print()
        print("-----------------")
        print("SCOREBOARD")
        print("-----------------")
        for player in scores:
            # If player was not out then we need to add a "*" after the score
            if scores[player]["Out"] is False:
                print(player + " - " + str(scores[player]["Score"]) +
                      "* (" + str(scores[player]["Balls"]) + " balls)")
            else:
                print(player + " - " + str(scores[player]["Score"]) +
                      " (" + str(scores[player]["Balls"]) + " balls)")


# Main Function, number of runs to win and number of overs left can be changed
if __name__ == "__main__":
    match1 = Cricket(40, 4)
    match1.start()
