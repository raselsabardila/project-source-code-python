class leaderboard():
    rank=[]
    
    def __init__(self,nama,trophy):
        self.username=nama
        self.trophy=trophy
        leaderboard.rank.append([self.username,self.trophy])
        
    def sortir(self):
        no=1
        hasil=leaderboard.rank.sort()
        hasil2=leaderboard.rank.reverse()
        print("----leaderboard----")
        for i in leaderboard.rank:
            print(i)
            
ulang=True
index=1
while ulang:
    username=input("masukan name class:")
    name=input("masukan username game:")
    trophy=int(input("masukan jumlah trophy"))
    username=leaderboard(name,trophy)
    tanya=input("lagi?(y/t)")
    if tanya=="y" or tanya=="Y":
        ulang=True
        index+=1
    else:
        ulang=False
        
username.sortir()