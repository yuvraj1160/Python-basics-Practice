'''Q2-> Write a program to accept marks of 6 students and display them in a sorted manner.'''


# Code

marks = []

f1= int(input ("Enter marks  : "))
marks.append(f1)

f2= int(input ("Enter marks  : "))
marks.append(f2)

f3= int(input ("Enter marks  : "))
marks.append(f3)

f4= int(input ("Enter marks : "))
marks.append(f4)

f5= int(input ("Enter marks  : "))
marks.append(f5)

marks.sort()
print(marks)