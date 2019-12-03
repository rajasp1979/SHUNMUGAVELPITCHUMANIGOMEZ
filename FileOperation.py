import re
from os import listdir
from os.path import isfile, join
#mypath = "./RAND/"
mypath = "C:/RajaHilman/RAND/"
allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("File List :\n",allfiles)
for fileinp in allfiles:

    f = open(mypath+fileinp, "r+")
    lst = [ re.findall("\S+", l) for l in f.readlines() ]
    row_cnt = len(lst)
    loc1_ind = lst[0].index("LOC_01")
    loc2_ind = lst[0].index("LOC_02")
    dad_ind = lst[0].index("DAD")
    mom_ind = lst[0].index("MOM")
    chng_ind = lst[0].index("IsProband")
    row_ind = []
    for i in range(row_cnt):
        if i != 0:
            if lst[i][loc1_ind] in ("A1/A2","A2/A1") and lst[i][loc2_ind] in ("M1/M2","M2/M1") and lst[i][dad_ind] != "-1" and lst[i][mom_ind] != "-1":
                row_ind.append(i)
        else:
            pass
    f.close()
    f2 = open(mypath+fileinp, "r+")
    line_str=''
    for ind,line in enumerate(f2):
        if ind in row_ind:
            repl_str = line[:-2] + "#\n"
            line_str = line_str + repl_str
        else:
            line_str = line_str + line
    f2.close()
    f_out = open(mypath+fileinp, "w")
    f_out.write(line_str)
    f_out.close()
    print("File replace done for :", fileinp)
print ("All files replaced in the given directory!")