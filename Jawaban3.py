#continue
for val in "bahasa":
    if val == "h":
        continue
        #break
    print(val)
    #output: b a a s a
print("selesai")

#break
for val in "bahasa":
    if val == "h":
        #continue
        break
    print(val)
    #output: b a
print("selesai")

"""
Terlihat jelas, dari output yang berbeda dapat disimpulkan. Jika menggunakan continue, maka akan melanjutkan ke perulangan selanjutnya. Jika menggunakan break, maka akan menghentikan perulangan.
"""