def sort_films(name_in,name_w):
    open_file = open(name_in,"r")
    open_filew = open(name_w,"w")
    list_in = []
    for i in open_file:
        list_in.append([i.strip().split("\t")[0],int(i.strip().split("\t")[1])])
        list_in.sort(key = lambda i: i[1],reverse=True)
    for i in list_in:
        open_filew.write((i[0]+"\t"+str(i[1])+"\n"))
    open_file.close()
    open_filew.close()

sort_films("top500.txt", "top500result.txt")
