# Run it only with Jupyter notebook or other Python IDE
# Please only input numbers, and if it reaches thousands and above do not use dots
# Continue to do the previous step as requested until it's finished
# If there is a question that is not needed, please fill in the zero '0'
# Especially for G (be it G1 or G2) if it decreases, give minus '-' in front of nominal
# Doesn't yet support calculation except F against A, G, and P

print('-'*46)
print('COMPOUND INTEREST CALCULATOR')
print('-'*46)
print('How many years will you invest? (n)')
years = int(input('Enter the time period in years : '))

print('How much balance do you have on your account now? (P)')
principal = float(input('Enter the balance : '))

print('How much is the nominal deposit that you will invest each year? (A)')
annual_invest = float(input('Enter the annual deposit : '))

print('How much is your annual savings deposit increased / decreased? (G)')
gradient = float(input('Enter the increase / decrease of the deposit : '))

print('What percentage of the estimated interest will you earn each year? (i)')
interest = float(input('Enter the estimated interest (without percent)  : '))
interest = interest/100

print('-'*46)

final_amount = 0
grad = 0
year = 0
year_ = 1

for j in range (0, years):
  if final_amount == 0:
    final_amount = principal

for y in range (0, years):
  year += year_
  grad += gradient

  print('Accumulated in the following year  = (',final_amount,'+((',annual_invest,'+',grad-gradient,') / (', 1, '+', interest,')**', year,'))')

  final_amount = (final_amount + ((annual_invest - gradient + grad)/(1 + interest)** year))

print('-'*92)

print('The nominal amount you earn in', years, 'years is =', final_amount)

print('-'*92)
print('Note : The results listed (especially if using G) may not be the same / close to the results of the compound interest table formula, because the accuracy of the reference values in the table is only 3 to 4 digits behind the comma' )
