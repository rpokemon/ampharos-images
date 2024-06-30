# Helper script to validate that all pokemon in pokemon.json are in the pokedex

import json
import pathlib

IMG_DIR = pathlib.Path('img/')

def main():
    with open('pokemon.json') as f:
        pokemon = json.load(f)

    for pokemon in pokemon:
        term = pokemon['term']

        if not (IMG_DIR / f'{term}.png').exists():
            print(f'{term}.png does not exist')



if __name__ == '__main__':
    main()
