# Loops over dictionary exercises

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for number in phone_numbers.values():
    print(number.removeprefix("+").zfill(14))


# this above solution is wrong but was me just thinking out loud using the dir function to see how else i could do the problem

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for number in phone_numbers.values():
    print(number.replace("+", "00"))
    