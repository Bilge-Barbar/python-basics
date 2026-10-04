sözlük={"a":0,
        "b":1,
        "c":2,
        "d":3}
# keys()sözlüğün sadece anahtarlarını almak için kullanılır.
print(sözlük.keys()) 
print(list(sözlük.keys()))  # elde edilen çıktıyı başka veri tiplerine dönüştürebiliriz.
print("*".join(sözlük.keys()))

print("------------------------------------------")

# values() sözlüğün tüm değerlerini çıktı olarak verir.
print(sözlük.values()) # elde edilen çıktıyı başka veri tiplerine dönüştürebiliriz.
print(tuple(sözlük.values()))
print("".join([str(i)for i in sözlük.values()]))  # sözlük içindeki veriler int olduğu için önce str'e dönüştürürüz.

print("-------------------------------------------")

# items() hem anahtarı hem değeri aynı anda alırız.
print(sözlük.items())
for anahtar, değer in sözlük.items():
    print("{} = {}".format(anahtar,değer))

print("-------------------------------------------")

# get() iki değer alır, ilki sorgulamak istediğiniz öğe diğeri bu öğe sözlükte yoksa hangi mesajın gösterileceği.
#soru=input("a ile d arası bir harf girin: ")
#print(sözlük.get(soru,"a ile d arası bir harf!"))

print("-------------------------------------------")

# clear() sözlüklerin içeriğini siler.
# copy() varolan bir sözlüğü kopyalar.
# fromkeys()yeni sözlük oluşturur.
elemanlar="ben","sen","o"
adresler=dict.fromkeys(elemanlar,"kadıköy")
print(adresler)

print("-------------------------------------------")

# pop() sıra numarası girilen öğeyi siler ve silinen öğeyi ekrana basar.
                # argumansız kullanılamaz.
print(adresler.pop("o"))
print(adresler.pop("biz","silinecek öge yok!")) #silinmek isteyen oge sözlükte yoksa diye hata mesajı tanımladık.

# popitem() sözlükten rastgele öğe siler.
# setdefault() sözlük içinde arama yapar ve aradığımız anahtar sözlükte yoksa, metot içinde belirtilen özellikleri
                    #taşıyanyeni bir anahtar değer çifti oluşturur.
print(sözlük.setdefault("e",5))
print(sözlük.setdefault("a",1))

print("-------------------------------------------")

# update() sözlükleri yeni verilerle günceller.
yeni_sözlük={"a":1,
             "b":2,
             "e":10}
sözlük.update(yeni_sözlük)
print(sözlük)