print("**********")
print("Fungsi map")
print("**********")
def kalidua(x):
    return x * 2 #fungsi menghasilkan setiap nilai di dalam list dikali 2

list1 = [7, 8, 9]
list3 = list(map(kalidua, list1))
print(f'list 1={list1}')
print(f'list 2={list3}')
