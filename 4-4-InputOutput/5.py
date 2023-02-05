#def write_1301(name_in,list_in):
#    open_file = open(name_in,"w")
#    for i in list_in:
#        name = str(i[0])+" "+i[1]+" "+str(i[2])+" "+str(i[3])+" "+str(i[4])+"\n"
#        open_file.write(name)
#    open_file.close()


#The code below will test your function. It's not used
#for grading, so feel free to modify it! You may check
#output.cs1301 to see how it worked.
#tuple1 = (1, "exam_1", 90, 100, 0.6)
#tuple2 = (2, "exam_2", 95, 100, 0.4)
#tupleList = [tuple1, tuple2]
#write_1301("output.cs1301", tupleList)
def reader(name_in):
    file_name = open(name_in,"r")
    list_out = []
    while True:
        a = file_name.readline().strip()
        list_in = a.split()
        if not list_in:
            break
        list_out.append((int(list_in[0]),\
                         str(list_in[1]),int(list_in[2]),
                         int(list_in[3]),float(list_in[4])))
    file_name.close()
    return list_out

def get_grade(name_in):
    return reader(name_in)

print(get_grade("output.cs1301"))
