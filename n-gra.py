


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line




dic={}
pair={}
bi_gr={}
with open("1.txt") as f_in:
    for line in nonblank_lines(f_in):
        print(line)
        line=line.split(" ")
        #приведение текста в чувства
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


for i in pair:
    probab=pair[i]/dic[i[0]]
    if i[0] not in bi_gr:
        bi_gr[i[0]]=(i[1], probab)
    else:
        bi_gr[i[0]]+=(i[1], probab)
print(bi_gr)
        
#генерация
print("Введите первое слово")
prefix=input()
print("Задайте длинну генерируемого предложения")
leng=int(input())
ans=prefix
for k in range(leng):
    na=0
    for i in range(1, len(bi_gr[prefix]), 2):
        if bi_gr[prefix][i]>na:
            next_word=bi_gr[prefix][i-1]
    ans+=" " + next_word
    prefix=next_word
print(ans)
 
    
    
    
