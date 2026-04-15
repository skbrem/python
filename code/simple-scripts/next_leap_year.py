current_year = int(input("Year: "))
year_test = current_year + 1

while True:
    if year_test % 400 == 0:
        print(f"The next leap year after {current_year} is {year_test}")
        break
    elif year_test % 100 == 0:
        check_year += 1
    
    elif year_test % 4 == 0:
        print(f"The next leap year after {current_year} is {year_test}")
        break
    else: 
        year_test += 1
