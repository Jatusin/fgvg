num_emps = int(input('how many employee records do you want to create?'))
with open('employees.txt','w')as emp_file:
    for count in range(1, num_emps+1):
        print('Enter data for example # ',count,sep="")
        name = input ('name:')
        id_num = input('ID number:')
        dept = input ('department:')
        emp_file.write(name +'\n')
        emp_file.write(id_num +'\n')
        emp_file.write(dept +'\n')
print()
print('employee recorfs written to employees.txt.')