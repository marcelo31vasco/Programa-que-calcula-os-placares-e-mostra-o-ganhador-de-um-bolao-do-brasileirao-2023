Versão 2.0 - Acrencentei uma divisão para primeiros colocados e a classificação geral abaixo.


partidas = [
"Atletico/MG x Bahia",
"America/MG x Goias",
"Corinthians x Coritiba",
"Grêmio x Fluminense",
"Guarani x Juventude",
"Vitoria x Ceara",
"Flamengo x São Paulo",
"Fortaleza x Santos",
"Palmeiras x Cruzeiro",
"Bragantino x Vasco"

  
]

placares_reais = []

# Aqui irei inserir os placares reais das partidas
for partida in partidas:
    placar = input(f"Digite o placar real da partida {partida}: ")
    placares_reais.append(placar)

palpites = {
       "Bruno": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"1x2",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "0x2"
       }  ,
        "Lula": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"0x2",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "2x0"
       },
      "Narinha": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"3x0",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"0x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "0x1"    
      },
         "Gordinho": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x0"    
      },
         "Fela": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "1x0"    
      },
         "Marcelinho": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x0",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "1x2"    
      },
         "Rodrigo BB": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"0x0",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"3x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "3x0"    
      },
         "Diego": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x0",
"Fortaleza x Santos":"1x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x0"    
      },
         "Nixon": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"1x0",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "1x0"
      },
         "Emarcio": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"1x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "1x0"    
      },
         "Paulo Nunes": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"2x0",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "2x0"    
      },
         "Vascão": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"1x0",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "1x2"    
      },
         "Edmar": {

"Atletico/MG x Bahia":"3x1",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "1x1"    
      },
         "Bolsonaro": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Bolsonaro 2": {

"Atletico/MG x Bahia":"3x1",
"America/MG x Goias":"3x1",
"Corinthians x Coritiba":"3x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"3x1",
"Fortaleza x Santos":"3x1",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "3x1"    
      },
         "Rafael Xavier": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"0x1",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"3x0",
"Bragantino x Vasco": "3x1"    
      },
         "Deca": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"3x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"0x1",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "1x2"    
      },
         "Thales": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"1x2",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "2x0"    
      },
         "Palhaço": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"1x2",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "2x0"    
      },
         "Palhaço": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"0x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"0x0",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "3x1"    
      },
         "Araujo 31": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x2",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Almir": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"0x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"0x0",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "1x2"    
      },
         "Novo do Bolo": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"2x0",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Novo do Bolo 2": {

"Atletico/MG x Bahia":"3x1",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"3x1",
"Guarani x Juventude":"0x1",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "3x0"    
      },
         "Roniel": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"3x1",
"Grêmio x Fluminense":"1x0",
"Guarani x Juventude":"0x1",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"0x0",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "1x2"    
      },
         "Ticofe": {

"Atletico/MG x Bahia":"3x0",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "3x0"    
      },
         "Edmar Motorista": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"0x1",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x3",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "1x1"    
      },
         "Mario": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"3x0",
"Bragantino x Vasco": "0x1"    
      },
         "Jacinto": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Nem Melo": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"0x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"1x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "1x2"    
      },
         "Selmo": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"0x1",
"Guarani x Juventude":"0x1",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"0x1",
"Palmeiras x Cruzeiro":"1x0",
"Bragantino x Vasco": "0x1"    
      },
         "Selmo 2": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"0x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x0",
"Fortaleza x Santos":"0x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "0x1"    
      },
         "Fabiano Caico": {

"Atletico/MG x Bahia":"0x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"0x2",
"Grêmio x Fluminense":"0x0",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"0x0",
"Palmeiras x Cruzeiro":"0x1",
"Bragantino x Vasco": "2x1"    
      },
         "Rodrigo Roca": {

"Atletico/MG x Bahia":"3x2",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x2",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"2x3",
"Vitoria x Ceara":"1x2",
"Flamengo x São Paulo":"3x2",
"Fortaleza x Santos":"1x2",
"Palmeiras x Cruzeiro":"2x3",
"Bragantino x Vasco": "1x2"    
      },
         "Fogo Jardim": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Jardim Fogo": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"3x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "3x0"    
      },
         "Marcelo": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"3x0",
"Bragantino x Vasco": "3x0"    
      },
         "Valeria": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"0x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "2x1"    
      },
         "Heron": {

"Atletico/MG x Bahia":"3x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x2",
"Fortaleza x Santos":"1x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "1x2"    
      },
         "Assis Chorão": {

"Atletico/MG x Bahia":"3x0",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"0x1",
"Fortaleza x Santos":"3x1",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "3x1"    
      },
         "Paloma": {

"Atletico/MG x Bahia":"1x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"1x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"1x2",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x2"    
      },
         "Mica": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"0x1",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Silvano": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"1x0",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "1x1"    
      },
         "Meu Berra": {

"Atletico/MG x Bahia":"1x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"0x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"4x1",
"Bragantino x Vasco": "0x1"    
      },
         "Chagas PM": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"3x1",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "2x0"    
      },
         "Djalma": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "2x1"    
      },
         "Lazaro": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"0x2",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x0"    
      },
         "Luciano Chorão": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"2x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"2x2",
"Guarani x Juventude":"0x2",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"0x2",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "0x1"    
      },
         "Chico Roque": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x2",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "2x1"    
      },
         "Nino": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"0x1",
"Vitoria x Ceara":"0x2",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "0x1"    
      },
         "Nino 2": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"3x1",
"Corinthians x Coritiba":"1x1",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"1x0",
"Vitoria x Ceara":"0x2",
"Flamengo x São Paulo":"0x1",
"Fortaleza x Santos":"3x1",
"Palmeiras x Cruzeiro":"1x1",
"Bragantino x Vasco": "2x0"    
      },
         "Ronaldo": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"3x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"0x2",
"Vitoria x Ceara":"1x2",
"Flamengo x São Paulo":"0x2",
"Fortaleza x Santos":"1x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "1x2"    
      },
         "Lucas FLA": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"0x2",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "2x0"    
      },
         "Venceslau": {

"Atletico/MG x Bahia":"1x2",
"America/MG x Goias":"1x2",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"0x1",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"3x1",
"Palmeiras x Cruzeiro":"3x0",
"Bragantino x Vasco": "2x0"    
      },
         "Naldo Naja": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"1x2",
"Vitoria x Ceara":"2x0",
"Flamengo x São Paulo":"2x2",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "1x1"    
      },
         "Allyn": {

"Atletico/MG x Bahia":"2x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"3x0",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"2x1",
"Vitoria x Ceara":"1x1",
"Flamengo x São Paulo":"2x0",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "2x1"    
      },
         "Junior Naja": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"2x0",
"Grêmio x Fluminense":"2x0",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"2x2",
"Flamengo x São Paulo":"1x2",
"Fortaleza x Santos":"2x0",
"Palmeiras x Cruzeiro":"3x0",
"Bragantino x Vasco": "2x0"    
      },
         "Dida": {

"Atletico/MG x Bahia":"2x1",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"1x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"0x1",
"Flamengo x São Paulo":"1x1",
"Fortaleza x Santos":"1x0",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "2x1"    
      },
         "Dida 2": {

"Atletico/MG x Bahia":"1x0",
"America/MG x Goias":"1x0",
"Corinthians x Coritiba":"2x1",
"Grêmio x Fluminense":"1x1",
"Guarani x Juventude":"0x0",
"Vitoria x Ceara":"1x0",
"Flamengo x São Paulo":"2x1",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x1",
"Bragantino x Vasco": "1x0"    
      },
   "Vitoriano": {

"Atletico/MG x Bahia":"3x1",
"America/MG x Goias":"2x1",
"Corinthians x Coritiba":"3x0",
"Grêmio x Fluminense":"2x1",
"Guarani x Juventude":"2x0",
"Vitoria x Ceara":"2x1",
"Flamengo x São Paulo":"3x1",
"Fortaleza x Santos":"1x2",
"Palmeiras x Cruzeiro":"3x1",
"Bragantino x Vasco": "3x1"    
      },
         "Vitoriano 2": {

"Atletico/MG x Bahia":"3x0",
"America/MG x Goias":"1x1",
"Corinthians x Coritiba":"3x0",
"Grêmio x Fluminense":"1x2",
"Guarani x Juventude":"1x1",
"Vitoria x Ceara":"1x2",
"Flamengo x São Paulo":"2x2",
"Fortaleza x Santos":"2x1",
"Palmeiras x Cruzeiro":"2x0",
"Bragantino x Vasco": "3x0"    
      },


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
    for partida, placar_real in zip(partidas, placares_reais):
        placar_palpite = palpites_usuario[partida]
        pontos = calcular_pontuacao(placar_real, placar_palpite)
        pontos_total += pontos
    classificacao[palpite] = pontos_total

classificacao_ordenada = sorted(classificacao.items(), key=lambda x: x[1], reverse=True)

primeiros_colocados = [classificacao_ordenada[0]]
for posicao, (palpite, pontos) in enumerate(classificacao_ordenada[1:], start=1):
    if pontos == primeiros_colocados[0][1]:
        primeiros_colocados.append((palpite, pontos))
    else:
        break

print("Primeiros colocados:")
for posicao, (palpite, pontos) in enumerate(primeiros_colocados, start=1):
    print(f"{posicao}. {palpite}: {pontos} pontos")

# A exibição de todos os placares dos primeiros é removida aqui

classificacao_geral = sorted(classificacao.items(), key=lambda x: x[1], reverse=True)

print("Classificação final:")
for posicao, (palpite, pontos) in enumerate(classificacao_geral, start=1):
    print(f"{posicao}. {palpite}: {pontos} pontos")
