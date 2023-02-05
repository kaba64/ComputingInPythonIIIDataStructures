def save_list(my_list, my_filename):
    output_file = open(my_filename, "w")
    for item in my_list:
        output_file.write(item + "\n")
    output_file.close()
        
def load_list(my_filename):
    new_list = []
    input_file = open(my_filename, "r")
    for line in input_file:
        new_list.append(line.strip())
    return new_list

save_list(['jun','ka','ja'], "book,txt")
print(load_list("book,txt"))
