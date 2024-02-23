nama = input('masukkan nama anda : ')
nim = int(input('masukkan nim anda : '))
resolusi = input('masukkan resolusi anda : ')

data = 'Nama : ' + nama +'\nNim : '+ str(nim)+'\nResolusi tahun ini : '+ resolusi


with open('resolusi', 'w') as f:
    f.write(data)
