# 1-100 arasında rastgele üretilecek sayıyı asagı yukarı ifadeleri ile buldurmaya çalısır.

# 100 üzerinden puanlama yapılır.Her soru 20 puan
# Hak bilgisi kullanıcıdan alınır ve her soru belirtilen can sayısı üzerinden hesaplanır


import random
sayi = random.randint(1,100)
print(sayi)
hak =5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin : '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}.defada bildiniz...')
        break
    elif sayi>tahmin:
        print('yukarı')
    else:
        print('aşağı')

    if hak == 0:
        print(f'hakkınız bitti.. Tutulan sayi : {sayi}')
        print('Oynadığınız için teşekkürler')
        print('Taner Egehan')