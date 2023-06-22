
#-----------------Task Mad Libs---------------
# print('--------This Is Mad Libs--------\n')
# benda = input('Beri saya kata benda: ')
# kerja = input('Beri saya kata kerja: ')
# sifat = input('Beri saya kata sifat: ')
# waktu = input('Beri saya kata keterangan waktu: ')

# print('\nCerita Mad Libs')
# print('Pada suatu ' + waktu + ', saya ' + kerja + ' di ' + benda + ' yang ' + sifat + ' dan sedang ' + kerja + ' sarapan.')
# print('Dalam contoh tersebut,' + benda + ' adalah kata benda, ' + kerja + ' adalah kata kerja,')
# print(sifat + ' adalah kata sifat,dan ' + waktu + ' adalah kata keterangan waktu. ')
# --------------------------------------------------Done-----------------------------------------



#========================FUNCTION=====================
# ----------------------------------------------------
def sapa(nama):
    print("Halo,", nama)

sapa("Zikra")  # Memanggil fungsi sapa() dengan argumen "John"

def charge(a, b):
    hasil = a + b
    return hasil
x = 5
y = 9
total = charge(x, y)  # Memanggil fungsi tambah() dengan argumen x dan y
print(total)  # Output: 14

def status(nama, usia, alamat, kerja):
    nama = input('Nama Kamu : ')
    print('Kamu adalah ',nama)
    print('Nama kamu : ', nama)
    print('Usia kamu : ',usia)
    print('Alamat kamu : ',alamat)
    print('Pekerjaan kamu : ', kerja)

status('Zikra', '23', 'Bekasi', 'Programmer')

def sapa(nama):
    nama = input("Masukkan nama Anda: ")
    print("Halo, " + nama + "! Selamat datang.")
sapa('Your Name')

