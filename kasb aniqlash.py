savollar = [
    "1.O'qituvchi sifatida talabalar bilan qanday o'zaro aloqani o'rnatmoqchsiz \nA)O'z fikrlarimni muloqot qilish \nB)Ular bilan do'stona munosabatlar o'rnatish \nC)Yagona yondashuvni qo'llash\n",
    "2.Iytiy sohasida kasbiy rivojlanish imkoniyatlaringi qanday\nA) Yangi texnologiyalarni o'rganish \nB) Yaqin do'stlarimdan yordam olish\nC)O'zimni izolyatsiyalash\n",
    "3.Bank ishida muvaffaqiyat qozonish uchun qanday kasbiy etikaga amal qilishim kerak\nA) Mijozlar sotqinligini anglash\nB) Yaqin do'stlarimdan yordam olish\nC) Har qanday sharoitda ishlash\n",
    "4.O'qituvchilikni tanlaganingizda, qaysi darsni o'qitishni xohlayiz\nA)Matematikadan\nB)Tarixdan\nC)San'atdan \n",
    "5.Qanday jamoalarni yaratish va ular bilan ishlashni rejalashtirmoqdasi?\nA) E'tiborni jamlash\nB)O'z fikrlarimga ishonc\nC) Faoliyatda o'zaro munosabatlarni o'rnatish\n",
    "6.Dasturchi sifatida o'z nazoratni va muammolarni hal qilish qobiliyatlaringiz qanday?\nA)O'zimni muammolarga duch keltirish\nB) Keng qamrovli misollarni tahlil qilish\nC) Boshqalardan maslahatlarga murojaat qilish\n",
    "7.O'qituvchilikda talabalar bilan muloqot qilishda qanday rol o'ynaydi?\nA) Sen o'z fikrlaringni aytgandan keyin\nB) Talabalar o'zlarini erkin his qilishlari kerak\nC)Har bir o'quvchini alohida ko'rmaslik\n",
    "8.E'tiborni jamlash qanday foydali?\nA)Mijozlar kelganda maslahatlar olish\nB) Ishda faoliyatni yaxshilash\nC) Yakkalikni rivojlantirish\n",
    "9.Bankda ishlash uchun qanday qobiliyatlar muhim hisoblanadi?\nA) Mijozlarga xizmat ko'rsatish\nB)Shaxsiy qobiliyatlar\nC)Tezda yechim topish\n",
    "10.Yangi texnologiyalarni darslarda qanday ishlatmoqchiiz\nA) An'anaviy usullar bilan birga\nB) Har bir darsda yangi texnologiyalarni kiritish\nC) Hech qanday yangilik kiritmaslik\n",
]

a_ni_hiaoblovchi = 0
b_ni_hiaoblovchi = 0
c_ni_hiaoblovchi = 0

print("Kasbga yo'naltiruvchi savollarga xush kelibsiz!")

for question in savollar:
    javoblar = input(question)
    while javoblar.lower() not in ['a', 'b', 'c']:
        print("Iltimos, 'a', 'b' yoki 'c' dan birini tanlang.")
        javoblar = input(question)

    if javoblar.lower() == 'a':
        a_ni_hiaoblovchi += 1
    elif javoblar.lower() == 'b':
        b_ni_hiaoblovchi += 1
    elif javoblar.lower() == 'c':
        c_ni_hiaoblovchi += 1

if a_ni_hiaoblovchi > b_ni_hiaoblovchi and a_ni_hiaoblovchi > c_ni_hiaoblovchi:
    print("Siz ko'proq O'qituvchi kasbiga moyilsiz!")
    a1 = input("Sizga bu yo'nalishlar bo'yicha yordam kerakmi (Matematika, Ingliz tili, Rus tili)? ")
    if a1.lower() == "ha":
        print("Siz qaysi yo'nalishda ishlamoqchisiz?")
    elif a1.lower() == "matematika":
        print("Pedagogik ta'lim: o'qitish usullari va matematik bilimlarni o'rganishingiz kerak.")
    elif a1.lower() == "ingliz tili":
        print("Grammatika, madaniyat va kontekst: bu yo'nalish bo'yicha kitoblarni tavsiya qilamiz.")
    elif a1.lower() == "rus tili":
        print("Davomiylik va har kuni mashqlar qilish kerak.")
    elif a1.lower() == "yo'q":
        print("Bizning dasturimizdan foydalanganingizdan hursandmiz!")

elif b_ni_hiaoblovchi > a_ni_hiaoblovchi and b_ni_hiaoblovchi > c_ni_hiaoblovchi:
    print("Siz ko'proq Dasturchi kasbiga moyilsiz!")
    a2 = input("Sizga bu yo'nalishlar bo'yicha yordam kerakmi (JavaScript, Python, C++)? ")
    if a2.lower() == "ha":
        print("Siz qaysi yo'nalishda ishlamoqchisiz?")
    elif a2.lower() == "javascript":
        print("Asosiy tushunchalarni o'rganing: ma'lumot turlari va loyihalar yarating.")
    elif a2.lower() == "python":
        print("Jamiyat va muloqotga e'tibor qarating, onlayn resurslardan foydalaning.")
    elif a2.lower() == "c++":
        print("Ma'lumotlar tuzilmalari va funksiyalarni chuqur o'rganing.")
    elif a2.lower() == "yo'q":
        print("Bizning dasturimizdan foydalanganingizdan hursandmiz!")

elif c_ni_hiaoblovchi > a_ni_hiaoblovchi and c_ni_hiaoblovchi > b_ni_hiaoblovchi:
    print("Siz ko'proq Bank xodimi kasbiga moyilsiz!")
    a3 = input("Sizga bu yo'nalishlar bo'yicha yordam kerakmi (Kassa, Nazorat bo'limi, Operator bo'limi)? ")
    if a3.lower() == "ha":
        print("Siz qaysi yo'nalishda ishlamoqchisiz?")
    elif a3.lower() == "kassa":
        print("Matematik bilimlar va mijozlar bilan muloqot qilishni o'rganing.")
    elif a3.lower() == "nazorat bo'limi":
        print("Psixologik bilimlar va bardoshlilikni rivojlantiring.")
    elif a3.lower() == "operator bo'limi":
        print("Bank tizimlari va moliyaviy axborotlarni o'rganing.")
