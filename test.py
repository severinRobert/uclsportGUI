from data import Data

sport = Data('https://sites.uclouvain.be/uclsport/api/v1/sport')
lieu = Data('https://sites.uclouvain.be/uclsport/api/v1/lieu')
activite = Data('https://sites.uclouvain.be/uclsport/api/v1/activite')
seance = Data('https://sites.uclouvain.be/uclsport/api/v1/seance')

for e in seance.data:
    if e['Activite'] == 'Badminton':
        print(f"{e['Lieu']} - {e['Date']}")
