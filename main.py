import requests
import json
import time
from flask import Flask, jsonify

# iniciando o script com flask
app = Flask(__name__)


# ordenando os valores com quicksort
def dividirvet(vet, prim, ult):
    valorpivo = vet[prim]

    primpos = prim +1
    ultpos = ult

    fim = False
    while not fim:
        while primpos <= ultpos and vet[primpos] <= valorpivo:
            primpos = primpos + 1

        while vet[ultpos] >= valorpivo and ultpos >= primpos:
            ultpos = ultpos - 1

        if ultpos < primpos:
            fim = True
        else:
            temp = vet[primpos]
            vet[primpos] = vet[ultpos]
            vet[ultpos] = temp

    temp = vet[prim]
    vet[prim] = vet[ultpos]
    vet[ultpos] = temp

    return ultpos


# para auxiliar a fazer a seleção dos valores maiores ou menores
def quick_helper(vet, prim, ult):
    if prim < ult:
        indicdiv = dividirvet(vet, prim, ult)

        quick_helper(vet, prim, indicdiv -1)
        quick_helper(vet, indicdiv +1, ult)


# chamando a função de ordenamento
def ordena_quick(vet):
    print('começando o ordenamento')
    print(vet)
    quick_helper(vet, 0, len(vet)-1)
    vetjson = json.dumps(vet, ensure_ascii=False)
    print(vetjson)
    return vetjson


@app.route('/', methods=['GET'])
# pegando os valores da API
def get_data():
    control = 0
    page = 9990
    vet = []
    while control != -1:
        tentativas = 0
        values = requests.get("http://challenge.dienekes.com.br/api/numbers?page="+str(page))
        elements = json.loads(values.content)
#        print(type(elements))
        if 'numbers' in elements:
            if len(elements['numbers']) == 0:
                control = -1
            vet = vet + elements['numbers']
            print(page)
            page = page + 1
        else:
            while tentativas < 3:
                time.sleep(3)
                values = requests.get("http://challenge.dienekes.com.br/api/numbers?page=" + str(page))
                elements = json.loads(values.content)
                if 'numbers' in elements:
                    vet = vet + elements['numbers']
                    print(page)
                    print('segunda chance')
                    page = page + 1
                    tentativas = 4
                else:
                    tentativas = tentativas + 1
                    print('tentativa: ', tentativas)
                    if tentativas == 4:
                        print('fim, chamar a ordenação')
                        control = -1
    variavel = ordena_quick(vet)
    return variavel


if __name__ == '__main__':
    app.run()
