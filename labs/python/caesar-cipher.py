def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# request user message that they want to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# request user to input cipher key that they want to use
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount


# create function for encrypting a message that takes in (message, cipherKey, alphabet) as parameters
def encryptMessage (message, cipherKey, alphabet):
    # initialize variable
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    # create a for loop to traverse each letter in the message
    for currentCharacter in uppercaseMessage:
        # find position of a specific letter
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        # conditional statement for determining whether current letter is in alphabet or not and how to handle it
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Function to decrypte a message

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


# decrypt message

def runCaesarCipherProgram():
    # define a string variable containing A-Z
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    # double the alphabet string created in order to shift it
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    # take in input message from user to encrypt
    myMessage = getMessage()
    print(myMessage)
    # get input on which cipher key to use
    myCipherKey = getCipherKey()
    print(myCipherKey)
    # encrypt message
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    # decrypt message
    myDecryptMessage = decryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptMessage}')

# 
runCaesarCipherProgram()




