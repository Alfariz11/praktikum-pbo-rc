jumlah_data = int(input('masukkan banyak data yang ingin dimasukkan : '))

dictionary_student ={}

for i in range(jumlah_data):
    nama = input('masukkan nama siswa/i : ')
    nilai = int(input('masukkan nilai siswa/i : '))
    dictionary_student.update({nama:nilai})

print(dictionary_student)