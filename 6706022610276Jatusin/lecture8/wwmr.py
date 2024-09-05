import struct
with open ('records.din','rb') as file:
    record_size = struct.calcsize('i20sif')
    while True:
        data = file.read(record_size)
        if not data:
            break
        record = struct.unpack('i20sif',data)
        record = (record[0],record[1].decade().strip('\x00'),recode[2],recode[3])
        print(f'id:{recode[0]},name:{recode[1]},age:{recode[2],gpa:{recode[3]}}')