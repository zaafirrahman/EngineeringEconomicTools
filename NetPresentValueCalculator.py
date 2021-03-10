print('-'*46)
print('NET PRESENT VALUE CALCULATOR')
print('-'*46)
print('Period of use (n)')
years = int(input('Enter the time period in years : '))

print('Investment capital (P)')
principal = float(input('Enter the investment value : '))

print('Annual profit (A1)')
annual_income = float(input('Enter the annual profit: '))

print('Increase or decrease in profit (G1)')
gradient = float(input('Enter the increase / decrease in profit : '))

print('Annual fee (A2)')
annual_cost = float(input('Enter the annual fee : '))

print('Increase or decrease in annual costs (G2)')
gradient_cost = float(input('Enter the increase / decrease in annual costs : '))

print('Estimated annual interest rates (i)')
interest = float(input('Enter the estimated interest rate (without percent)  : '))
interest = interest/100

print('-'*46)

final_amount = 0
grad = 0
final_cost = 0
grad_ = 0
year = 0
year_ = 1
c_year = 0
c_year_ = 1

for i in range (0, years):
  if final_amount == 0:
    final_amount = 0

for g in range (0, years):
  grad += gradient
  year += year_

  print('Accumulated profit for the following year  = (',final_amount,'+((',annual_income,'+',grad-gradient,') / (', 1, '+', interest,')**', year,'))')

  final_amount = (final_amount + ((annual_income - gradient + grad)/(1 + interest)**year))

  final_pwb = final_amount

print('-'*46)

print('Percent worth of benefit :', final_pwb)

print('-'*46)

for j in range (0, years):
  if final_cost == 0:
    final_cost = 0

for h in range (0, years):
  grad_ += gradient_cost
  c_year += c_year_

  print('Accumulated cost for the following year  = (',final_cost,'+((',annual_cost,'+',grad_-gradient_cost,') / (', 1, '+', interest,')**', c_year,'))')

  final_cost = (final_cost + ((annual_cost - gradient_cost + grad_)/(1 + interest)**c_year))

  final_pwc = final_cost

print('Final cost =', final_cost)

final_pwc = final_cost + principal

print('-'*92)

print('Percent worth of cost (PWC) :', 'Final cost + Principal =', final_pwc)

print('-'*92)

print('Total net present value in', years, 'years (NPV): ', 'PWB - PWC =', str(final_pwb-final_pwc))
print('-'*92)
print('Note : The results listed (especially if using G) may not be the same / close to the results of the compound interest table formula, because the accuracy of the reference values in the table is only 3 to 4 digits behind the comma')
