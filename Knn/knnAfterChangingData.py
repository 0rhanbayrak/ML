import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
import os

# Çalışma dizinini ayarla
os.chdir('C:\\Users\\Harun\\Desktop\\dataMiningMidtermProject')

# Veriyi yükle
data  = pd.read_csv('DataMiningDataSetContainsMeanInsteadOfNan.csv')

# Özellikler ve hedef değişken
X = data[['Cinsiyet', 'Yas', 'TahminiMaas']]
y = data['IngilizceBilme']

# Veriyi eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN modelini oluştur ve eğit
model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)

# Confusion Matrix çıktısını yazdır
print(conf_matrix)

print("Accuracy:", accuracy)

