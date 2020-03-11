class toko_es():
    
    def __init__(self):
        self.pelanggan=''
        self.pilihan=''
        self.jumlah=0
        self.harga=0
        self.total=0
        self.potongan=0
        self.totalkeseluruhan=0
        self.uang_bayar=0
        self.kembalian=0
        self.namaes=''
        
    def kasir(self):
        print('       Tukang es krim       ')
        print('============================')
        self.pelanggan=input("nama pembeli : ")
        print('pilih es krim yang tersedia : ')
        print('[A1] -- Es krim coklat')
        print('[A2] -- Es krim vanila')
        print('[A3] -- Es krim stoberi')
        self.pilihan=input('Es krim yang dipilih : ')
        self.jumlah=int(input('jumlah beli : '))
        
    def hargaes(self):
        if self.pilihan == 'A1':
            self.harga=15000
            self.namaes='Es krim coklat'
        elif self.pilihan == 'A2':
            self.harga=20000
            self.namaes='Es krim vanila'
        elif self.pilihan == 'A3':
            self.harga=25000
            self.namaes='Es krim stoberi'
            
    def totalharga(self):
        self.total=self.harga*self.jumlah
        
    def diskon(self):
        if self.total >= 40000 and self.total < 50000:
            self.potongan=self.total*5/100
        elif self.total > 50000:
            self.potongan=self.total*10/100
            
    def totalkeseluruhanharga(self):
        self.totalkeseluruhan=self.total-self.potongan
        
    def bayar(self):
        self.kembalian=self.uang_bayar-self.totalkeseluruhan
    
    def proses(self):
        print('='*30)
        print('     struk pembayaran     ')
        print('='*30)
        print('nama pembeli : ',self.pelanggan)
        self.hargaes()
        print('nama es krim : ',self.namaes)
        print('harga : ',self.harga)
        print('jumlah : ',self.jumlah)
        self.totalharga()
        print('total : ',self.total)
        self.diskon()
        print('potongan : ',int(self.potongan))
        print('='*30)
        self.totalkeseluruhanharga()
        print('total keseluruhan : ',int(self.totalkeseluruhan))
        self.uang_bayar=int(input('uang bayar : '))
        self.bayar()
        print('kembalian : ',self.kembalian)
        
rebuy=True

while rebuy:
    demo=toko_es()
    demo.kasir()
    demo.proses()
    
    tanya=input('ingin membeli es lagi?[y/t] : ')
    if tanya == 'y' or tanya == 'Y':
        rebuy=True
    else:
        rebuy=False
        print('terima kasih telah membeli di toko kami')