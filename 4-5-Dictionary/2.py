def length_words(string_in):
    dict_out = {}
    punc = '''.,?'!'''
    for i in string_in:
        if i in punc:
            string_in = string_in.replace(i,"")
    list_in = string_in.lower().split(" ")
    for i in list_in:
        if len(i) not in dict_out:
            dict_out[len(i)]=[i]
        else:
            dict_out[len(i)].append(i)
    return dict_out


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))
