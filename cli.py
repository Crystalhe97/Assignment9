from game import Game, Human, Bot

prompt = "Single or Double? " # Prompt the user to choose between Single or Double player mode
player_number = input(prompt)

if player_number == 'Single': # Check the user's input and create a Game instance accordingly
    game = Game(Human(), Bot())
elif player_number == 'Double':
    game = Game(Human(), Human())
else:
    raise ValueError("Only Accept input \"Single\" or \"Double\"!")
game.run()