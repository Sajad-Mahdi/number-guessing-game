from random import randint

class GuessingGame:
    def __init__(self, secret_number):
        self.secret_number = secret_number
        self.guesses = []
        self.has_won = False
        self.number_diff = []

    def guess(self, number):
        self.guesses.append(number)
        self.number_diff.append(abs(number - self.secret_number))
        if number > self.secret_number:
            print("Lower")
        elif number < self.secret_number:
            print("Higher")
        else:
            self.has_won = True
            print("Congratulations! You guessed correctly!")

    def show_guesses(self):
        print("Your guesses were : ")
        for y in self.guesses:
            print(y, end=" , ")
        print()
        closest_index = self.number_diff.index(min(self.number_diff))
        farthest_index = self.number_diff.index(max(self.number_diff))
        print("Your closest guess was:", self.guesses[closest_index])
        print("Your farthest guess was:", self.guesses[farthest_index])


class LimitedGuessingGame (GuessingGame) :
	def __init__ (self , secret_number , max_guesses = 5 ) :
		super().__init__(secret_number)
		self.max_guesses = max_guesses
		self.game_over = False

	def guess(self, number) :
	       self.guesses.append(number)
	       if len(self.guesses) >= self.max_guesses :
	       	print(f"Game Over , The number was {self.secret_number}")
	       	self.game_over  = True
	       	return
	       self.number_diff.append(abs(number - self.secret_number))
	       if number > self.secret_number : print("Lower")
	       elif number < self.secret_number : print("Higher")
	       else :
	              self.has_won = True
	              print("Congratulations! You guessed correctly!")
            
def get_guess():
    while True :
        try:
            return int(input("What is the secret number? "))
        except ValueError:
            print("Please input a valid integer.")
 
def play_again():
    while True:
        decision = input("Play again (yes or no)? ")
        if decision == "yes":
            return True
        elif decision == "no":
            return False
        else:
            print("Invalid input")

while True:
    game = LimitedGuessingGame(randint(1, 100))
    while not game.has_won and not game.game_over :
        inserted_number = get_guess()
        game.guess(inserted_number)
    game.show_guesses()
    if not play_again():
        break
