from models import Player
from game import PokemonGame

def main():
    print("Welcome to Pokemon CLI Adventure!")
    name = input("What's your name, trainer? ").strip() or "Ash"
    player = Player(name)
    game = PokemonGame(player)
    game.choose_starter()
    game.main_menu()

if __name__ == "__main__":
    main()