from datetime import date
def age(dob):
    today = date.today()
    years = today.year - dob.year
    if(today.month,today.day) < (dob.month , dob.day):
        years -=1
    return years

print(age(date(2002, 7,11)))