line=str(input())
line=line.split()
for i in range(len(line)):
    line[i]=int(line[i])

npiers=line[0]
cards=line[1]
events=line[2]
data=[]
data2=[]
for i in range(cards):
    data.append(0)
for i in range(cards):
    data2.append(0)

for i in range(events):
    current=str(input())
    current=current.split()
    current[0]=int(current[0])
    current[1]=int(current[1])
    if data[current[1]-1]==0:
        data[current[1]-1]=current[0]

    else:
        if abs(current[0]-data[current[1]-1])==0:
            data2[current[1]-1]=data2[current[1]-1]+100
        else:
            data2[current[1]-1]=data2[current[1]-1]+abs(current[0]-data[current[1]-1])
            data[current[1]-1]=0
    


    # data[current[1]-1]=current[0]

for i in range(len(data)):
    if data[i]!=0:
        data2[i]=data2[i]+100


for i in range(len(data2)):
    print(data2[i], '')

print(data,data2)


