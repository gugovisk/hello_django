from django.shortcuts import HttpResponse


# Create your views here.

def hello(request, nome, idade, operacao, num1, num2):
    resultado=0
    match operacao:
        case "soma":
            resultado = num1 + num2
        case "subtracao":
            resultado = num1 - num2
        case "multiplicacao":
            resultado = num1 * num2
        case "divisao":
            resultado = num1 - num2


    return HttpResponse('<h1>Hello {} de {} anos. O resultado da {} é {} </h1>'.format(nome,idade,operacao,resultado))