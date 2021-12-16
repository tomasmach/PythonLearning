phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for i in phone_numbers:
    if isinstance(i, int):
        print(i.replace("+", "00"))