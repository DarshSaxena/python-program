import matplotlib.pyplot as plt
names=[]
marks=[]
n=int(input("enter the number of entries"))
for i in range (n):
  name =input("Enter name of student")
  mark = int(input(f"Enter marks of "))
  names.append(name)
  marks.append(mark)
grade=[]
if mark in marks:
  if (marks >90):
    grade='A'
  if (marks >80):
    grade.append('8')
  if (marks >70):
    grade.append('C')
  if (marks >65):
    grade.append('D')
  if (marks >50):
    grade.append('E')
  else:
    grade.append('F')

plt.figure(figsize=(10,5))
plt.bar(name,marks)
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.tittlel("Student Marks and Grades")
