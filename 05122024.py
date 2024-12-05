##def converter_segundos(segundos):
    ##horas = segundos // 3600
    ##minutos = (segundos % 3600) // 60
    ##segundos_restantes = segundos % 60
    
    ##resultado = []
    
    ##if horas > 0:
    ##    resultado.append(f"{horas} hora" + ("s" if horas > 1 else ""))
    ##if minutos > 0:
    ##    resultado.append(f"{minutos} minuto" + ("s" if minutos > 1 else ""))
    ##if segundos_restantes > 0:
    ##    resultado.append(f"{segundos_restantes} segundo" + ("s" if segundos_restantes > 1 else ""))
    
    ##return " e ".join(resultado)

    ##print(converter_segundos(3661))  # Saída: "1 hora, 1 minuto e 1 segundo"

##Exercicio02

##def calcular_juros_compostos(P, r, n):
##    A = P * (1 + r) ** n
##    return A

##capital_inicial = 1000  
##taxa_juros = 0.05  
##numero_periodos = 3 

##montante_final = calcular_juros_compostos(capital_inicial, taxa_juros, numero_periodos)
##print(f"Montante final após {numero_periodos} períodos: R$", montante_final)

##Exercicio03

##def contar_letras(s):
 ##   vogais = "aeiouAEIOU"
 ##   consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
 ##   cont_vogais = 0
 ##   cont_consoantes = 0
    
 ##   for char in s:
 ##       if char in vogais:
 ##           cont_vogais += 1
 ##       elif char in consoantes:
##            cont_consoantes += 1
    
 ##   return cont_vogais, cont_consoantes

##string_teste = "Olá, como você está?"
##vogais, consoantes = contar_letras(string_teste)
##print(f"Vogais: , Consoantes:", vogais, consoantes)


##Exercicio06

##def contar_palavras(s):
##    palavras = s.split()
    
##    return len(palavras)

##frase_teste = "Esta é uma frase de teste."
##quantidade_palavras = contar_palavras(frase_teste)
##print(f"Quantidade de palavras: {quantidade_palavras}")


##Exercicio08

##def primo(n):
##    if n <= 1:
##        return False
    
 ##   for i in range(2, int(n ** 0.5) + 1):
##        if n % i == 0:
 ##           return False
    
 ##   return True

##numero_teste = 29
##if primo(numero_teste):
 ##   print(f"{numero_teste} é primo.")
##else:
 ##   print(f"{numero_teste} não é primo.")


##Exercicio09

##def contar_caracteres(s, caractere):
 ##   return s.count(caractere)

##string_teste = "abracadabra"
##caractere_teste = "a"
##quantidade = contar_caracteres(string_teste, caractere_teste)
##print(f"O caractere '{caractere_teste}' aparece {quantidade} vezes na string.")


##Exercicio10

##def converter_temperatura(celsius):
 ##   fahrenheit = (celsius * 9/5) + 32
    
 ##   kelvin = celsius + 273.15
    
##    return fahrenheit, kelvin

##temperatura_celsius = 25  
##fahrenheit, kelvin = converter_temperatura(temperatura_celsius)
##print(f"{temperatura_celsius}°C é igual a {fahrenheit}°F e {kelvin}K.")


##Exercicio13

##def eh_palindromo(s):
##    s = s.replace(" ", "").lower()
    
 ##   return s == s[::-1]

##string_teste = "A man a plan a canal Panama"
##if eh_palindromo(string_teste):
##    print(f'"{string_teste}" é um palíndromo.')
##else:
##    print(f'"{string_teste}" não é um palíndromo.')


##Exercicio14

##def par_ou_impar(n):
##    if n % 2 == 0:
##        return "par"
##    else:
##        return "ímpar"

##numero_teste = 7
##resultado = par_ou_impar(numero_teste)
##print(f"O número {numero_teste} é {resultado}.")