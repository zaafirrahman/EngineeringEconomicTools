# INTERNAL RATE OF RETURN IDENTIFIER
# FIND INTEREST RATE WITH NPV (+) & (-) RESULTS QUICKLY
# The solution to avoid wasting time due to trial errors on paper

# PLEASE READ FIRST
 
# For cellphone users, please tap on this cell first
# Click the play button on the top left corner to Run
# When the program loads, enter the data as requested and then enter
# Please only input numbers, and if it reaches thousands and above do not use dots
# If there is a question that is not needed, please fill in the zero '0'
# Especially for G (both G1 and G2) if it decreases, it will be given a minus '-' in front of nominal
# In the interest input (i), enter several interest rates that you want to identify (-) and (+) from the NPV result
# Please enter one by one the interest rate (i) in a different column in each enter
# If MARR is known, it is better to look for an interest rate (i) that is close to MARR
# The NPV answer for each interest (i) input can be seen in the terminal at the bottom
# If the NPV (+) results, then increase the interest rate (i) until the NPV (-) result is found, and vice versa
# When finished, enter the number zero (0) in the next interest column
# Good luck ;)

import matplotlib.pyplot as plt

print('-'*46)
print('INTERNAL RATE OF RETURN IDENTIFIER')
print('-'*46)
 
n = int(input('Masukkan masa waktu dalam tahun (n) : '))
p = float(input('Masukkan nilai investasi (P) : '))
a1 = float(input('Masukkan laba tahunan (A1) : '))
g1 = float(input('Masukkan kenaikan / penurunan laba (G1) : '))
a2 = float(input('Masukkan biaya tahunan (A2) : '))
g2 = float(input('Masukkan kenaikan / penurunan biaya (G2) : '))
f = float(input('Masukkan nilai sisa (F) : '))
marr = float(input('Masukkan MARR tanpa persen (MARR) : '))/100
i = input('Masukkan suku bunga tanpa persen (i) atau 0 jika cukup : ')

g = cg = y = cy = 0

def npv (annual_income, gradient, grad, interest, year, future, 
         years, annual_cost, gradient_cost, c_grad, c_year, principal) :
  final_amount = 0
  final_cost = 0

  for income in range (years):
    grad += gradient
    year += 1
    final_amount = (final_amount + ((annual_income - gradient + grad)/(1 + interest)**year))
    final_pwb = final_amount + (future / (1 + interest)**(years))
 
  for cost in range (years):
    c_grad += gradient_cost
    c_year += 1
    final_cost = (final_cost + ((annual_cost - gradient_cost + c_grad)/(1 + interest)**c_year))
 
  final_pwc = final_cost + principal
  npv_amount = final_pwb - final_pwc
  return npv_amount 

def graph() :
  fig, ax = plt.subplots()
  ax.plot(I, limit, 'r-', I, NPV, 'bo-')
  ax.set(ylabel = 'Net Present Value', xlabel = 'Discount Rate')
  ax.set(title = 'Interpolation')
  ax.legend(['Limit','i1;IRR;i2'])
  ax.grid()
  plt.show()

while i != '0' :
    i = float(i)
    i = i/100
    print('-'*60)

    def npv_total() :
      npv_main = npv(a1,g1,g,i,y,f,n,a2,g2,cg,cy,p)
      return npv_main
    print('Jumlah keuntungan dalam', n, 'tahun (NPV): ', npv_total())
    print('-'*80)
    i = input('Masukkan suku bunga tanpa persen (i) atau 0 jika cukup : ')

print('-'*80)

i_min = float(input('\nMasukkan suku bunga dengan NPV (-) tanpa persen (i-) : '))/100
def npvmin() :
  npv_min = npv(a1,g1,g,i_min,y,f,n,a2,g2,cg,cy,p)
  return npv_min
npv_min = npvmin()
 
i_plus = float(input('Masukkan suku bunga dengan NPV (+) tanpa persen (i+) : '))/100
def npvplus() :
  npv_plus = npv(a1,g1,g,i_plus,y,f,n,a2,g2,cg,cy,p)
  return npv_plus
npv_plus = npvplus()

print('-'*80) 

if i_plus > i_min :
  interest1, interest2 = i_min, i_plus
  npv1, npv2 = npv_min, npv_plus
else :
  interest1, interest2 = i_plus, i_min
  npv1, npv2 = npv_plus, npv_min

def ror() :
  irr = interest1 + ((interest2 - interest1) * (npv1 / (npv1-npv2)))
  return irr
irr = ror()

print('Tingkat pengembalian modal internal (IRR) : ',irr*100,'%')
print('Tingkat pengembalian minimum yang dapat diterima (MARR) : ',marr*100,'%')

print('-'*80)

if irr > marr :
  print('Proyek layak dilaksanakan')
else :
  print('Proyek tidak layak dilaksanakan')

print('-'*46)

I = [interest1, irr, interest2]
NPV = [npv1, 0, npv2]
limit = (0,0,0)

graph()
