print("*******************")
print("Fungsi for loop zip")
print("*******************")
kd_brg = ['A01', 'A02', 'A03']
nm_brg = ['Pensil', 'Penghapus', 'Penggaris']
for dt_kd_brg, dt_nm_brg in zip(kd_brg, nm_brg):
    print(f'{dt_kd_brg}-->{dt_nm_brg}')