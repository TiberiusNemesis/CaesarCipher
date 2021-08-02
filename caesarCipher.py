#Author: Tiberius Nemesis Dourado
#This program is an encoder and a decoder for a Caesar Cipher.

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encoder(text, shift):
    encoding = []
    for i in range(len(text)):
        encoding.append(text[i])
        if encoding[i] in alphabet:
            encoding[i] = alphabet[alphabet.index(text[i])+shift]
    message = "".join(encoding)
    return(message)
def decoder(text, shift):
    decoding = []
    for i in range(len(text)):
        decoding.append(text[i])
        if decoding[i] in alphabet:
            decoding[i] = alphabet[alphabet.index(text[i])-shift]
    message = "".join(decoding)
    return (message)

print("CAESAR CYPHER ENCODER\n")
operation = input('Type in "encode" to make a cipher, or "decode" to decipher something: ')
while operation != "encode" and operation != "decode":
    operation = input('\nType in "encode" to make a cipher, or "decode" to decipher something: ').lower()

if operation == "encode":
    encoding = input("Input the message to be encoded: ").lower()
    cipher = int(input("Type in the shift number: "))
    while cipher > 25:
        cipher = int(input("Type in a valid shift number: "))
    message = encoder(encoding, cipher)
    print("Encoded message: " + message)
elif operation == "decode":
    decoding = input("Input the message to be decoded: ").lower()
    cipher = int(input("Type in the shift number: "))
    while cipher > 25:
        cipher = int(input("Type in a valid shift number: "))
    message = decoder(decoding, cipher)
    print("Decoded message: " + message)





