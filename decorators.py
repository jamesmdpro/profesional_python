from datetime import datetime

# decorador que calcula el tiempo de ejecucion de una funcion 
def execution_time(func):
    def wrapper(*args, **kwargs):  # wrapper emboltura args-kwargs aceptan lo enviado o sin enviar 
        initial_time = datetime.now() # dat..now indica el tiempo del momento
        func(*args, ** kwargs) 
        final_time = datetime.now() # dat..now indica el tiempo del momento
        timee_elapsed = final_time - initial_time # se resta para saber el resultado
        print("pasaron" + str(timee_elapsed.total_seconds()) + "segundos") # respuesta pantalla
    return wrapper  # retorna la respuesta lo que hace que sea un CLOUSURE  

@execution_time
def random_func():  # de esta manera se llama el decorador 
    for _ in range(1, 1000000): # _ indica que no nos interesa el numero solo la acción
        pass

@execution_time
def suma(a: int, b: int)-> int:
    return a + b

@execution_time
def saludo(nombre="James"):
    print("Hola " + nombre)


random_func()
suma(5, 5)
saludo("James")
