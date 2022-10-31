from data import Data
import time
import json

def main():
    
    start = time.time()
    sport = Data('https://sites.uclouvain.be/uclsport/api/v1/sport')
    print(e[0]['_resid'])
    lieu = Data('https://sites.uclouvain.be/uclsport/api/v1/lieu')
    print()
    e = [print(f'{key}: ') for key in lieu[0]]
    activite = Data('https://sites.uclouvain.be/uclsport/api/v1/activite')
    print()
    e = [print(f'{key}: ') for key in activite[0]]
    seance = Data('https://sites.uclouvain.be/uclsport/api/v1/seance')
    print()
    e = [print(f'{key}: ') for key in seance[0]]
    end = time.time()
    print(f'{end - start} seconds')

if __name__ == '__main__':
    main()
