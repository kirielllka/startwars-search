import requests

class Searching:
    def __init__(self):
        self.api = 'https://swapi.dev/api/'

    def personages(self,name:str):
        people = requests.get(self.api+f'people/?search={name}').json()['results'][0]
        films = ', '.join([requests.get(i).json()['title'] for i in people['films']])
        return f'Name:{people['name']}\nGender:{people['gender']}\nHair color:{people['hair_color']}\nFilms:{films}\nHome:{(requests.get(people['homeworld']).json())['name']}\n\n'

    def planet(self,name:str)->str:
        planet = requests.get(self.api+f'planets/?search={name}').json()['results'][0]
        residents = ', '.join([requests.get(i).json()['name'] for i in planet['residents']])
        films = ', '.join([requests.get(i).json()['title'] for i in planet['films']])
        return f'Name:{planet['name']}\nClimate:{planet['climate']}\nPopulation:{planet['population']}\nResidents:{residents}\nFilms:{films}\n\n'

    def film(self,name:int)->str:
        film = requests.get(self.api+f'films/?search={name}').json()['results'][0]
        characters = ', '.join([requests.get(i).json()['name'] for i in film['characters']])
        planets = ', '.join([requests.get(i).json()['name'] for i in film['planets']])
        return f'Title:{film['title']}\nDirector:{film['director']}\nDate:{film['release_date']}\nEpisode:{film['episode_id']}\nPlanets:{planets}\nCharacters:{characters}\n\n{film['opening_crawl']}\n\n'

