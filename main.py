from fake_numberphone_id import indosat, telepon, layanan_operator


nomor = telepon(indosat.EMPAT_BELAS)
ll = layanan_operator(indosat.EMPAT_BELAS)

if __name__ == '__main__':
    print(nomor)
    print(ll)
