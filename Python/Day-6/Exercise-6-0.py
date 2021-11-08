# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
student_total = 0
stundntH_total =0 

for i in student_heights:  

    stundntH_total += i
    student_total += 1

hAVG =stundntH_total / student_total


print(f"{stundntH_total} / {student_total }={hAVG}")

#Write your code below this row 👇




 