
t= {1: "gisht", 2: "olma", 3: "chillak", 4: "qarg'a"}
q = {
    6: 'olti',7: "yetti", 8: "sakkiz", 9: "to'qqiz", 10: "o'n",
    11: "valet", 12: "dama", 13: "qirol", 14: "tuz"
}
N = int(input("Karta qiymatini kiriting (6 <= N <= 14): "))
M = int(input("Karta turini kiriting (1 <= M <= 4): "))

if 6 <= N <= 14 and 1 <= M <= 4:
    k_q = q.get(N, "Noma'lum qiymat")
    k_t = t.get(M, "Noma'lum tur")
    print(k_q,k_t)
else:
    print("Kiritilgan qiymatlar noto'g'ri!")
