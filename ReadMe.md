# DİKKAT
## .py dosyalarında yol uzantılarını kendi kaydettiğiniz yol uzantılarında çalıştırın düzenleyin . 
## her bir dosya içerisinde belli kütüphaneler vardır bu kütüphaneleri indirin .


# Proje Açıklanması 

- ## 1.Adım (Var olan veri üzerinde çalışmak)
**Elimizde bulunan veri(DataMiningDataSet) üzerinde Sırasıyla knn *before isimli olan*  ve svm *before isimli olan* algoritmalarını çalıştırmak ve confisoun (karmaşıklık) matrixini bulmak.**

- ## 2.Adım (yer değiştir Nan ile)
**Var olan veri setimiz üzerinde manipüle ederek random şekilde yaş sutunun içerisinde Nan değerlerle yer değiştirme Nan yazmak *replaceWithNanValuesRandomFiftyValues.py* dosyası çalıştırıldı ve *DataMiningDataSetContainsNan* oluşturuldu.**

- ## 3.Adım (Nan yerine Mean hesapla yaz)
**Oluşturduğumuz *DataMiningDataSetContainsNan* dosyasını bir kez daha manipüle ederek Nan değerler yerine hesapladığımız ortalama (*Mean*) değer yazmak ve yeni son veri setimize ortaya çıkarmak *DataMiningDataSetContainsMeanInsteadOfNan* dosyasını oluşturduk.**

- ## 4.Adım (Mean yazdığımız dosya üzerinde çalışmak)
**Oluşturduğumuz *DataMiningDataSetContainsMeanInsteadOfNan* dosyasının üzerinde Sırasıyla knn *After isimli olan*  ve svm *After isimli olan*algoritmalarını çalıştırmak ve confisoun (karmaşıklık) matrixini bulmak .**


# ÇIKTILARIM
### Detaylı Çıktılar

#### KNN - Değişiklikten Önce-before
##### Confusion Matrix:
[[11  3  0]
 [ 2 72  1]
 [ 0  5 66]]
##### Accuracy: 0.93125

#### Svm  - Değişiklikten Önce-before
[[14  0  0]
 [ 1 74  0]
 [ 0  0 71]]
##### Accuracy: 0.99375

#### KNN - Değişiklikten sonra-after
[[11  2  0]
 [ 2 62  7]
 [ 0  2 74]]
##### Accuracy: 0.91875

#### Svm  - Değişiklikten sonra-after
[[13  0  0]
 [ 2 64  5]
 [ 0  0 76]]
##### Accuracy: 0.95625**