# tries decoding string with tons of different options
import base64, collections, math, re

# helping dictionaries
alphaNum = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6',
'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11', 'L': '12', 'M': '13',
'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26'}
numAlpha = {z: x for x, z in alphaNum.items()}

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lettersList = list(letters)

morseEnglish =  {'.-...': '&', '--..--': ',', '....-': '4', '.....':
'5', '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--':
'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
'.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
'.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
'---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
'....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
'-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
'--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
'-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
'----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}
englishMorse = {z: x for x, z in morseEnglish.items()}

'''
with open('lang-english.txt', 'r') as handle:
    englishDictionary = []

    for line in handle:
        englishDictionary.append(line.strip().upper())
'''

# helping methods
def hasNumbers(input):
    return any(char.isdigit() for char in input)
def hasLetters(input):
    return any(char.isalpha() for char in input)
def wordCheck(word):
    return word in englishDictionary

def rotate(input, rotation):
    rotOutput = ""
    for z in list(input):
        if z is " ":
            rotOutput = rotOutput + " "
        else:
            inbetween = int(alphaNum.get(z)) + rotation
            if inbetween > 26:
                inbetween = inbetween - 26
            rotOutput = rotOutput + numAlpha.get(str(inbetween))
    return rotOutput

# rot13
def rot13(input):
    print("ROT13")
    print("Shift 13:", rotate(input, 13))
    print()

# caesar cipher
def caesar(input):
    print ("CAESAR")
    for i in range(1, 26):
        print("Shift " + str(i) + ": " + rotate(input, i))
    print()

# null cipher
def null(input):
    # first letter of each word
    firstLetterOutput = ""
    for x in input.split():
        firstLetterOutput += x[0]

    # last letter of each word
    lastLetterOutput = ""
    for x in input.split():
        lastLetterOutput += x[len(x)-1]

    # just the capitalized letters
    capitalLetterOutput = ''.join([c for c in input if c.isupper()])

    if len(firstLetterOutput) > 1 or len(lastLetterOutput) > 1 or len(capitalLetterOutput) > 1:
        print ("NULL")
        if len(firstLetterOutput) > 1:
            print ("First letter :", firstLetterOutput)
        if len(lastLetterOutput) > 1:
            print ("Last letter :", lastLetterOutput)
        if len(capitalLetterOutput) > 1:
            print ("Capital letters :", capitalLetterOutput)
        print()

# polybius square
def polybius(input):
    check = list(input)
    for x in check:
        if int(x) > 5:
            return

    print("POLYBIUS")

    row1 = "ABCDE"
    row2 = "FGHIK"
    row3 = "LMNOP"
    row4 = "QRSTU"
    row5 = "VWXYZ"

    input = input.replace(" ","")
    polybiusArray = re.findall('..', input)
    polybiusOutput = ""

    for x in polybiusArray:
        secondNumber = x[1]
        secondNumber = int(secondNumber)

        if x[0] == "1":
            polybiusOutput = polybiusOutput + row1[secondNumber - 1]
        elif x[0] == "2":
            polybiusOutput = polybiusOutput + row2[secondNumber - 1]
        elif x[0] == "3":
            polybiusOutput = polybiusOutput + row3[secondNumber - 1]
        elif x[0] == "4":
            polybiusOutput = polybiusOutput + row4[secondNumber - 1]
        elif x[0] == "5":
            polybiusOutput = polybiusOutput + row5[secondNumber - 1]
    print("Translation:", polybiusOutput)

    print()

# two square
#def twoSquare(input):

# four square
#def fourSquare(input):

# transposition ciphers
def rail(input):
    length = len(input)

    if length > 2:
        print("RAIL")
        railInput = input

        for x in range(2, length):
            railInput = railInput + input
            railString = ""

            for y in range(0, length):
                railString = railString + railInput[x*y]
            print("Shift", x - 1, ":", railString)
        print()
# route cipher?  https://en.wikipedia.org/wiki/Transposition_cipher

# enigma
#def enigma(input):

# morse code
def morseConverter(input):
    length = len(collections.Counter(input).most_common(3))
    if length is 2:
        print("MORSE CODE")
        mostCommon = collections.Counter(input).most_common(2)[0][0]
        secondMostCommon = collections.Counter(input).most_common(2)[1][0]

        morse = input.replace(mostCommon, ".").replace(secondMostCommon, "-")
        print("Output 1:", morse)
        morse = morse.replace(".", "/").replace("-", ".").replace("/", "-")
        print("Output 2:", morse)
        print()
def morseEncoder(input):
    print("MORSE CODE ENCODER")
    morseOutput = ""
    english = input.upper()

    for x in list(english):
        if x is not " ":
            morseOutput = morseOutput + str(englishMorse.get(x) + " ")
    print("English to Morse:", morseOutput)
    print()
def morseDecoder(input):
    print("MORSE CODE DECODER")
    englishOutput = ""
    for x in input.split():
        englishOutput = englishOutput + str(morseEnglish.get(x))
    print("Morse to English:", englishOutput)
    print()

# monoalphabetic
#def monoalphabetic(input):

# polyalphabetic
#def polyalphabetic(input)

# vigenere
def vigenere(input):
    print("VIGENERE")
    key = ""
    solutions = {}
    for word in englishDictionary:
        key = re.sub('[\W_]+', '', word)
        if key[:len(input)] not in keyList:
            while len(key) < len(input):
                key = key + key
            keyLetters = list(key.upper())
            keyNumbers = []

            for x in keyLetters:
                keyNumbers.append(alphaNum.get(x))
            vigenereOutput = ""

            for z in list(input):
                try:
                    keyNum = int(keyNumbers[0])
                except IndexError:
                    pass
                keyNum = keyNum - 1
                inbetween = int(alphaNum.get(z)) - keyNum
                del keyNumbers[0]

                if inbetween < 1:
                    inbetween = 26 + inbetween
                vigenereOutput = vigenereOutput + numAlpha.get(str(inbetween))

            if vigenereOutput in englishDictionary:
                print("OUTPUT:", vigenereOutput)
                print("KEY:", key[:len(input)])
                print()

                #solutions.update({:len(input):vigenereOutput})
    if len(keyList) > 0:
        for keyEntry in len(keyList):
            print()
            print()
            print()
            for k, v in d.items():
                print(k, v)
            #print("Key:", keyList[keyEntry])
            #print("Text:", textList[keyEntry])
    print()

# base32
def base32(input):
    print(base64.b32decode(input, casefold=True))

# base64
def base64(input):
    print(base64.b64decode(input))

#input = input()
input = "hello world"
inputUpper = input.upper()
print("Input:", input)
print()
inputWords = inputUpper.split()

mostCommon = collections.Counter(input.replace(" ", "")).most_common(2)[0][0]
secondMostCommon = collections.Counter(input.replace(" ", "")).most_common(2)[1][0]

if mostCommon is "-" or secondMostCommon is "-":
    morseDecoder(input)
if hasLetters(input) is True and hasNumbers(input) is False:
    rot13(inputUpper)
    caesar(inputUpper)
    null(input)
    rail(inputUpper)
    morseConverter(inputUpper)
    morseEncoder(inputUpper)
    #vigenere(input)
if hasNumbers(input) is True and hasLetters(input) is False:
    polybius(input) # make this one line printed and look nicer
if hasLetters(input) is True and hasNumbers(input) is True:
    #base32(input)
    base64(input)
