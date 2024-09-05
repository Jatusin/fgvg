import struct
num_record = int(input('how many record do you want to create?'))
with open('record.bin','wb')as file:
    for _ in range (num_record):
        id_num = int(input('enter id:'))
        name = input('enter name:')
        age = int(input('enter age'))
        gpa = float(input('enter gpa:'))
        data = struct.pack('i20sif',id_num,name.encode(),age,gpa)
        file.write(data)
print(f'{num_record}record have been written to records.bin')
