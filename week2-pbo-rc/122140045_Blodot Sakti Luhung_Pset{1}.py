import random

class Ayah:
    def __init__(self, golongan_darah):
        self.golongan_darah = golongan_darah

class Ibu:
    def __init__(self, golongan_darah):
        self.golongan_darah = golongan_darah

class Anak(Ayah, Ibu):
    def __init__(self, ayah, ibu):
        self.ayah = ayah
        self.ibu = ibu
        super().__init__(ayah.golongan_darah) 
        self.golongan_darah_ibu = ibu.golongan_darah

    def nyari_goldar_anak(self):
        alel = [self.ayah.golongan_darah, self.golongan_darah_ibu]
      
        alel_anak = random.choice(alel)
        print(f'alel anaknya adalah {alel_anak}')
      
        if alel_anak == 'AA':
            print('Golongan darah anaknya A')
        elif alel_anak == 'AO' or alel_anak == 'OA':
            print('Golongan darah anaknya A')
        elif alel_anak == 'AB' or alel_anak == 'BA':
            print('Golongan darah anaknya AB')
        elif alel_anak == 'BB':
            print('Golongan darah anaknya B')
        elif alel_anak == 'BO' or alel_anak == 'OB':
            print('Golongan darah anaknya B')
        elif alel_anak == 'OO':
            print('Golongan darah anaknya O')
      

print('Contoh Alel = AA, AO, AB, BB, BO, OO')
golongan_darah_ayah = input("Masukkan alel Ayah: ").upper()
golongan_darah_ibu = input("Masukkan alel Ibu: ").upper()

ayah = Ayah(golongan_darah_ayah)
ibu = Ibu(golongan_darah_ibu)

anak = Anak(ayah, ibu)
anak.nyari_goldar_anak()


