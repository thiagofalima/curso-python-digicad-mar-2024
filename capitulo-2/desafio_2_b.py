A = int(input("Tamanho do lado A: "))
B = input("Tamanho do lado B: ")
C = input("Tamanho do lado C: ")

if A == B == C:
    print("Este triangulo eh um equilatero.")
elif A == B != C:
    print("Este triangulo eh um isosceles.")
elif A != B != C:
    print("Este triangulo eh um escaleno.")
elif B == A != C:
    print("Este triangulo eh um isosceles.")
elif B == C != A:
    print("Este triangulo eh um isosceles.")
elif C == A != B:
    print("Este triangulo eh um isosceles.")