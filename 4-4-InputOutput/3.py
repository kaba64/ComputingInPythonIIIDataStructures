def format_checker(name_in):
    file_name = open(name_in+".txt","r")
    sum_all = 0
    while True:
        a = file_name.readline().strip()
        list_in = a.split()
        if not list_in:
            break
        if(len(list_in)!= 5):
            return False
        for i in list_in:
            if(i=="" or i==" "):
                print(2)
                return False
        try:
            int(list_in[0])
            int(list_in[2])
            int(list_in[3])
            float(list_in[4])
            sum_all+= float(list_in[4])
            if(isinstance(list_in[1], str)==False):
                print(3)
                return False
        except:
            print(4)
            return False
    if(sum_all==1.):
        return True
    else:
        return False
    
print(format_checker("sample_1.cs1301"))
#print(format_checker("sample_2.cs1301"))
