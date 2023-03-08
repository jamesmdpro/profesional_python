import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0 
    sequences = int(input("Cuantas secuencias debo relizar: "))
    cycle = 1


    while cycle <= sequences:

        if counter == 0:
            cycle += 1
            counter += 1
            yield n1
        elif counter == 1:
            cycle += 1
            counter += 1
            yield n2
        else:
            aux =n1 + n2
            n1, n2 = n2, aux
            cycle += 1
            counter += 1
            yield aux

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)