alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "

def encrypt(message:int,positions:int)->str:
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