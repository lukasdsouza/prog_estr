import cmath

def calcula_raizes(coeficiente_a, coeficiente_b, coeficiente_c):
    # Calcula o discriminante
    discriminante = (b**2 - 4*a*c)**2 - 4*(a**2*b**2 - 4*a*b*c + c**2)

    # Calcula as raízes usando a fórmula de Bhaskara
    delta_numerador = (discriminante**(1/2) - (b**2 - 4*a*c))/(2*27*a**3)
    delta_denominador = (9*a**2)
    delta = delta_numerador / delta_denominador
    raiz1 = (-b/2*a + cmath.sqrt(delta))
    raiz2 = (-b/2*a - cmath.sqrt(delta))
    raiz3 = -0.5*raiz1
    raiz4 = -0.5*raiz2

    return raiz1, raiz2, raiz3, raiz4

# Solicita os coeficientes
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

# Encontra as raízes
raizes = calcula_raizes(a, b, c)

# Imprime as raízes
print("As raízes são:", raizes)