#Dados cinco enteros positivos, encuentre los valores mínimo y máximo
# que se pueden calcular sumando exactamente cuatro de los cinco enteros. 
# Luego imprima los respectivos valores mínimo y máximo 
# como una sola línea de dos enteros largos separados por espacios con su respectivo nombre.
def miniMaxSum(arr):
    max = 0
    min = 0
    for i in range(len(arr)):
        aux = sum(arr) - arr[i]
        if max < aux:
            max = aux
        if min > aux or min == 0:
            min = aux
    print(f'Minimo:{min} Maximo:{max}')

if __name__ == '__main__':
    try:
        arr = list(map(int, input().rstrip().split()))
        miniMaxSum(arr)
    except ValueError as ve:
        print('Debe ingresar un lista de numeros separados por espacio')
    