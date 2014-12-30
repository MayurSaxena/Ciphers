"""
Mayur Saxena
2013-09-31
To perform a Caesar cipher
"""
import random

def encode(inputString,shiftValue):
    #if the user inputs r or R for random, change shiftValue to a random number
    if shiftValue == "R" or shiftValue == "r":
        # the random number should be between 1 and 25
        shiftValue = random.randrange(1,26)
        
    stringElements = []
    #creates a list from each letter of the string
    lst = list(inputString)
    
    for letter in lst:
        #any letter that can be regularly processesd
        
        if ord(letter) < (91-int(shiftValue)) and ord(letter) > 64:
         stringElements.append(chr(ord(letter)+int(shiftValue)))
         
      #Tests for spaces, punctuation, etc. adds them as is
         
        elif ord(letter) < 65 or ord(letter) > 90:
         stringElements.append(letter)
         
      # If the letter does go past A-Z after encode, keep in boundaries

        else:
            
      # We have to move S letters forward, so we see what is already covered
      # from the current letter to Z, and add the remaining from A
      # eg. if X with shift of 5, we can cover 2 letters until Z, and then add A,B,C
      # Start from 64 so A is included in addition
      
         stringElements.append(chr(64+(int(shiftValue)-(90-ord(letter)))))
     #exit the function, returning the whole word        

    return("".join(stringElements))

def moveCharsDecode(inputString,shiftValue):
    lst = list(inputString)
    stringElements = []
    for letter in lst:
         #Letters can be moved around without going past A-Z
        if ord(letter) < (91) and ord(letter) > (64+shiftValue):
           stringElements.append(chr(ord(letter)-shiftValue))
         #Tests for spaces, punctuation, etc.
        elif ord(letter) < 65 or ord(letter) > 90:
           stringElements.append(letter)
        else:
         # We have to move S letters backward, so we see what is already covered
         # from the current letter to A, and subtract the remaining from Z
         # eg. if E with shift of 5, we can cover 4 letters until A, and then add Z
         # Start from 91 so Z is included in addition         
           stringElements.append(chr(91-(shiftValue-(ord(letter)-65))))
           #return just the list
    return stringElements
	
print("Mayur's Caesar Shift Cipher Encoder/Decoder - v1.0\n")

# Does user want to encode or decode, keep going until proper response
while 1:
    while True:
          mode=input("Would you like to encode or decode? E/D/EXIT: ").upper()
          if mode == "e".upper() or mode == "d".upper() or mode == "exit".upper():
             break

    # User wants to encode
    if mode == "E":
       shiftValue = "invalid"
       inputString = ''
       allowedShifts = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 r R'.split(' ')
        # make a var with name inputString containing string
        #and shiftValue, an integer between 1 and 25
       print('')
       while len(inputString) == 0:
           inputString = (input("Enter string to be encoded: ")).upper()

       print('')

       while shiftValue not in allowedShifts:
           shiftValue = (input("Enter shift value from 1-25 or R (random): "))
    #print out the result of encode function, which is the joined word
       print ("\nYour encoded string is: "+ encode(inputString,shiftValue)+'\n')
       
    # User wants to decode
    elif mode == "D":
       shiftKnown = ''
       inputString = ''
       print('')
       while len(inputString)==0:
           inputString = input("Enter string to be decoded: ").upper()
       print('')
       while shiftKnown != 'Y' and shiftKnown != 'N':
           shiftKnown = input("Is shift value known? Y/N: ").upper()
       print('')
    # Shift value is known
       if shiftKnown == "Y":
           #S is the shift value
          S = ''
          allowedShifts = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split(' ')
          while S not in allowedShifts:
              S = input("Enter shift value from 1-25: ")
          S = int(S)
     #print our the result of moveChars decode, after joining the list elements together
          print ("\nYour decoded string is: "+ "".join(moveCharsDecode(inputString,S))+'\n')

    # Shift value is unknown
       else:
        # from here on is natural language processing
          points = 0
          pointsArray = []
          
          
          #Move through 1-25 (different shift values
          for i in range(1,26):
              #reset points after each number
             points = 0
              #assign different point values based on frequency of letters in English
              #loop through every character
             for character in moveCharsDecode(inputString,i):
                 if character == "A":
                     points += 8.167
                 if character == "B":
                     points += 1.492
                 if character == "C":
                     points += 2.782
                 if character == "D":
                     points += 4.253
                 if character == "E":
                     points += 12.702
                 if character == "F":
                     points += 2.228
                 if character == "G":
                     points += 2.015
                 if character == "H":
                     points += 6.094
                 if character == "I":
                     points += 6.966
                 if character == "J":
                     points += 0.153
                 if character == "K":
                     points += 0.772
                 if character == "L":
                     points += 4.025
                 if character == "M":
                     points += 2.406
                 if character == "N":
                     points += 6.749
                 if character == "O":
                     points += 7.507
                 if character == "P":
                     points += 1.929
                 if character == "Q":
                     points += 0.095
                 if character == "R":
                     points += 5.987
                 if character == "S":
                     points += 6.327
                 if character == "T":
                     points += 9.056
                 if character == "U":
                     points += 2.758
                 if character == "V":
                     points += 0.978
                 if character == "W":
                     points += 2.360
                 if character == "X":
                     points += 0.150
                 if character == "Y":
                     points += 1.974
                 if character == "Z":
                     points += 0.074

                #still part of NLP, checks for pairs of the same letters
             for j in range(0,len(moveCharsDecode(inputString,i))-1):
                   
                 nextDoubleSet = moveCharsDecode(inputString,i)[j] + moveCharsDecode(inputString,i)[j+1]

                 if nextDoubleSet == "LL":
                       points += 56
                 if nextDoubleSet == "EE":
                       points += 48
                 if nextDoubleSet == "SS":
                       points += 43
                 if nextDoubleSet == "OO":
                       points += 36
                 if nextDoubleSet == "TT":
                       points += 56
                 if nextDoubleSet == "FF":
                       points += 11
                 if nextDoubleSet == "RR":
                       points += 14
                 if nextDoubleSet == "NN":
                       points += 8
                 if nextDoubleSet == "PP":
                       points += 10
                 if nextDoubleSet == "CC":
                       points += 4
                 if nextDoubleSet == "AA":
                       points += 1
                 if nextDoubleSet == "BB":
                       points += 1
                 if nextDoubleSet == "DD":
                       points += 13
                 if nextDoubleSet == "GG":
                       points += 4
                 if nextDoubleSet == "HH":
                       points += 6
                 if nextDoubleSet == "II":
                       points += 1
                 if nextDoubleSet == "JJ":
                       points += 0
                 if nextDoubleSet == "KK":
                       points += 0
                 if nextDoubleSet == "MM":
                       points += 5
                 if nextDoubleSet == "QQ":
                       points += 0
                 if nextDoubleSet == "UU":
                       points += 0
                 if nextDoubleSet == "VV":
                       points += 0
                 if nextDoubleSet == "WW":
                       points += 2
                 if nextDoubleSet == "XX":
                       points += 0
                 if nextDoubleSet == "YY":
                       points += 2
                 if nextDoubleSet == "ZZ":
                       points += 0
                 


             #for each shift value, a different item in the array will have a value
             pointsArray.append(points)

            
          # the highest points value is the most likely shift, and add 1 because list elements start at 0
          actualShift = pointsArray.index(max(pointsArray)) + 1

          #print out the result, passing in actualShift
          print ("The most likely string is: "+"".join(moveCharsDecode(inputString,actualShift))+", where shift is "+str(actualShift))
          print('')

          seeMore = ''
          
          #what if our NLP was wrong? Let the user see more...
          while seeMore != 'Y' and seeMore != 'N':
              seeMore = input(("Output doesn't make sense? Would you like to see more? (Y/N): ")).upper()

          if seeMore == "Y":
                #every single shift value, print it out
             for i in range(1,26):
                 print ("\n"+"".join(moveCharsDecode(inputString,i))+", where shift is "+str(i))

          print('')

    else:
        break
