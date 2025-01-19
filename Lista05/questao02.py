def traduzir_para_lingua_p(frase):
    vogais = "aeiouáéíóúàèìòùâêîôûãõäëïöüAEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜ"
    traduzida = ""
    
    for letra in frase:
        if letra.isalpha() and letra not in vogais:
            traduzida += "p"
        else:
            traduzida += letra
    
    return traduzida

frase = input()

print(traduzir_para_lingua_p(frase))