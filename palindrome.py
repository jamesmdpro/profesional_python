def is_palindrome(string: str) -> bool:  #Se aclara el tipado estatico
    string = string.replace(" ", "").lower() #Se eliminan espacios(replace), lower Cambia a MINUS
    return string == string[::-1] # gira el texto entregado 

def run():  
    print (is_palindrome(1000))

if __name__ == '__main__':
    run()