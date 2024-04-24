import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.boxlogin = tk.Tk()
        self.boxlogin.title('Login')
        self.boxlogin.geometry('300x200')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.boxlogin, text = 'Username:').pack()
        tk.Entry(self.boxlogin, textvariable=self.username).pack()

        tk.Label(self.boxlogin, text = 'Password:').pack()
        tk.Entry(self.boxlogin, textvariable = self.password, show='*').pack()

        tk.Button(self.boxlogin, text = 'Login', command = self.untuk_cek).pack()
        tk.Button(self.boxlogin, text = 'Register', command = self.buka_register).pack()

        self.users = {'Hallad': 'akuGanteng', 'Kaylaat': 'AkuJago'}

    def untuk_cek(self):
        if self.username.get() in self.users and self.password.get() == self.users[self.username.get()]:
            messagebox.showinfo('Successful', 'Alhamdulillah Anda Berhasil Login')
        else:
            messagebox.showerror('Error', 'Salahh Cuyy Usernamenya atau PWnya')

    def buka_register(self):
        self.boxlogin.withdraw()
        self.jendela_register = Register(self.boxlogin, self.users)
        self.jendela_register.jendela.protocol("WM_DELETE_WINDOW", lambda: self.tutup_register())
        self.jendela_register.mainloop()

    def tutup_register(self):
        self.boxlogin.deiconify()

    def run(self):
        self.boxlogin.mainloop()

class Register:
    def __init__(self,master, users):
        self.jendela = tk.Toplevel()
        self.jendela.title('Register')
        self.jendela.geometry('300x300')

        self.users = users
        self.username_register = tk.StringVar()
        self.password_register = tk.StringVar()
        self.cek_password = tk.StringVar()

        tk.Label(self.jendela, text = 'Username:').pack()
        tk.Entry(self.jendela, textvariable=self.username_register).pack()

        tk.Label(self.jendela, text = 'Password:').pack()
        tk.Entry(self.jendela, textvariable = self.password_register).pack()

        tk.Label(self.jendela, text = 'Confirm Password:').pack()
        tk.Entry(self.jendela, textvariable = self.cek_password).pack()

        tk.Button(self.jendela, text = 'Register', command = self.tombol_register).pack()

    def tombol_register(self):
        if self.password_register.get() == self.cek_password.get():
            if not self.ada_username(self.username_register.get()):
                self.users[self.username_register.get()] = self.password_register.get()
                messagebox.showinfo('Registrasi Berhasil', 'Anda berhasil registrasi akun')

            else:
                messagebox.showerror('Register Gagal', 'Username anda sudah digunakan')
        else:
            messagebox.showerror('Error', 'Tidak Sesuai')

    def ada_username(self, username):
        return username in self.users


login = Login()
login.run()
