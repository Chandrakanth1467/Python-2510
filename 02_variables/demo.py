student_age=20
student_name="yamini"

print(student_age)
print(student_name)


print(id(student_age))
print(id(student_name))


print(type(student_age))
print(type(student_name))


data_one="Good"
data_two="night"
print(data_one+data_two)

num1=10
num2=20
print(num1+num2)
#print(num1+data_one)

name="yamini"
age=28
cibl=8.8
print(f"my name is {name} my age is {age} my cibl is {cibl}")


x,y,z=10,20,30
print(x,y,z)


x=y=z=10
print(x,y,z)


#Student management
Student_id=10
student_name="yamini"
student_age=30

#Score
quiz_score=80
assignment_score=30
exam_score=80

#Attendance
student_attendance=90

total_score=quiz_score+assignment_score+exam_score
print(total_score)
avg_score=total_score/3
print(avg_score)

student_passed=avg_score>75
print(student_passed)

#student_attendance=student_attendance+1
student_attendance +=1

student_award=student_attendance>=90 and student_passed

print(Student_id)
print(student_name)
print(student_age)
print(total_score)
print(avg_score)
print(student_award)
print(student_passed)



# car EMI

total_amount=1351492
down_payment=40000
bank_interestrate=8.8
r=bank_interestrate/(12*100)
loan_amount=total_amount-down_payment
print(loan_amount)
no_years=4
n=no_years*12
emi_calculate=(loan_amount*r*(1+r)**n)/((1+r)**n -1)

print(emi_calculate)



