import sys
bottles = {}
alphabet = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',0:'j'}

n = sys.stdin.readline()
for i in range(n):
    bottle = sys.stdin.readline()[:-1]
    if bottle in bottles:
        pass
    else:
        
    print(bottles[bottle])



# k=int(input())
# foundList = []
# nameList = []
# count = 0
# output = []
# # letters = "vabcdefghijklmnopqrstuw"
# name = ""
# for i in range(k):
#     hold=str(input())
    
#     hold=hold[:-1]

    
#     if hold in (foundList):
#         for i, ii in enumerate(foundList):
#             output.append(nameList[i])
            

#     else:
#         name = "a"
#         for i in range(count):
#             name = name + "a"
#         nameList.append(name)
#         foundList.append(hold)
#         output.append(name)
#         count += 1

# for i in output:
#     print(str(i))

# k=int(input())
# final=[]

# for i in range(k):
#     hold=str(input())
#     hold=hold[:-1]
#     hold=float(hold)
#     l=1
#     for i in range(len(final)):
#         if final[i][0]==hold:
#             print(final[i][1])
#             l=0
#             break
#     if l==1:
#         gg=''
#         for i in range(len(final)+1):
#             gg=gg+'a'
#         final.append([hold,gg])
#         print(gg)
    

    






