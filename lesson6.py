#1
list=[]
while len(list) != 5:
	list.append(input())

#2
names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
a = 0
for i in names:
	if 'JACK' == i:
		a +=1
print(a)
print()

#3
#b = 0
#while r < 
#for i in range(len(names)):
#	if i % 2 == 0:
#		names.pop(i)
#print(names)
del names[0:10:2]
print(names)


#4
list=[]
list.append(input())
list.append(input())
list.append(input())	
print(list)


#5
list=['nurtai','aman','jack','baibo','ken']
a = ''.join(list)
print(a)

