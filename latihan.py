a=int(input('input angka:'))
b=[]
c=''
for i in str(a):
    b.append(i)
    
for o in range(len(b)):
    if b[o] == '1':
        b[o] = 'satu'
    elif b[o] == '2':
        b[o] = 'dua'
    elif b[o] == '3':
        b[o] = 'tiga'
    elif b[o] == '4':
        b[o] = 'empat'
    elif b[o] == '5':
        b[o] = 'lima'
    elif b[o] == '6':
        b[o] = 'enam'
    elif b[o] == '7':
        b[o] = 'tujuh'
    elif b[o] == '8':
        b[o] = 'delapan'
    elif b[o] == '9':
        b[o] = 'sembilan'
    elif b[o] == '0':
        b[o] = 'no'
        
for p in b:
    c+=str(p)
    
print(c)
        