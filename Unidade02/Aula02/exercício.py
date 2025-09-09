import numPy as np

participantes = [
    {
        'nome': 'Bruno',
        'localizacao': 'Brasil',
        'afiliacao':'Ampli',
        'interesses': ['Python', 'C#']
    },
    {
        'nome': 'Jurandir',
        'localizacao': 'Brasil',
        'afiliacao':'Ampli',
        'interesses': ['Javascript', 'C#']
    },
    {
        'nome': 'Claudineia',
        'localizacao': 'Colômbia',
        'afiliacao':'Ampli',
        'interesses': ['Python', 'Rust']
    },
    {
        'nome': 'Cearina',
        'localizacao': 'Brasil',
        'afiliacao':'Ampli',
        'interesses': ['Javascript', 'C++']
    },
    {
        'nome': 'Tostella',
        'localizacao': 'Brasil',
        'afiliacao':'Ampli',
        'interesses': ['React', 'C#']
    },
]

# Usando NumPy para analisar áreas de interesse

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante['interesses']])

interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)

area_mais_popular = interesses_unicos[np.argmax(contagem)]

print(f'Área de interesse mais popular: {area_mais_popular}')