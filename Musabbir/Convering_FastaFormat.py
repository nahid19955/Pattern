fh=open("File_name.fasta")
count=0
num=0
for line in fh:
    if line.startswith(">"):continue
    line=line.rstrip()
    print(">"+str(num)+"|0|training")   #|1| for negetive files
    print(line)
    count+=1
    num+=1
print(count)