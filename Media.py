notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

#calcular Média
mediafinal = (notaA + notaB)/2

#Verificação
if mediafinal >= 7.0:
    print("a média: %.1f - Aprovado" % mediafinal)
else:
    print("a média: %.1f - Reprovado" % mediafinal)