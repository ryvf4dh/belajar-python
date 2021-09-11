print("*************************")
print("Fungsi for loop enumerate")
print("*************************")
kd_brg = ['A01', 'A02', 'A03']
nm_brg = ['Pensil', 'Penghapus', 'Penggaris']
for i, dt_kd_brg in enumerate(kd_brg):
    print(f'{dt_kd_brg}-->{nm_brg[i]}')