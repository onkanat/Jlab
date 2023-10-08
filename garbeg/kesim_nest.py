# /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# /usr/local/bin/python3
# /usr/bin/python3
"""
Dosya Adı: kesim_nest.py
Yazar: Hakan KILIÇASLAN
Açıklama: T150 için kesilen malzeme durumunu gözetlemek.
Versiyon: 0.150.01
Tarih: 4 October 2023

<İsteğe Bağlı Ek Bilgi veya Notlar>

"""

# Kodunuz buraya gelecek

import math

# KESİLECEK Çapa göre testere bağlatmaya zorla.
# Testere listesine kesme verileride konabilir.

Testere = [[460, 60, 2.75],
           [360, 60, 2,75],
           [250, 60, 2,50]
          ]

uc_kes = 25        # Malzeme çaplarına göre sabit değerler konabilir.
ham_boy = 6000     # Ana kesim ekranından girilecek.
kesim_boy = 600    # Kesim parçası giriş ekranından alınacak.
kesim_adet = 10    # Kesim parçası giriş ekranından alınacak.
uc_kesim_varmi = True # Kesim parçası giriş ekranından alınacak.
testere_payi = 3   # Testere listesinden Alınacak.

# Kesim miktarını hesapla
kesilen_miktar = kesim_adet * (kesim_boy + testere_payi)

# Uç kesim varsa ekleyin
if uc_kesim_varmi:
    kesilen_miktar += uc_kes

# Kalan boyu hesapla
kalan_boy = ham_boy - kesilen_miktar

# Kesim taşı miktarını hesapla
kesim_talasi = kesim_adet * testere_payi

print("Kesilen Miktar:", kesilen_miktar)
print("Kalan Boy:", kalan_boy)
print("Kesim Talası:", kesim_talasi)

# Malzeme yetmezse uyarı ver
if kesilen_miktar > ham_boy:
    print("Malzeme Yetmez!!! Kalan Boy:", kalan_boy)
