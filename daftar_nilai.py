from view.input_nilai import *

dataMhs = {}

def tambah_data():
    global dataMhs
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUas()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print("\nData Ditambahkan!")
    return dataMhs

def ubah_data():
    nama = input("Input Nama: ")
    if nama in dataMhs.keys():
        nim           = input_nim()
        nilaiTugas    = input_nilaiTugas()
        nilaiUts      = input_nilaiUts()
        nilaiUas      = input_nilaiUas()
        nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dataMhs[nama]  = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Telah Di Ubah")
    else:
        print("Data tidak Ada")

def hapus_data():
    nama = input("Input Nama:  ")
    if nama in dataMhs.keys():
        del dataMhs[nama]
        print("Data",nama,"Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada".format(nama))