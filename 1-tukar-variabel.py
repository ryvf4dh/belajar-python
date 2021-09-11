print("******************************")
print('Penukaran Variabel di Python')
print("******************************")
a, b, c, d, e = 1, 2, 3, 4, 5
print('sebelum tukar')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
a, b, c, d, e = b, d, e, a, c
print('setelah tukar')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}') 
print("****************")
print('    Selesai     ')
print("****************")