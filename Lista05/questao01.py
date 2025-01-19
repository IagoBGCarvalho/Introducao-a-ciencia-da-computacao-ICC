def decodificar_mensagem(frase):
    palavras = frase.split()
    mensagem = ''.join([palavra[1] for palavra in palavras if len(palavra) >= 2])
    return mensagem

frase = input()

print(decodificar_mensagem(frase))