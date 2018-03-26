with open('feature2.txt') as f:
    data=f.read().split('\n')

f1=open('data.csv','wb')

dataset=[]

for line in data:
    temp=''
    temp+=line+'\n'
    f1.write(temp)



