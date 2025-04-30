# project.py

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: pembagian dengan nol!"
    return a / b

def tampilkan_menu():
    print("=== Kalkulator Sederhana ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

def kalkulator():
    tampilkan_menu()
    pilihan = input("Pilih operasi (1/2/3/4): ")

    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid!")
        return

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if pilihan == "1":
        hasil = tambah(angka1, angka2)
        operasi = " + "
    elif pilihan == "2":
        hasil = kurang(angka1, angka2)
        operasi = " - "
    elif pilihan == "3":
        hasil = kali(angka1, angka2)
        operasi = " * "
    elif pilihan == "4":
        hasil = bagi(angka1, angka2)
        operasi = " / "

    print(f"Hasil: {angka1}{operasi}{angka2} = {hasil}")

if __name__ == "__main__":
    kalkulator()
