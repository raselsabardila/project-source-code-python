from random import randint

class money():
    
    def __init__(self,sisauang):
        self.sisauang=sisauang
        
    def sisa(self,pengeluaran):
        print('sisa uang anda = ',self.sisauang)
        print('pengeluaran anda = ',pengeluaran)
        self.sisauang=self.sisauang-pengeluaran
        print('sisa uang anda = ',self.sisauang)
        return self.sisauang
    
# uang=float(input('input sisa uang anda:'))
# beli=float(input('input pengeluaran:'))
# demo=money(uang)
# demo.sisa(beli)

class gajikaryawan():
    
    def __init__(self,nama,alamat,gaji_pokok):
        self.nama=nama
        self.alamat=alamat
        self.gaji_pokok=gaji_pokok
        self.tunjangan=0
        self.pajak=0
        self.gaji_bersih=0
        
    def tunjangan_karyawan(self):
        self.tunjangan=0.15*self.gaji_pokok
        return self.tunjangan
    
    def pajak_karyawan(self):
        self.pajak=0.075*self.gaji_pokok
        return self.pajak
    
    def gaji_bersih_karyawan(self):
        self.gaji_bersih=self.gaji_pokok+self.tunjangan-self.pajak
        return self.gaji_bersih
    
    def show(self):
        print('nama karyawan : ',self.nama)
        print('gaji pokok anda : ',self.gaji_pokok)
        self.tunjangan_karyawan()
        print('tunjangan anda : ',self.tunjangan)
        self.pajak_karyawan()
        print('pajak anda : ',self.pajak)
        self.gaji_bersih_karyawan()
        print('gaji bersih anda : ',self.gaji_bersih)
        
# nama=input('input nama anda : ')
# alamat=input('input alamat anda : ')
# gaji_pokok=float(input('input gaji pokok anda  : '))
# demo=gajikaryawan(nama,alamat,gaji_pokok)
# demo.show()

class tebakan():
    
    def __init__(self,tebakan):
        self.tebakan=tebakan
        self.angka=randint(1,10)
        
    def nebak(self):
        print('tebakan kamu : ',self.tebakan)
        
        if self.tebakan == self.angka:
            print('selamat tebakan kamu benar')
        else:
            print('maaf tebakan kamu salah')
            
# value=int(input('input angka tebakan anda dari 1-10 : '))

# demo=tebakan(value)
# demo.nebak()

class usia():
    
    def __init__(self,ttl):
        self.ttl=ttl
        self.umur=0
        
    def menghitung(self):
        self.umur=2019-self.ttl
        print('umur kamu sekitar',self.umur,'tahun')
        return self.umur
    
# age=int(input('input tahun lahir anda : '))
# demo=usia(age)
# demo.menghitung()

