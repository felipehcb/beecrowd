values = input().split(' ')
a = float(values[0])
b = float(values[1])
c = float(values[2])
PI = 3.14159
triangulo_retangulo = a * c / 2
area_circulo = PI * c * c
area_trapezio = (a+b)*c /2
area_quadrado = b**2
area_retangulo = a * b

print(f'TRIANGULO: {triangulo_retangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')