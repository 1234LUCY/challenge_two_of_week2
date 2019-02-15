#lists, strings and loops.
string = input("please type any word:")#prompting the user to enter any string
vowel = 0 #initializing the count variable to zero
for n in string: #traversing through the characters of the string
    if (n=='a' or n=='e' or n=='i' or n=='o' or n=='u'): #checking if the character is a vowel 
        vowel = vowel+1 # each time a vowel is encountered, the count is incremented

print("The total number of vowels in the string you entered is:") #total number of vowels counted in the string is printed
print(vowel)


