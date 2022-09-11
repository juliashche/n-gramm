#считывание модели
bigram={}
a=[]
with open("model.txt") as f_in:
    for line in f_in:
        a.append(line)
a = [i.strip() for i in a]
for i in range(0, len(a)-1, 2):
    bigram[a[i]]=a[i+1]

#генерация
print("Enter you first word")
prefix=input()
print("Enter the number of words in the sentence")
length=int(input())
answer=prefix
for k in range(length):
    maxim=0
    for i in range(1, len(bigram[prefix].split(" ")), 2):
        if float(bigram[prefix].split(" ")[i])>maxim:
            maxim=float(bigram[prefix].split(" ")[i])
            next_word=bigram[prefix].split(" ")[i-1]
    answer+=" " + next_word
    prefix=next_word
print(answer)
 
    
    
    
