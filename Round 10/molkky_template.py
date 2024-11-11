"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""

class Player:
    def __init__(self, name, points=0, round = 0):
        """Initialize the newly created object"""
        self.__name = name
        self.__points = points
        self.__round = round

    def get_name(self):
        """Get the name of the object which called this function"""
        return self.__name

    def get_points(self):
        """Get the points of the object which called this function"""
        return self.__points

    def add_points(self,points):
        """Add the points to the object points and count the rounds"""
        self.__round += 1
        total_point = self.__points + points
        if total_point> 50:
            print(f"{self.__name} gets penalty points!")
            self.__points = 25
        else:
          self.__points += points
          if total_point >= 40 and self.__points <= 49:
              print(
                  f"{self.__name} needs only {50 - total_point} points. It's better to avoid knocking down the pins with higher points.")

    def has_won(self):
        """if the objects point has exactly 50 then return true for won"""
        if self.__points == 50:
            return True
        else:
            return False

    def average(self,total):
        """Calculate the average - cummulative total divided by number of rounds"""
        average = total/self.__round
        return average

    #total is the list of the points of that particular player
    def hit(self,total):
        """Calculate hit percentage - not zeros/total times. the total is the list of numbers of that player """
        try:
            not_zero = 0
            for number in total:
                if number !=0 :
                    not_zero+=1
            percent = not_zero/len(total)*100
            return percent
        except ZeroDivisionError:
            return 0


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")
    cumulative_score = {}
    cumulative_score[player1.get_name()] = []
    cumulative_score[player2.get_name()] = []
    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)


        cumulative_score[in_turn.get_name()].append(pts)

        if in_turn.average(sum(cumulative_score[in_turn.get_name()]))<pts:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        percent1 = player1.hit(cumulative_score[player1.get_name()])
        percent2 = player2.hit(cumulative_score[player2.get_name()])

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {percent1:.1f}" )  # TODO: d)
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {percent2:.1f}" )
        print("")

        throw += 1


if __name__ == "__main__":
    main()
