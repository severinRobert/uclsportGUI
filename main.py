import requests
import time
import json

def main():
    start = time.time()
    sport = requests.get('https://sites.uclouvain.be/uclsport/api/v1/sport')
    sport = sport.json()
    e = [print(f'{key}: ') for key in sport[0]]
    lieu = requests.get('https://sites.uclouvain.be/uclsport/api/v1/lieu')
    lieu = lieu.json()
    print()
    e = [print(f'{key}: ') for key in lieu[0]]
    activite = requests.get('https://sites.uclouvain.be/uclsport/api/v1/activite')
    activite = activite.json()
    print()
    e = [print(f'{key}: ') for key in activite[0]]
    seance = requests.get('https://sites.uclouvain.be/uclsport/api/v1/seance')
    seance = seance.json()
    print()
    e = [print(f'{key}: ') for key in seance[0]]
    end = time.time()
    print(f'{end - start} seconds')

if __name__ == '__main__':
    main()
