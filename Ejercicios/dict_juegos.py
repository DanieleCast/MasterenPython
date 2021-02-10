'''Crear una lista con el contenido de ésta tabla y mostrarlo 
en pantalla:
ACCIÓN          AVENTURA            DEPORTES
GTA             Prince of Persia    FIFA 21
COD             Uncharted           MOTO GP 21
PUBG            Crash               PES 21
'''
games = [
    {'Género':'Acción',
     'Juegos':['GTA','COD','PUBG']
    },
    {'Género':'Aventura',
     'Juegos':['Prince of Persia','Uncharted','Crash']
    },
    {'Género':'Deportes',
     'Juegos':['FIFA 21','MOTO GP 21','PES 21']
    }    
]
for genero in games:
    print(f"Los juegos de la categoría {genero['Género']} son:\n")
    for juego in genero['Juegos']:
        print(f"{juego}")
    print("\n")    