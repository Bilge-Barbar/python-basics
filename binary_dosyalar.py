# Dosyalar iki farklı sınıfa ayrılır: ikili ve metin dosyaları:
# Metin dosyaları metin içerir, ikili dosyalar video,müzik,MS OWce vb. dosyalarıdır.

# PDF dosyalayından bilgi almak:
f=open("1_1.pdf","rb")
print(f.read(10))
# PDF belgelerinde ,o belgeler hakkında önemli bilgiler veren özel etiketler bulunur:
# /Creator -> Belgeyi oluşturan yazılım.
# /Producer -> Belgeyi PDF'ye çeviren yazılım.
# /Title -> Belgenin başlığı.
# /Author -> Belgenin yazarı.
# /Subject -> Belgenin konusu.
# /Keywords -> Belgenin anahtar kelimeleri.
# /CreationDate -> Belgenin oluşturulma zamanı.
# /ModDate -> Belgenin değiştirilme zamanı.

#okunan=f.read()
#print(producer_index=okunan.index(b"/Producter"))
# okunan[producer_index]
# chr(okunan[producer_index]) sayının hangi karaktere karşılık geldiğini görür.

# Resim dosyalarının türünü tespit etme:
# JPEG :
# Bir JPEG dosyasını ayırt edebilmek için ilgili dosyanın 7-10 arası baytlarının ne olduğuna bakmalıyız.
# Eğer bu aralıkta "JFIF" ya da "Exif" ifadelieri varsa dosya JPEG dosyasıdır.
# \x işaretleri sayıların 16'lı sayı olduğunu gösterir.

# PNG :
# PNG dosyalarını ayırt etmek için ilk 8 bayta bakmak yeterlidir.

# GIF :
# ilk 3 bayta bakmak yeterli olur.

# TIFF :
# ilk 2 bayt yeterli.

# BMP :
#ilk 2.

#for f in dosyalar:
 #   okunan =open(f,"rb").read(10)
  #  if okunan [6:11] in[b"JFIF",b"Exif"]:
   #     print("{} adlı dosya bir JPEG".format(f))
    #elif okunan [:8] ==b"\211PNG\r\n\032\n":
#        print("{} adlı dosya bir PNG".format(f))
 #   elif okunan [:3] ==b"GIF":
  #      print("{} adlı dosya bir GIF".format(f))
   # elif okunan [:2] in [b"IT",b"MM"]:
#        print("{} adlı dosya bir TIFF".format(f))
 #   elif okunan [:2] in [b"BM"]:
  #      print("{} adlı dosya bir BMP".format(f))
   # else :
    #    print("Türü bilinmeyen dosya: {}".format(f))