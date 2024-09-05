import struct
with open('records.bin'<'rb')as file:
    data = file.read(struct.calcsize('120sif'))
    record = struct.unpack('i20sif',data)
    print(f'id{record[0]},name:{record[1]},age:{record[2]},gpa:{record[3]}')