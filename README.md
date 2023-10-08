# fake-number-id
Membuat validasi dengan memasukan angka ke formulir inputan tentunya memakan waktu yang tidak sedikit, karena itulah aku membuat pustakan ini untuk mempermudah validasi dan tentunya mempercepat pengembangan aplikasi.

## Instalasi
```
pip install fake-number-id
```
atau kamu bisa kunjungi situs resmi pypi
```
https://pypi.org/project/fake-number-id
```

## Pengujian
program untuk menguji apakah pustaka berjalan atau terjadi kutu program
```python
from fake_number_id import indosat, telepon, layanan_operator

nomor = telepon(indosat.EMPAT_BELAS)
ll = layanan_operator(indosat.EMPAT_BELAS)

if __name__ == '__main__':
    print(nomor)
    print(ll)
```

## Konstanta
Selain indosat juga terdapat beberapa operator di indonesia yang tersedia di pustaka ini
```
indosat
	EMPAT_BELAS
	LIMA_BELAS
	ENAM_BELAS
	LIMA_LIMA
	LIMA_ENAM
	LIMA_TUJUH
	LIMA_DELAPAN

xl
	TUJUH_BELAS
	DELAPAN_BELAS
	SEMBILAN_BELAS
	LIMA_SEMBILAN 
	TUJUH_DELAPAN
	TUJUH_TUJUH

axis
	TIGA_DELAPAN	
	TIGA_TUJUH
	TIGA_SATU
	TIGA_DUA


telkomsel
	DUA_BELAS
	TIGA_BELAS
	LIMA_DUA
	LIMA_TIGA
	DUA_SATU
	DUA_TIGA
	DUA_DUA
	LIMA_SATU


smartfren
	DELAPAN_SATU
	DELAPAN_DUA
	DELAPAN_TIGA
	DELAPAN_EMPAT
	DELAPAN_LIMA
	DELAPAN_ENAM
	DELAPAN_TUJUH
	DELAPAN_DELAPAN


three
	SEMBILAN_ENAM
	SEMBILAN_TUJUH
	SEMBILAN_DELAPAN
	SEMBILAN_SEMBILAN
	SEMBILAN_LIMA
```
## Telepon
fungsi **telepon(parameter)** membuat data telepon palsu berdasarkan parameter konstanta penyedia layanan\
contoh pengguan telepon(parameter) :
```python
palsu = telepon(axis.TIGA_DELAPAN)
print(palsu)
```

## Penyedia Layanan
fungsi **layanan_operator(parameter)** memberitahukan nama operator\
beserta nomor prefiksnya berdasarkan parameter konstanta penyedia layanan\
contoh pengguan layanan_operator(parameter) :
```python
palsu = layanan_operator(smartfren.DELAPAN_SATU)
print(palsu)
```







