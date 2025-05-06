# allowance = 10
# spending = 9
# print(allowance < spending)
# print(allowance > spending)
# print(allowance != spending)
# print(allowance == spending)
# print((allowance == 10) and (spending == 8))
# print((allowance == 12) or (spending == 8))

# while True:
#     answer = input("""Do you want to loop this argument?
#     Type yes or no: """)
#     if answer.lower()=="yes":
#         print("Okay lets go!")
#     else: 
#         print("Goodbyee..")
#         break

students_name=['Alex', 'Bryan', 'Christ', 'Dave', 'Eva']
students_score=[100, 75, 80, 78, 99]
students_grade=[]
students_grade=['A' if i >= 90 else
                'B' if i >= 70 else
                'C'
                for i in students_score]
# for i in students_score:
#     if (i >= 90):
#         students_grade.append('A')
#     elif (i >= 70):
#         students_grade.append('B')
#     else:
#         students_grade.append('C')
print(students_grade)