#tanda |,&,^,~ buat di binary
#tanda and,or,and,xor itu buat di boolean(true or false)
#OPERASI BITWISE YAITU BINARY DENGAN OPERASI 
# 1. OR (|)
# 2. AND (&)
# 3. XOR (^)
# 4. NOT (~)
# 5. SWIFT RIGHT (>>)
# 6.  SWIFT LEFT (<<)

print("\n====operasi or====")
a=9
b=7
c=a|b
print("nilai",a,"dibinerkan menjadi",format(a,'08b'))
print("nilai",b,"dibinerkan menjadi",format(b,'08b'))
print("==================")
print("menjadi",format(c,'08b'))

print("\n====operasi and====")
c=a&b
print("nilai",a,"dibinerkan menjadi",format(a,'08b'))
print("nilai",b,"dibinerkan menjadi",format(b,'08b'))
print("==================")
print("menjadi",format(c,'08b'))

print("\n====operasi xor====")
c=a^b
print("nilai",a,"dibinerkan menjadi",format(a,'08b'))
print("nilai",b,"dibinerkan menjadi",format(b,'08b'))
print("==================")
print("menjadi",format(c,'08b'))

print("\n====operasi not====")
c=~a
print("nilai",a,"dibinerkan menjadi",format(a,'08b'))
print("==================")
print("menjadi",format(c,'08b'))#dimirrorkan tapi bertambah 1 jadi 9 ke -10
#jadi kita memakai xor untuk membalikkan dari 0 ke 1 dan sebaliknya
d=0b00001001
e=0b11111111
hasil=d^e
print("\nhasilnya menjadi jika diubah dari 0 dan 1 yaitu",format(hasil,'08b'))

print("\n====operasi swift right====")
c=a>> 1
print("nilai",a,"dibinerkan menjadi",format(a,'08b'))
print("==================")
print("menjadi",format(c,'08b'))

print("\n====operasi swift left====")
c=a<< 2
print("nilai",a,"dibinerkan menjadi",format(a,'08b'))
print("==================")
print("menjadi",format(c,'08b'))