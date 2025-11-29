** start of main.py **

def number_pattern(n):
    list_kosong = []
    if not isinstance(n,int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    for i in range(1,n+1):
        list_kosong.append(str(i))
    return " ".join(list_kosong)
print(number_pattern(4))

** end of main.py **

