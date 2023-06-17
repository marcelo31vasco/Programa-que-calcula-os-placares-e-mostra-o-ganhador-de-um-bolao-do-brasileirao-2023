
"""Versão 0.1.1 Resultados de um bolão do campeonato brasileiro


partidas = [
    "Fortaleza x Bahia",
    "Atletico/PR x Botafogo",
    "Cruzeiro x Atletico/MG",
    "America/MG x Corinthias",
    "Santos x Internacional",
    "Fluminense x Bragantino",
    "Grêmio x São Paulo",
    "Londrina x Sport",
    "Goias x Cuiabá",
    "Palmeiras x Coritiba"
]

placares_reais = []

# Obter os placares reais das partidas
for partida in partidas:
    placar = input(f"Digite o placar real da partida {partida}: ")
    placares_reais.append(placar)

palpites = {
    "Marcelinho": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x0",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "2x0"
    },
    "Diogão": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },
    "Rodrigo Rocha": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "2x2",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "0x0",
        "Palmeiras x Coritiba": "3x1"
    },  
    "Paloma": {
        "Fortaleza x Bahia": "1x2",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "0x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x1"
    },  
    "Djalma": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "0x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },  
      "Chaguinha": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "2x0"
    },  
     "Anselmo": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },  
    "Fela": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "1x2",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },  
    "Lucas": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "1x0",
        "America/MG x Corinthias": "2x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x0"
    },  
     "Lazaro": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "2x1"
    },  
    "Emacio": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x2",
        "Palmeiras x Coritiba": "2x0"
    },  
    "Ronaldo": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "3x0"
    },  
     "Palhaço": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "0x2",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "2x0"
    },  
     "Vascão": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "2x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "2x0"
    },  
     "Edmar": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "1x2",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "2x1"
    }, 
     "Silvano": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "2x2",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x2",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x1"
    },  
     "Meu Berra": {
        "Fortaleza x Bahia": "1x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "4x1"
    },  
     "Japa": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x2",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x0"
    },  
     "Buchudinho": {
        "Fortaleza x Bahia": "1x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "3x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x1"
    },  
     "Igor BV": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x2",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x1"
    },
      "SGT 1": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x0"
    },    
    "SGT 2": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "2x1",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "3x1"
    },    
    "Fogo Jardim": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "2x0"
    },    
    "Jardim Fogo": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "2x1",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },   
    "Valéria": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "0x2",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "0x2",
        "Palmeiras x Coritiba": "3x1"
    },     
      "Lula": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "0x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x2",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x0"
    },  
      "Jesus": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },        
      "Gordinho Moto TAX": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "2x0"
    },        
      "Gabriel": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "2x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x0"
    },    
      "Gabriel 2": {
        "Fortaleza x Bahia": "1x2",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "2x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "2x0"
    },   
      "Romenigue": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x3",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "3x0"
    },  
      "Ticofe": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x2",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x0"
    },       
      "Luiz Fabiano": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x0"
    },  
      "Felipe": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "2x2",
        "America/MG x Corinthias": "1x3",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "0x1",
        "Palmeiras x Coritiba": "2x0"
    },      
      "Almir": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x0",
        "Goias x Cuiabá": "1x2",
        "Palmeiras x Coritiba": "3x0"
    },     
      "Ojuara 31": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "2x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x0"
    }, 
      "Allyn": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "0x1",
        "Palmeiras x Coritiba": "3x0"
    },    
      "Moleque": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "2x2",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "4x1"
    },  
      "Nixon": {
        "Fortaleza x Bahia": "1x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x0",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "2x0"
    },  
      "Dudeca": {
        "Fortaleza x Bahia": "1x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x0",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "1x0"
    },  
      "Dida 1": {
        "Fortaleza x Bahia": "1x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x2",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x1"
    },     
      "Dida 2": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },                
      "Selmo 2": {
        "Fortaleza x Bahia": "1x1",
        "Atletico/PR x Botafogo": "0x1",
        "Cruzeiro x Atletico/MG": "0x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "2x0"
    },     
      "Acassio": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x2",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "3x0",
        "Palmeiras x Coritiba": "4x0"
    },   
      "Neta": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x2",
        "Cruzeiro x Atletico/MG": "0x2",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "3x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "2x0",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x1"
    },                               
      "Assis Chorão": {
        "Fortaleza x Bahia": "3x0",
        "Atletico/PR x Botafogo": "2x0",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "2x0",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "3x1",
        "Londrina x Sport": "1x3",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "4x0"
    },        
      "Rafael Xavier": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "2x1",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "0x0",
        "Londrina x Sport": "0x0",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },      
      "Roniel": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x0"
    },       
      "Novo do Bolo 1": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "3x0",
        "Cruzeiro x Atletico/MG": "0x2",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "0x1",
        "Grêmio x São Paulo": "3x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "3x1",
        "Palmeiras x Coritiba": "3x0"
    },  
      "Novo do Bolo 2": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "0x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "3x1"
    },       
      "Novinho  Preto": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "2x0",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "4x2",
        "Londrina x Sport": "1x3",
        "Goias x Cuiabá": "4x1",
        "Palmeiras x Coritiba": "3x0"
    },    
      "Rodrigo BB": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "0x0",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "3x0"
    },   
      "Diego": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "0x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "0x1",
        "Palmeiras x Coritiba": "3x1"
    },             
      "Yan": {
        "Fortaleza x Bahia": "1x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x0",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },   
      "Januncio": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x0",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "3x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "4x0"
    },    
      "Luciano": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "0x1",
        "Cruzeiro x Atletico/MG": "0x0",
        "America/MG x Corinthias": "0x2",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "0x3",
        "Grêmio x São Paulo": "0x1",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "4x0"
    },      
      "Dedé 1": {
        "Fortaleza x Bahia": "1x1",
        "Atletico/PR x Botafogo": "0x2",
        "Cruzeiro x Atletico/MG": "0x2",
        "America/MG x Corinthias": "1x3",
        "Santos x Internacional": "0x2",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "2x1",
        "Goias x Cuiabá": "0x1",
        "Palmeiras x Coritiba": "3x0"
    },      
      "Dedé 2": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "3x1",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "2x0",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "4x0"
    },
    "Mário": {
        "Fortaleza x Bahia": "1x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "0x2",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },
    "Petinha": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "0x2",
        "Fluminense x Bragantino": "3x0",
        "Grêmio x São Paulo": "3x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "3x0"
    },
    "Nenzão 1": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },
    "Nenzão 2": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "2x0",
        "America/MG x Corinthias": "0x0",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "1x2",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },
    "Higor Esporte": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x0"
    },
    "Naldo Naja": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "1x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },
     "Edmar Motorista": {
        "Fortaleza x Bahia": "3x0",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "0x0",
        "America/MG x Corinthias": "1x3",
        "Santos x Internacional": "2x0",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "4x0"
    },
    "Nanin": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "2x2",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x0",
        "Londrina x Sport": "2x1",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x0"
    },
    "Jacinto Severo": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x1"
    },
    "Narinha": {
        "Fortaleza x Bahia": "3x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "1x1",
        "Santos x Internacional": "0x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "4x0"
    },
    "Marcelo": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "1x2",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "1x1",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "2x1",
        "Palmeiras x Coritiba": "4x0"
    },
    "Paulo Nunes": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "2x0",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x2",
        "Santos x Internacional": "2x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "2x1",
        "Londrina x Sport": "1x1",
        "Goias x Cuiabá": "1x0",
        "Palmeiras x Coritiba": "3x1"
    },
    "Wilson": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "2x0",
        "Cruzeiro x Atletico/MG": "3x1",
        "America/MG x Corinthias": "2x0",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x1",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "0x0",
        "Palmeiras x Coritiba": "3x0"
    },
    "Nem Melo 1": {
        "Fortaleza x Bahia": "2x1",
        "Atletico/PR x Botafogo": "1x1",
        "Cruzeiro x Atletico/MG": "2x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "2x1",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "0x2",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "3x1"
    },
    "Nem melo 2": {
        "Fortaleza x Bahia": "2x0",
        "Atletico/PR x Botafogo": "0x1",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "1x0",
        "Santos x Internacional": "1x1",
        "Fluminense x Bragantino": "2x0",
        "Grêmio x São Paulo": "1x2",
        "Londrina x Sport": "1x2",
        "Goias x Cuiabá": "1x1",
        "Palmeiras x Coritiba": "2x0"
    },
    "Selmo 1": {
        "Fortaleza x Bahia": "1x0",
        "Atletico/PR x Botafogo": "1x0",
        "Cruzeiro x Atletico/MG": "1x1",
        "America/MG x Corinthias": "0x1",
        "Santos x Internacional": "0x0",
        "Fluminense x Bragantino": "1x0",
        "Grêmio x São Paulo": "1x0",
        "Londrina x Sport": "0x1",
        "Goias x Cuiabá": "2x0",
        "Palmeiras x Coritiba": "2x0"
    }
}

def calcular_pontuacao(placar_real, placar_palpite):
    pontos = 0
    if placar_real == placar_palpite:
        pontos = 5
    elif placar_real.split('x')[0] > placar_real.split('x')[1] and placar_palpite.split('x')[0] > placar_palpite.split('x')[1]:
        pontos = 3
    elif placar_real.split('x')[0] < placar_real.split('x')[1] and placar_palpite.split('x')[0] < placar_palpite.split('x')[1]:
        pontos = 3
    elif placar_real.split('x')[0] == placar_real.split('x')[1] and placar_palpite.split('x')[0] == placar_palpite.split('x')[1]:
        pontos = 3
    return pontos

classificacao = {}

for palpite, palpites_usuario in palpites.items():
    pontos_total = 0
    print("\n")
    print(f"\nPalpites de {palpite}:")
    for partida, placar_palpite in palpites_usuario.items():
        print(f"{partida} / {placar_palpite}", end=" ")
        placar_real = placares_reais[partidas.index(partida)]
        pontos = calcular_pontuacao(placar_real, placar_palpite)
        pontos_total += pontos
    classificacao[palpite] = pontos_total
classificacao_ordenada = sorted(classificacao.items(), key=lambda x: x[1], reverse=True)

print("\n")
print("\nClassificação:")
for posicao, (palpite, pontos) in enumerate(classificacao_ordenada, start=1):
    print(f"{posicao}. {palpite}: {pontos} pontos")
