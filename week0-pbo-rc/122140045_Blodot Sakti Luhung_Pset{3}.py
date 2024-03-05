file = open('Me.txt', 'w')

file.write('Nama : Blodot Sakti Luhung')
file.write('\nNIM : 122140045')
file.write('\nResolusi saya tahun ini: menyempurnakan ibadah wajib dan memperbanyak ibadah sunnah')

file.close()

baca_file = open('Me.txt', 'r')
print(baca_file.read())


# catatan saya
# w = write mode/ buat nulis dan bisa juga nimpah
# r = read only/ buat baca 
# a = appending mode/ nambah data di akhir baris
# r+ = baca dan nulis
