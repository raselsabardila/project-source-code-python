class absen():
    daftarsiswa=[]
    
    def __init__(self,nama):
        self.nama=nama
        absen.daftarsiswa.append(nama)
        
    @classmethod
    def sortirabsen(cls):
        cls.daftarsiswa.sort()
        print("----daftar siswa----")
        for i in range(len(cls.daftarsiswa)):
            print("[{}]".format(i+1),cls.daftarsiswa[i])
            
ulang=True

while ulang:
    nameobject=input("input nama object:")
    nama=input("input nama anda:")
    nameobject=absen(nama)
    tanya=input("mau memasukan nama siswa algi?(y/t)")
    if tanya =="y" or tanya =="Y":
        ulang=True
    else:
        ulang=False
        
nameobject.sortirabsen()