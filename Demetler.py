#                                  DEMETLER(TUPLE)
# Normal parantez işaretleri ile tanımlanırlar.
# immutable (değiştirilemez) veri tipleridir.

demet=("buse","bilge",1,2344)  # ya da demet="buse,"bilge,1,2344
print(demet,type(demet))
# Demet oluşturmak için tuple() fonksiyonu da kullanılabilir.
print(tuple('asdfgh'))
# tuple() fonksiyonu kullanılarak başka veri tipleri demetlere dönüştürülebilir.
print(tuple(["ali","ayşe",1,2344]))
demet_değil=("Bilge")
demettir=("Bilge",)
print(type(demet_değil),type(demettir))

# Demetlerin öğelerine erişmek
print(demet[0])

# Python' da sadece aynı tür veri tipleri birleştirilebilir.
