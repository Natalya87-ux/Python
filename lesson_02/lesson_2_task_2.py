def is_year_leap(year, res):
    if year % 4 == 0:
        res = True
        print(f"Год {year}: {res}")
    else:
        res = False
        print(f"Год {year}: {res}")


res = bool
year_as_string = int(input("Введите год:"))
is_year_leap(year_as_string, res)
