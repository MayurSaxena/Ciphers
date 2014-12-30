"""
Mayur Saxena
2013-09-30
To perform a Vignere cipher
"""

while 1:

    method = '' 

    while method != "D" and method != "E" and method != "EXIT":
        method = str(input("Would you like to encrypt or decrypt? E/D/EXIT: ")).upper()
        

    if method == "EXIT":
        break

    else:

        key = ""
        phrase = ''

        print('')

        while len(phrase) == 0:
    
            phrase = str(input("Please enter a phrase: ")).upper() #Input phrase in uppercase

        print('')
        while key.isalpha() == False or len(key) == 0:
            key = str(input("Please enter an alphabetical key: ")).upper().replace(' ','') #Input key in uppercase without spaces

        lengthenedKey = (key * (len(phrase)//len(key))) + key[0:len(phrase)-(len(key)*(len(phrase)//len(key)))] #Make the key the same length as the phrase

        if method == "E": #They want to encrypt
            encryptedString = ""

            for i in range(0,len(phrase)): #From 0 to the length of the phrase

                if ord(phrase[i]) < 65 or ord(phrase[i]) > 90:
                    ordToConvert = ord(phrase[i])

                else:

                    ordToConvert = ord(phrase[i])+ord(lengthenedKey[i])-65 # The new char number

                    if ordToConvert > 90: #Loop it around
                        ordToConvert = 64 + ordToConvert-90

                encryptedString += chr(ordToConvert) #Add it to the string

            print("\nThe encrypted phrase is: " + encryptedString + '\n') #Print it out

        elif method == "D": #Same thing as above
            decryptedString = ""

            for i in range(0,len(phrase)):

                if ord(phrase[i]) < 65 or ord(phrase[i]) > 90:
                    ordToConvert = ord(phrase[i])

                else:
                    ordToConvert = ord(phrase[i])-(ord(lengthenedKey[i])-65) #Go backwards because you're decrypting

                    if ordToConvert < 65:
                        ordToConvert = 91 - (65-ordToConvert)

                decryptedString += chr(ordToConvert)

            print("\nThe decrypted phrase is: " +decryptedString+'\n')
