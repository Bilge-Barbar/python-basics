#                   LİSTELERİN VE DEMETLERİN METOTLARI
#   Listelerin Metotları
print(dir(list))

print("______________________________")

print([i for i in dir(list) if not "_" in i])

# append() (eklemek,ilave etmek, iliştirmek.) Öğe eklemek için kullanılır.
liste=["elma","armut","muz"]
liste.append("erik") #append() metodu tek parametre alır.
for i in ["karpuz","kavun","çilek"]:
    liste.append(i)
print(liste)

# kullanıcının girdiği bütün sayıları çarpan program:

kontrol=[]
sonuç=1

while True:
    sayı=input("Sayı(hesaplamak için q):")
    if sayı=="q":
        break
    kontrol.append(sayı)
    sonuç*=int(sayı)
if len(kontrol)<2:
    print("yeterli sayıda değer girmediniz!")
else:
    print(sonuç)

# extend() (genişlemek,yaymak)
li1=[1,2,3]
li2=[4,5,6]
li1.extend(li2)
print(li1)

# insert() (yerleştirmek)
tohum=["pirinç","fıstık","badem"]
tohum.insert(1,"çekirdek")
print(tohum)

# remove() listeden öğe siler.
tohum.remove("badem")
print(tohum)

# reverse() tersten yazdırır.
print(list(reversed(tohum)))
tohum.reverse()
print(tohum)


# pop() listeden öğe siler.
# remove metodundan farkı silinen öğe ekrana basar.
tohum.pop(0)
print(tohum)

# sort() alfabetik ya da numeritrik olarak sıralar.
sayılar=[8,7,0,5,2,6,9,4,1,3]
sayılar.sort()
print(sayılar)
sayılar.sort(reverse=True) # tersten gidiyor. reverse sort modülünün parametresidir.
print(sayılar)

# index() konum belirtir.
# count() öğenin o veri tipi içinde kaç kez geçtiğini söyler.
# copy() listeleri kopyalar.
# clear() listenin içeriğini siler.

#   Demetlerin Metotları
print(dir(tuple))

# index() konum söyler.
# count() öğenin veri tipi içinde kaç kez geçtiğini söyler.