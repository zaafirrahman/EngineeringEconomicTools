# DEPRECIATION
# 6 METHOD OF INVESTMENT VALUE REDUCTION

print('-'*40)
print('DEPRECIATION')
print('Reduction of Investment Value')
print('-'*60)

choose = input('Metode Depresiasi (SLD, SOYD, DBD, DDBD, SF, UPD) : ')

if choose == 'SLD' :

  print('-'*40)
  print('STRAIGHT LINE DEPRECIATION (SLD)')
  print('-'*60)

  I = float(input('Masukkan biaya investasi (I) : '))
  L = float(input('Masukkan nilai sisa (L) : '))
  N = int(input('Masukkan masa pakai dalam tahun (N) : '))

  print('-'*60)

  n_dn = 0
  n_Dn = 0
  n_Bn = 0
  dn = 0
  Dn = 0

  for i in range (0, N) :
    n_dn += 1
    d = (I-L)/N
    print('Depresiasi pada tahun ke',n_dn,' : ',d)

  print('-'*60)

  for j in range (0, N) :
    n_Dn += 1
    n_Bn += 1

    if Dn == 0 :
      dn += 1

    Dn = Dn + (dn * d)
    print('Total depresiasi pada tahun ke',n_Dn,' : ',Dn)

    Bn = (I - Dn)
    print('Nilai buku pada tahun ke',n_Bn,' : ',Bn)

    print('-'*60)

elif choose == 'SOYD' :

  print('-'*40)
  print('SUM OF THE YEARS DIGIT (SOYD)')
  print('-'*60)

  I = float(input('Masukkan biaya investasi (I) : '))
  L = float(input('Masukkan nilai sisa (L) : '))
  N = int(input('Masukkan masa pakai dalam tahun (N) : '))

  print('-'*60)

  n_dn = 0
  n_Dn = 0
  n_Bn = 0
  Dn = 0

  s = (N*(N + 1))/2

  print('Bobot digit tahun (s) : ',s)

  print('-'*60)

  for i in range (0, N) :
    n_dn += 1
    n_Dn += 1
    n_Bn += 1

    d = ((N -(n_dn-1))/s) * (I-L)
    print('Depresiasi pada tahun ke',n_dn,' : ',d)

    Dn = Dn + d
    print('Total depresiasi pada tahun ke',n_Dn,' : ',Dn)

    Bn = (I - Dn)
    print('Nilai buku pada tahun ke',n_Bn,' : ',Bn)

    print('-'*60) 

elif choose == 'DBD' :

  print('-'*40)
  print('DECLINING BALANCE DEPRECIATION (DBD)')
  print('-'*60)

  I = float(input('Masukkan biaya investasi (I) : '))
  L = float(input('Masukkan nilai sisa (L) : '))
  N = int(input('Masukkan masa pakai dalam tahun (N) : '))

  print('-'*60)

  n_dn = 0
  n_Dn = 0
  n_Bn = 0
  Dn = 0

  f = 1 - (L/I)**(1/N)

  print('Laju penyusutan tetap (f) :',f)

  print('-'*60)

  for i in range (0, N) :
    n_dn += 1
    n_Dn += 1
    n_Bn += 1

    d = I * (1-f)**(n_dn-1) * f
    print('Depresiasi pada tahun ke',n_dn,' : ',d)

    Dn = Dn + d
    print('Total depresiasi pada tahun ke',n_Dn,' : ',Dn)

    Bn = (I - Dn)
    print('Nilai buku pada tahun ke',n_Bn,' : ',Bn)

    print('-'*60)  

elif choose == 'DDBD' :

  print('-'*40)
  print('DOUBLE DECLINING BALANCE DEPRECIATION (DDBD)')
  print('-'*60)

  I = float(input('Masukkan biaya investasi (I) : '))
  L = float(input('Masukkan nilai sisa (L) : '))
  N = int(input('Masukkan masa pakai dalam tahun (N) : '))
  SLD = float(input('Masukkan persentase SLD tanpa persen : '))/100

  print('-'*60)

  n_dn = 0
  n_Dn = 0
  n_Bn = 0
  Dn = 0

  d = (SLD/N)*I
  Dn = Dn + d
  Bn = I - Dn

  print('Depresiasi pada tahun ke 1 : ',d)
  print('Total depresiasi pada tahun ke 1 : ',Dn)
  print('Nilai buku pada tahun ke 1 : ',Bn)

  print('-'*60)

  for i in range (1, N) :
    n_dn += 1
    n_Dn += 1
    n_Bn += 1

    d = (SLD/N)*Bn
    print('Depresiasi pada tahun ke',n_dn,' : ',d)

    Dn = Dn + d
    print('Total depresiasi pada tahun ke',n_Dn,' : ',Dn)

    Bn = (I - Dn)
    print('Nilai buku pada tahun ke',n_Bn,' : ',Bn)

    print('-'*60)  

elif choose == 'SF' :

  print('-'*40)
  print('SINKING FUND (SF)')
  print('-'*60)

  I = float(input('Masukkan biaya investasi (I) : '))
  L = float(input('Masukkan nilai sisa (L) : '))
  N = int(input('Masukkan masa pakai dalam tahun (N) : '))
  i = float(input('Masukkan suku bunga tanpa persen (i) : '))/100

  print('-'*60)

  n_dn = 0
  n_Dn = 0
  n_Bn = 0
  Dn = 0

  a = (I-L)*(i/((1+i)**N-1))
  print('Nilai tahunan (A) : ', a)

  print('-'*60)

  for j in range (0, N) :
    n_dn += 1
    n_Dn += 1
    n_Bn += 1

    d = a*(1+i)**(n_dn-1)
    print('Depresiasi pada tahun ke',n_dn,' : ',d)

    Dn = Dn + d
    print('Total depresiasi pada tahun ke',n_Dn,' : ',Dn)

    Bn = (I - Dn)
    print('Nilai buku pada tahun ke',n_Bn,' : ',Bn)

    print('-'*60)  

elif choose == 'UPD' :

  print('-'*40)
  print('UNIT OF PRODUCTION DEPRECIATION (UPD)')
  print('-'*60)

  I = float(input('Masukkan biaya investasi (I) : '))
  L = float(input('Masukkan nilai sisa (L) : '))
  UN = float(input('Masukkan jumlah produksi keseluruhan (UN) : '))
  N = int(input('Masukkan masa pakai dalam tahun (N) : '))

  n = 0

  print('-'*60)

  for i in range (N):

    Un = float(input('Masukkan jumlah produksi tahun ke-{} : '.format(i+1)))
    n += Un
    d = (n/UN) * (I-L)

    print('Total produksi tahun ke-{} : {}'.format(i+1, n))
    print('Total depresiasi tahun ke-{} : {}'.format(i+1, d))

    print('-'*60)

else :
    print('-'*60)
    print('Salah input metode')
    print('-'*60)



