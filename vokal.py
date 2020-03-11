nama=input('naon weh bebas:')
vokal=['a','e','u','o']
namabaru=[]
kosong=''

for i in nama:
    namabaru.append(i)
    
for o in range(len(namabaru)):
    for p in vokal:
        if namabaru[o] == p:
            namabaru[o]='i'
            
for l in namabaru:
    kosong += l
    
print(kosong)