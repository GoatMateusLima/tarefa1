import random
import time
import requests

API_KEY = "QCJ2QWJQLYYTB5SZ"
URL = "https://api.thingspeak.com/update?api_key= QCJ2QWJQLYYTB5SZ &field1= 0"

def enviar_dados (fieldnumber, value):
    while True:
        url = f'https://api.thingspeak.com/update?api_key={API_KEY}&field{fieldnumber}={value}'

        resposta = requests.get (url)

        if resposta.text != '0':
            return f"resposta: {resposta.text}"
        
        print("repetindo.......")
        time.sleep(15)


def main():
    temperatura = random.uniform(20, 30)
    umidade = random.uniform(50, 70)
    ano = random.uniform(1, 9999)
    numero_de_Humanos = random.uniform(1, 9999999)


if __name__ == "__main__":
    main()