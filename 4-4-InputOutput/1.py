def load_file(filename):
    open_file = open(filename,"r")
    read_value = open_file.read().strip() 
    try:
        out_list = int(read_value)
    except ValueError:
        try:
            out_list = float(read_value)
        except ValueError:
            out_list = read_value        
    open_file.close()
    return out_list

contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
