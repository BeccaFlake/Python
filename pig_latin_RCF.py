#!/usr/bin/env python3

def get_input():
    uinput = input("Enter text: ")
    #input validation
    digit = False
    for char in uinput:                 #the sentence is made up of or has a digit/digits, it is invalid
        if char.isdigit():
            digit = True
    if digit == True:
        print("Please enter a sentence. ")
        get_input()
    #remove punctuation
    else:
        uinput = uinput.replace("\n", "")
        uinput = uinput.replace(",", "")
        uinput = uinput.replace(".", "")
        uinput = uinput.replace("!", "")
        uinput = uinput.replace("?", "")
        uinput = uinput.replace("'", "")
        uinput = uinput.replace("\"", "")
        uinput = uinput.replace(";", "")
        uinput = uinput.replace(":", "")
        uinput = uinput.replace("-", "")
        uinput = uinput.replace("_", "")
        sentence = uinput.lower()
        return sentence

def translate_sentence(sentence):
    sentence = sentence
    wordlist = sentence.split()             #split the sentence into a list of individual words
    vowels = ("a", "e", "i", "o", "u")      #a tuple of vowels
    translated_sentence = ""                #a variable to hold the translated sentence
    translation = []                        #an empty list to hold the translated words

    #loop that looks at each word in the list and translates it appropriately
    for word in wordlist:
        
        #if the word starts with a vowel
        if word.startswith(vowels):
            #join way to the end of the word
            newword = word + "way "         #the word simply has "way" and a space added to it. 
            translation.append(newword)     #append the translated word to the translation list
            
        else:
            #get the index for the first instance of the vowel
            a = word.find("a")
            if a == -1:                     
                a = 1000000                 
            e = word.find("e") 
            if e == -1:
                e = 1000000
            i = word.find("i")
            if i == -1:
                i = 1000000
            o = word.find("o")
            if o == -1:
                o = 1000000
            u = word.find("u")
            if u == -1:
                u = 1000000
            y = word.find("y")
            if y == -1:
                y = 1000000
                
            #If statements that find the first vowel in the word and then form the new word
            if ((a < e) and (a < i) and (a < o) and (a < u) and (a < y)):
                wordparts = word.split("a")
                #add the removed delimiter back
                if "aa" in word:
                   wordparts[1] = "aa" + wordparts[1] 
                else:    
                    wordparts[1] = "a" + wordparts[1]
                #form the new word
                newword = (wordparts[1] + wordparts[0] + "ay ")
                #add the new word to the translated sentence
                translation.append(newword)
                
            elif ((e < a) and (e < i) and (e < o) and (e < u) and(e < y)) :
                wordparts = word.split("e")
                if "ee" in word:
                   wordparts[1] = "ee" + wordparts[1] 
                else:    
                    wordparts[1] = "e" + wordparts[1]
                newword = (wordparts[1] + wordparts[0] + "ay ")
                translation.append(newword)
                
            elif ((i < a) and (i < e) and (i < o) and(i < u) and(i < y)):
                wordparts = word.split("i")
                if "ii" in word:
                   wordparts[1] = "ii" + wordparts[1] 
                else:    
                    wordparts[1] = "i" + wordparts[1]
                newword = (wordparts[1] + wordparts[0] + "ay ")
                translation.append(newword)
                
            elif ((o < a) and (o < e) and (o < i) and (o < u) and (o < y)):
                wordparts = word.split("o")
                if "oo" in word:
                    wordparts[1] = "oo" + wordparts[1] 
                else:    
                    wordparts[1] = "o" + wordparts[1]
                newword = (wordparts[1] + wordparts[0] + "ay ")
                translation.append(newword)
                
            elif ((u < a) and (u < e) and (u < i) and(u < o) and (u < y)):
                wordparts = word.split("u")
                if "uu" in word:
                    wordparts[1] = "uu" + wordparts[1] 
                else:    
                    wordparts[1] = "u" + wordparts[1]
                newword = (wordparts[1] + wordparts[0] + "ay ")
                translation.append(newword)
                
            elif ((y < a) and (y < e) and (y < i) and (y < o) and (y < u)):
                wordparts = word.split("y")
                if "yy" in word:
                    wordparts[1] = "yy" + wordparts[1] 
                else:    
                    wordparts[1] = "y" + wordparts[1]
                newword = (wordparts[1] + wordparts[0] + "ay ")
                translation.append(newword)

    #join the translated words into a new sentence and print it
    translation = translated_sentence.join(translation)
    return translation

def main():
    print("Pig Latin Translator\n\n")
    choice = "y"
    while choice.lower() == "y":
        sentence = get_input()
        print("English:   ", sentence)
        translation = translate_sentence(sentence)
        print("Pig Latin: ", translation)
        choice = input("\nContinue? (y/n): ")
        print()
    print("\n\nBye!")
        
if __name__ == "__main__":
    main()

