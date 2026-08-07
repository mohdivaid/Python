flag=True
a=[]
while flag:
    user_input=int(input('enter the number: '))
    if (user_input!=-1):
        a.append(user_input)
    elif(user_input==-1):
        flag=False
print("total number",len(a))
print("sum of numbers",sum(a))
print("smallest number",min(a))
print("largest number",max(a))