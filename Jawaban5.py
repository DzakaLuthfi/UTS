def konversi(h, m, s):
    if s > 60:
        m += s // 60
        s = s % 60
    elif m > 60:
        h += m // 60
        m = m % 60
    elif h > 24:
        h = h % 24
        print("Output lebih dari 24 jam")
        exit()
    elif h < 0 or m < 0 or s < 0:
        print("input tidak valid")
        exit()
    print(f'{h}:{m}:{s}')

jam = int(input("masukkan jam: "))
menit = int(input("masukkan menit: "))
detik = int(input("masukkan detik: "))
konversi(jam, menit, detik)
