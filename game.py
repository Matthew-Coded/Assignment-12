import random
from poke_api import get_pokemon_data
from models import Pokemon


class PokemonGame:
    def __init__(self,player):
        self.player = player
        self.wild_pokemon = None

    def go_hunting(self):
        print('\nYou go hunting for Pokemon!\n')

        random_id = random.randint(1, 151)
        data = get_pokemon_data(random_id)

        if not data:
            print("Couldn't find a wild pokemon right now. Go hunting again!")
            return
        
        self.wild_pokemon = Pokemon(
            data['name'],
            data['id'],
            data['hp'],
            data['attack'],
            data['sprite_url'],
            data['type']
        )

        print(f'A wild {self.wild_pokemon.name} appeared!')
        self.wild_pokemon.info()
        print('\n1. Try to catch.')
        print('2. Flee')

        choice = input('\nWhat do you want to do? ').strip()
        if choice == '1':
            self.try_catch_pokemon()

        elif choice == '2':
            print(f'You fled from {self.wild_pokemon.name}.\n')
            self.wild_pokemon = None

        else:
            print('Invalid choice. Wild pokemon fled the scene!')

    def try_catch_pokemon(self):
        if not self.wild_pokemon:
            print('There is no pokemon to catch right now.')
            input("\nPress Enter to return to the menu...")
            return
        
        catch_rate = 0.25
        print('\nYou throw a pokeball...')
        print(f'Catch rate: {catch_rate * 100:.1f}%')

        roll = random.random()
        if roll <= catch_rate:
            added = self.player.add_pokemon(self.wild_pokemon)
            if added:
                print(f"Caught 'em! {self.wild_pokemon.name} was caught!")

            else:
                print("Your collection is full! The pokemon ran away!")

            self.wild_pokemon = None

        else:
            print(f"Oh no! {self.wild_pokemon.name} broke free!")
            again = input("Try again? (y/n): ").strip().lower()
            if again.startswith("y"):
                return self.try_catch_pokemon()
            else:
                print(f"{self.wild_pokemon.name} ran away...")
                self.wild_pokemon = None


    def remove_pokemon_menu(self):
        print('\n=== Your Collection ===')
        self.player.show_collection()

        choice = input('\nEnter the number of pokemon to remove (or leave blank/press enter to cancel): ').strip()

        if choice == '':
            print('Removal canceled.\n')
            return
        
        try:
            as_int = int(choice)
        except ValueError:
            print('Please enter a valid number.\n')
            return
        
        index = as_int - 1
        removed = self.player.remove_pokemon(index)
        if removed in None:
            print('Invalid choice or number out of range.\n')

        else:
            print(f'You released {removed.name}.')

    def choose_starter(self):
        print("\nHello " + self.player.name + "! Choose your stater pokemon!\n")
        print('Choose your starter pokemon: ')
        print('1. Bulbasuar (Grass type).')
        print('2. Charmander (Fire type).')
        print('3. Squirtle (Water type.)')

        starters = {
            '1': 1,
            '2': 4,
            '3': 7
        }

        while True:
            choice = input('Enter 1, 2, or 3: ').strip()
            if choice in starters:
                data = get_pokemon_data(starters[choice])
                if not data:
                    print('Could not fetch starter. Please try again')
                    continue

                starter = Pokemon(
                    data['name'],
                    data['id'],
                    data['hp'],
                    data['attack'],
                    data['sprite_url'],
                    data['type']
                )
                self.player.add_pokemon(starter)
                print(f'You chose {starter.name}!\n')
                return
            else:
                print("Please enter 1, 2, or 3.")

    def main_menu(self):
        while True:
            print(f'=== Pokemon Adventure - {self.player.name} ===')
            print("1. Go hunting (find wild Pokemon)")
            print("2. View your collection")
            print("3. Remove Pokemon from collection")
            print("4. Quit game")

            choice = input('\nWhat would you like to do? ').strip()
            if choice == '1':
                self.go_hunting()

            elif choice == '2':
                self.player.show_collection()

            elif choice == '3':
                self.remove_pokemon_menu()

            elif choice == '4':
                print('Thanks for playing!')

            else:
                print('Invalid option. Choose 1-4.\n')