def corrigir_frases(texto):
    texto_corrigido = ""
    frases = texto.split(".")
    
    for i in range(len(frases)):
        frase = frases[i].strip()
        
        if frase:  
            frase = frase[0].upper() + frase[1:].lower()
        
        texto_corrigido += frase
        
        if i < len(frases) - 1:
            texto_corrigido += "."
    
    return texto_corrigido.strip()

texto = input().strip()

resultado = corrigir_frases(texto)

print(resultado)