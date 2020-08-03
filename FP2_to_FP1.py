import csv
csvfile=open("FP_Part-2.csv","r")
wr=open("formatted.csv","w")
st=""

csvreader = csv.reader(csvfile)
csvwriter=csv.writer(wr)

n=""
flag=0


for line in csvreader:
    if(line[0]!=n):
        if flag==1:
            if(st!=""):
                #print("\n",n,": \n",st)
                print(st)
            #print(st)
        n=line[0]
        st=line[2]
    else:
        st+=","+line[2]
        flag=1

if(st!=""):
    print(st)

#print(csvwriter)
csvfile.close()
wr.close()
