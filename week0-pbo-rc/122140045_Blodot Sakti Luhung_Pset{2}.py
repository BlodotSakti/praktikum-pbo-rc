grade = {}

n = int(input('Masukkan jumlah pasangan keys-values yang diinginkan:'))

for i in range(n):
    nama = input('Masukkan nama (keys) ke-{}: '.format(i+1))
    nilai = int(input('Masukkan nilai (values) {}: '.format(nama)))
    print('')
    grade[nama] = nilai

print('grade =', grade)
