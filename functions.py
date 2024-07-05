alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
number = 0
message = ""

def start_program():
    message = request_message()
    number = request_number()
    pattern = create_encrypt(number)
    encrypted_message = pattern(message)
    return print(encrypted_message)

def request_number():
    """
    Solicita un numero y luego devuelve dicho numero.
    Si el usuario no ingresa un numero valido:
        1. Devuelve ValueError.
        2. Vuelve a solicitar un numero al usuario.
    Si el usuario ingresa un numero valido, devuelve dicho numero.
    """
    global number
    while True:
        try:
            number = int(input("Ingrese un numero entero: "))
            if type(number) == float:
                raise ValueError(f'Usted ingreso un numero con decimales: "{number}"')
            return number
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese un numero valido: ')

def request_message():
    """
    Solicita un mensaje y luego devuelve dicho mensaje.
    Si el usuario ingresa un mensaje vacio, la
    funcion devuelve una cadena vacia.
    """
    global message
    message = input("Ingrese el mensaje que desea encriptar: ")
    return message

def create_encrypt(positions:int):
    def encrypt(message:int)->str:
        result = ""
        for character in message.upper():
            if character in alphabet:
                i = alphabet.index(character)
                index = i + positions
                if index >= len(alphabet):
                    index = abs(-len(alphabet) + index)
                    result += alphabet[index]
                else: 
                    result += alphabet[index]
        return result
    return encrypt