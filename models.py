


class Pokemon:
    def __init__(self, name, pokemon_id, hp, attack, sprite_url, pokemon_type):
        self.name = name
        self.id = pokemon_id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.type = pokemon_type

    
    def info(self):
        print(f'{self.name} (ID: {self.id})')
        print(f'-- HP: {self.hp}')
        print(f'-- Attack: {self.attack}')
        print(f'-- Type: {self.type}')
        print(f'-- Sprite: {self.sprite_url}')


class Player:
    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_pokemon(self, pokemon):
        if len(self.collection) < 6:
            self.collection.append(pokemon)
            print(f"{pokemon.name} added to {self.name}'s collection!")
            return True

        else:
            print(f"Collection is full! Can't add {pokemon.name}")
            return False
            
    def remove_pokemon(self, index):
        if index < 0 or index >= len(self.collection) or index > 5:
            return None
        removed = self.collection.pop(index)
        print(f'Released {removed.name} from the collection.')
        return removed
    
    def show_collection(self):
        if not self.collection:
            print(f"{self.name}'s Pokemon collection is empty.")
            return
        print(f"{self.name}'s Pokemon Collection: ")
        for i, p in enumerate(self.collection, start = 1):
            print(f'-- {i}. {p.name} (ID: {p.id}) - {p.type} type')
            