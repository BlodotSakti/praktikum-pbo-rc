class Robot:
  
    def __init__(self, nama, darah, serangan):
        self.nama = nama
        self.darah = darah
        self.serangan = serangan

    def nyerang(self, musuh, pilihan_robot, pilihan_musuh):
        print(f'{self.nama} menyerang {self.serangan} keruskaan ke {musuh.nama}')
        if pilihan_robot == 2 or pilihan_musuh == 2:
            pass
        else:
            musuh.darah += self.serangan
            if musuh.darah <= 0:
                print(f'{musuh.nama} mati')

    def bertahan(self, musuh, pilihan_robot, pilihan_musuh): 
        print(f'{self.nama} berhasil defense')
        self.darah -= musuh.serangan/2
        if self.darah <= 0:
            print(f'{self.nama} mati')

    def hidup(self):
        return self.darah > 0

class Game:

    def __init__(self, robot, musuh):
        self.robot = robot
        self.musuh = musuh
        self.ronde = 0

    def play(self): 
        print('     Perturan Pertandingan\n')
        print('# Opsi Attack digunakan untuk menyerang lawan dengan power serangan saat ini')
        print('# Opsi Defense berfungsi untuk menahan serangan lawan sebesar 50% power serangan saat ini')
        print('# Opsi Give Up digunakan untuk pemain menyerah dari pertandingan')
        print('# Opsi Regen Darah berfungsi untuk menambahkan darah sebesar 15% dari darah terbaru')
        print('# Opsi Tambah Attack berfungsi untuk menambahkan Attack sebesar 10% dari Attack saat ini')

        while self.robot.hidup() and self.musuh.hidup():

            self.ronde += 1
            print(f"\n     Round {self.ronde}")
            print(f'\n{self.robot.nama} vs {self.musuh.nama}')
            print(f'{self.robot.nama} darah: {self.robot.darah}; kekuatan serangan: {self.robot.serangan}')
            print(f'{self.musuh.nama} darah: {self.musuh.darah}; kekuatan serangan: {self.musuh.serangan}')

            print(f'\n1. Attack      2. Defense      3. Give Up      4. Regen Darah      5. Tambah Attack')
            pilihan_robot = int(input(f'{self.robot.nama}, memilih opsi:'))
            print(f'\n1. Attack      2. Defense      3. Give Up      4. Reegn Darah      5. Tambah Attack')
            pilihan_musuh = int(input(f'{self.musuh.nama}, memilih opsi:'))
            print('')
            
            if pilihan_robot == 3 and pilihan_musuh == 3:
                print(f'Pertandingan seri, {self.robot.nama} dan {self.musuh.nama} menyerah')
                break
            
            if pilihan_robot == 2 and pilihan_musuh == 2:
                print(f'Keduanya menggunakan defense')

            else:
                if pilihan_robot == 1:
                    self.robot.nyerang(self.musuh, pilihan_robot, pilihan_musuh)
                elif pilihan_robot == 2:
                    self.robot.bertahan(self.musuh, pilihan_robot, pilihan_musuh)
                elif pilihan_robot == 3:
                    print(f'{self.robot.nama} menyerah')
                    print(f'{self.musuh.nama} Win The Game!!')
                    break
                elif pilihan_robot == 4:
                    self.robot.darah += (15/100) * self.robot.darah
                    print(f'{self.robot.nama} menambah darah')
                elif pilihan_robot == 5:
                    self.robot.serangan += (10/100) *self.robot.serangan
                    print(f'{self.robot.nama} menambahkan serangan')
                else:
                    print('Pilihan tidak valid')

                if pilihan_musuh == 1:
                    self.musuh.nyerang(self.robot, pilihan_robot, pilihan_musuh)
                elif pilihan_musuh == 2:
                    self.musuh.bertahan(self.robot, pilihan_robot, pilihan_musuh)
                elif pilihan_musuh == 3:
                    print(f'{self.musuh.nama} menyerah')
                    print(f'{self.robot.nama} Win The Game!!')
                    break  
                elif pilihan_musuh == 4:
                    self.musuh.darah += (15/100) * self.musuh.darah
                    print(f'{self.musuh.nama} menambah darah')
                elif pilihan_musuh == 5:
                    self.musuh.serangan += (10/100) * self.musuh.serangan
                    print(f'{self.musuh.nama} menambah serangan')
                else:
                    print('Pilihan tidak valid')

robot = Robot('Lesley', 150, 40)
musuh = Robot('Kufra', 200, 20)
game = Game(robot, musuh)
game.play()
