#creando una funcion que muestre la serie de fibonacci entre el 0 el nuero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = [0]
    for i in range(num):
        if b > num: return fibonacci_list
        else:
            fibonacci_list.append(b)
            a,b = b,a+b
            
resultado = fibonacci(20)
print(resultado)
            