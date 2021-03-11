# Run it only with Jupyter notebook or other Python IDE
# Please only input numbers, and if it reaches thousands and above do not use dots
# Continue to do the previous step as requested until it's finished
# If there is a question that is not needed, please fill in the zero '0'
# Especially for G (be it G1 or G2) if it decreases, give minus '-' in front of nominal
# Doesn't yet support calculation with different time of usage period (list common multiple)

print('-'*46)
print('NET PRESENT VALUE COMPARISON')
print('-'*46)

print('Investment capital of A (P(A))')
principal_a = float(input('Enter the investment value of A : '))

print('Annual profit of A (A1(A))')
annual_income_a = float(input('Enter the annual profit of A : '))

print('Increase or decrease in annual profit of A (G1(A))')
gradient_a = float(input('Enter the increase / decrease in annual profit of A : '))

print('Annual fee of A (A2(A))')
annual_cost_a = float(input('Enter the annual fee of A : '))

print('Increase or decrease in annual costs of A (G2(A))')
gradient_cost_a = float(input('Enter the increase / decrease in annual costs of A : '))

print('-'*46)

print('Investment capital of B (P(B))')
principal_b = float(input('Enter the investment value of B : '))

print('Annual profit of B (A1(B))')
annual_income_b = float(input('Enter the annual profit of B : '))

print('Increase or decrease in annual profit of B (G1(B))')
gradient_b = float(input('Enter the increase / decrease in annual profit of B : '))

print('Annual fee of B (A2(B))')
annual_cost_b = float(input('Enter the annual fee of B : '))

print('Increase or decrease in annual costs of B (G2(B))')
gradient_cost_b = float(input('Enter the increase / decrease in annual costs of B : '))

print('-'*46)

print('Period of use (n)')
years = int(input('Enter the time period in years : '))

print('Estimated annual interest rates (i)')
interest = float(input('Enter the estimated interest rate (without percent) : '))
interest = interest/100

print('='*46)

final_amount_a = 0
final_amount_b = 0
grad = 0
final_cost_a = 0
final_cost_b = 0
grad_ = 0
year_a = 0
year__a = 1
c_year_a = 0
c_year__a = 1
year_b = 0
year__b = 1
c_year_b = 0
c_year__b = 1

for i in range (0, years):
  if final_amount_a == 0:
    final_amount_a = 0

for g in range (0, years):
  grad += gradient_a
  year_a += year__a

  print('Accumulated profit for the following year (A) = (',final_amount_a,'+((',annual_income_a,'+',grad-gradient_a,') / (', 1, '+', interest,')**', year_a,'))')

  final_amount_a = (final_amount_a + ((annual_income_a - gradient_a + grad)/(1 + interest)**year_a))

  final_pwb_a = final_amount_a

print('-'*92)

print('Percent worth of benefit (PWB(A)) :', final_pwb_a)

print('-'*92)

for j in range (0, years):
  if final_cost_a == 0:
    final_cost_a = 0

for h in range (0, years):
  grad_ += gradient_cost_a
  c_year_a += c_year__a

  print('Accumulated expenses for the following year (A) = (',final_cost_a,'+((',annual_cost_a,'+',grad_-gradient_cost_a,') / (', 1, '+', interest,')**', c_year_a,'))')

  final_cost_a = (final_cost_a + ((annual_cost_a - gradient_cost_a + grad_)/(1 + interest)**c_year_a))

print('Final cost A =', final_cost_a)

final_pwc_a = final_cost_a + principal_a

print('-'*92)

print('Percent worth of cost (PWC(A)) :', 'Final cost A + Principal A =', final_pwc_a)

print('-'*92)

final_nvp_a = final_pwb_a-final_pwc_a

print('Total net present value of A in', years, 'years (NPV(A)): ', 'PWB(A) - PWC(A) =', str(final_nvp_a))
print('='*92)

for k in range (0, years):
  if final_amount_b == 0:
    final_amount_b = 0

for s in range (0, years):
  grad += gradient_b
  year_b += year__b

  print('Accumulated profit for the following year (B) = (',final_amount_b,'+((',annual_income_b,'+',grad-gradient_b,') / (', 1, '+', interest,')**', year_b,'))')

  final_amount_b = (final_amount_b + ((annual_income_b - gradient_b + grad)/(1 + interest)**year_b))

  final_pwb_b = final_amount_b

print('-'*92)

print('Percent worth of benefit (PWB(B)) :', final_pwb_b)

print('-'*92)

for l in range (0, years):
  if final_cost_b == 0:
    final_cost_b = 0

for t in range (0, years):
  grad_ += gradient_cost_b
  c_year_b += c_year__b

  print('Accumulated expenses for the following year (B) = (',final_cost_b,'+((',annual_cost_b,'+',grad_-gradient_cost_b,') / (', 1, '+', interest,')**', c_year_b,'))')

  final_cost_b = (final_cost_b + ((annual_cost_b - gradient_cost_b + grad_)/(1 + interest)**c_year_b))

print('Final cost B =', final_cost_b)

final_pwc_b = final_cost_b + principal_b

print('-'*92)

print('Percent worth of cost (PWC(B)) :', 'Final cost B + Principal B =', final_pwc_b)

print('-'*92)

final_nvp_b = final_pwb_b-final_pwc_b

print('Total net present value of B in', years, 'years (NPV(B)): ', 'PWB(B) - PWC(B) =', str(final_nvp_b))
print('='*92)

if final_nvp_a > final_nvp_b:
    efficiency = "Option A"
else:
    efficiency = "Option B"
print('Option of the highest efficiency : ',efficiency)
print('='*46)
print('Note : The results listed (especially if using G) may not be the same / close to the results of the compound interest table formula, because the accuracy of the reference values in the table is only 3 to 4 digits behind the comma')
