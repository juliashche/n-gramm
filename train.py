def empty_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

dic={}
pair={}
bigram={}
with open("input.txt") as f_in:
    #работа с текстом
    for line in empty_lines(f_in):
        line=line.split(" ")
        for i in range(len(line)):
            if len(line[i])==1 and (ord(line[i][0]) < 97 or ord(line[i][0]) > 122):
                continue
            else:
                line[i]=line[i].lower()
                if ord(line[i][0]) < 97 or ord(line[i][0]) > 122:
                    line[i]=line[i][1:]
                if ord(line[i][-1]) < 97 or ord(line[i][-1]) > 122:
                    line[i]=line[i][:-1]
                    if (ord(line[i][-1]) < 97 or ord(line[i][-1]) > 122) and len(line)>1:
                        line[i]=line[i][:-1]
                
        #создание словарей   
        for i in range(len(line)-1):
            if line[i] not in dic:
                dic[line[i]]=1
            else:
                dic[line[i]]+=1

            if (line[i], line[i+1]) not in pair:
                pair[(line[i], line[i+1])]=1
            else:
                pair[(line[i], line[i+1])]+=1

#создание биграммы
for i in pair:
    probab=pair[i]/dic[i[0]] #формула вероятности
    if i[0] not in bigram:
        bigram[i[0]]=(i[1], probab)
    else:
        bigram[i[0]]+=(i[1], probab)

#сохранене модели в файл
f_out=open("model.txt", "w")
for i, j in bigram.items():
    f_out.write(str(i) +'\n')
    for x in j:
        f_out.write(str(x)+' ')
    f_out.write('\n')           
f_out.close()
