#fungsi pilihan
def choose(kode):
    if kode == 1:
        item = item1.upper()
    elif kode == 2:
        item = item2.upper()
    else:
        exit()
    print("memilih "+item)

#fungsi harga rumus PPN
def ppn(harga):
    ppn = harga * 0.1
    harga += ppn
    print(harga)

#main
item1 = "capucino"
item2 = "teh"
print("NIM : 20210801402\n"+
      "NAMA : Dzaka Luthfi Caussa")
print("Pilihan"+
        "\n1. "+item1+
        "\n2. "+item2+
        "\n3. Exit")
kode = int(input("masukkan pilihan : "))
choose(kode)
harga = int(input("masukkan harga : "))
ppn(harga)