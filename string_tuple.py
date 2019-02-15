def vowels(letters): # function called vowels
    
    #list of vowels
    vowel = ['a','e','i','o','u']
    
    #changing the input string into a list
    list_string =list(letters) 
    
    #compare if each character of the string is in the vowel list then store in list.
    new_list =[char for char in list_string if char in vowel] 

    #changing the new list of vowels into a tuple
    tuple0 = tuple(new_list) 

    #removing duplicates from tuple0
    remove_duplicates ="".join(OrderedDict.fromkeys(tuple0))

    # putting the results after removing the duplicates into a tuple with one item
    unique_tuple = (remove_duplicates,)

    dup0_char = [letter for letter in letters if letters.count(letter) > 1]

    #getting the number of duplicates from the original string
    unique_char = “”.join(OrderedDict.fromkeys(dup0_char))

    #after removing duplicates, convert it into a tuple
    tuple_dup = tuple(unique_char)

    #Get the length of the characters
    count_tuple_dup = len(tuple_dup)
    count_tuple_dup_final = (count_tuple_dup,)

    #combining the first and second tuple
    combine_tuple = get_unique_vowels_tuple + count_tuple_dup_final
    print(combine_tuple)
    word = “busitemauniversity”
    vowels(letters)
    
