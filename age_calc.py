def year_born(age):
    this_year = int(2022)
    year_born = this_year - age
    return f"You were born in {year_born}"

age = int(input("Please enter youe age:"))
print(year_born(age))