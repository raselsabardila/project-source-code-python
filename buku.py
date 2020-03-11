buku=[]

def showbuku():
    if len(buku) <=0:
        print("tidak ada buku yang tersedia!!")
    else:
        for i in range(len(buku)):
            print(i,".",buku[i])
        
def insert():
    namabuku=input("masukan judul buku:")
    buku.append(namabuku)
    
def edit():
    showbuku()
    nobuku=int(input("masukan no index buku:"))
    if nobuku > len(buku):
        print("no index tidak ada")
    else:
        bukubaru=input("masukan buku pengganti") 
        buku[nobuku]=bukubaru
        
def delete():
    showbuku()
    nobuku=int(input("masukan no index buku yang akan di hapus:"))
    if nobuku > len(buku):
        print("no index tidak ada")
    else:
       buku.remove(buku[nobuku])
       
def show():
    print("""
          ------menu------
          [1].list buku
          [2].insert buku
          [3].edit buku
          [4].delete buku
          [5].exit
          """)
    
    menu=int(input("pilih menu:"))
    if menu ==1:
        showbuku()
    elif menu ==2:
        insert()
    elif menu==3:
        edit()
    elif menu==4:
        delete()
    elif menu==5:
        exit()
    else:
        print("menu tidak ada")
        
while True:
    show()