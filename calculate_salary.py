work_hours = [int (x) for x in input('enter the no of hours working in a day in a week ' ).split()]
print(work_hours)
wage = int(input('entr the salary in wage'))
total  = sum(work_hours)
salary = total * wage
print('salary is:', salary)