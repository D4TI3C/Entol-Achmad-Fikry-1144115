import time

print("Hitunglah ( a * b ) + ( c / d )")
print("=====================")
a = raw_input("Masukkan nilai a : ")
b = raw_input("Masukkan nilai b : ")
c = raw_input("Masukkan nilai c : ")
d = raw_input("Masukkan nilai d : ")
print("=====================")

t1 = time.time()

if a == 'hiji':
        a=1
elif a == 'dua':
        a=2
elif a == 'tilu':
        a=3
elif a == 'opat':
        a=4
elif a == 'lima':
        a=5
elif a == 'genep':
        a=6
elif a == 'tujuh':
        a=7
elif a == 'dalapan':
        a=8
elif a == 'salapan':
        a=9
else :
        a=0

if b == 'hiji':
        b=1
elif b == 'dua':
        b=2
elif b == 'tilu':
        b=3
elif b == 'opat':
        b=4
elif b == 'lima':
        b=5
elif b == 'genep':
        b=6
elif b == 'tujuh':
        b=7
elif b == 'dalapan':
        b=8
elif b == 'salapan':
        b=9
else :
        b=0

if c == 'hiji':
        c=1
elif c == 'dua':
        c=2
elif c == 'tilu':
        c=3
elif c == 'opat':
        c=4
elif c == 'lima':
        c=5
elif c == 'genep':
        c=6
elif c == 'tujuh':
        c=7
elif c == 'dalapan':
        c=8
elif c == 'salapan':
        c=9
else :
        c=0

if d == 'hiji':
        d=1
elif d == 'dua':
        d=2
elif d == 'tilu':
        d=3
elif d == 'opat':
        d=4
elif d == 'lima':
        d=5
elif d == 'genep':
        d=6
elif d == 'tujuh':
        d=7
elif d == 'dalapan':
        d=8
elif d == 'salapan':
        d=9
else :
        d=0


hasil = float((float(a)*float(b))+(float(c)/float(d)))
print 'Hasil : (',a,'*',b,') + (',c,'/',d,') = ', hasil

t2 = time.time()
time =  t2 - t1
print 'Durasi Waktu : %s Detik'% time