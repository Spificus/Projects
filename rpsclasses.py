from numpy import random

class scoreBoard():
    def __init__(self,pscore,cscore,draws):
       self.pscore = pscore
       self.cscore = cscore
       self.draws = draws

    def inPscore(self):
        self.pscore += 1

    def inCscore(self):
        self.cscore += 1

    def inDraws(self):
        self.draws += 1

class game():
    def __init__(self):
        self.scoreBoard = scoreBoard(0,0,0)

    def compare(self, pchoice, compchoice):
        if compchoice == pchoice:
            print("computer: " + compchoice + "     Player: " + pchoice + "\n \n draw \n")
            self.scoreBoard.inDraws()
        elif compchoice == "rock" and pchoice == "scissors":
            print("computer: " + compchoice + "     Player: " + pchoice + "\n \n Computer wins \n")
            self.scoreBoard.inCscore()
        elif compchoice == "paper" and pchoice == "rock":
            print("computer: " + compchoice + "     Player: " + pchoice + "\n \n Computer wins \n")
            self.scoreBoard.inCscore()
        elif compchoice == "scissors" and pchoice == "paper":
            print("computer: " + compchoice + "     Player: " + pchoice + "\n \n Computer wins \n")
            self.scoreBoard.inCscore()
        elif compchoice == "scissors" and pchoice == "rock":
            print("computer: " + compchoice + "     Player: " + pchoice + "\n \n You win \n")
            self.scoreBoard.inPscore()
        elif compchoice == "rock" and pchoice == "paper":
            print("computer: " + compchoice + "     Player: " + pchoice + "\n \n You win \n")
            self.scoreBoard.inPscore()
        elif compchoice == "paper" and pchoice == "scissors":
            print("computer: " + compchoice + "      Player: " + pchoice + "\n \n You win \n")
            self.scoreBoard.inPscore()

    def play(self):
        options = ["rock", "paper", "scissors"]
        compchoice = random.choice(options)
        selection = input("Select 1 for rock, 2 for paper, 3 for scissors and 4 to quit \n \n")
        try:
            if 4 > int(selection) > 0: 
                pchoice = options[int(selection) - 1]
                self.compare(pchoice, compchoice)
                return True
            elif int(selection) == 4:
                print ("Game ended")
                print(f"Player score: {self.scoreBoard.pscore}")
                print(f"Computer score: {self.scoreBoard.cscore}")
                print(f"Draws: {self.scoreBoard.draws}")
                return False
            else:
                print("Invalid entry")
                return True

        except:
            print("Invalid entry")
            return True

    



def main():
    p = game()
    while p.play():
        pass
if __name__ == "__main__":
    main()