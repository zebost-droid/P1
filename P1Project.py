emp_name = input('Enter your name: ')
hours_worked = float(input('Enter the number of hours worked: '))
hourly_rate = float(input('Enter your hourly rate: '))
tax_rate = float(input('Enter the tax rate (as a decimal): '))
gross_pay = hours_worked * hourly_rate
tax_withheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_withheld
print(f'Employee Name: {emp_name}')
print(f'Gross Pay: ${gross_pay:.2f}')
print(f'Tax Withheld: ${tax_withheld:.2f}')
print(f'Net Pay: ${net_pay:.2f}')