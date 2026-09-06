 # 1. تعريف المتغيرات
game = "كرة القدم"
players = 11

# 2. طباعة المتغيرات
print("اسم اللعبة:", game)
print("عدد اللاعبين:", players)

# النتيجة (المخرجات):
# اسم اللعبة: كرة القدم
# عدد اللاعبين: 11



game = "كرة القدم"
players = 11

print(f"عدد لاعبين {game} هو {players} لاعباً")

# النتيجة: عدد لاعبين كرة القدم هو 11 لاعباً


# حلقة تكرار عكسية
for i in range(2, -1, -1):
    print("العدد", i)

# النتيجة المخرجة:
# العدد 2
# العدد 1
# العدد 0


# كود التكرار لطباعة تسلسل أرقام
for i in range(3):

   print(i) 

# المخرجات (النتيجة):
# 0
# 1
# 2


# إنشاء قائمة والوصول للعنصر الأول
my_list = ["عصير", "قهوة", "شاي"]

print(my_list[0])

# النتيجة المخرجة:
# شاي


# كود التكرار لطباعة نص عدة مرات
for i in range(3):
    print("مرحبا")

# النتيجة المخرجة:
# مرحبا
# مرحبا
# مرحبا


# مشروع: قائمة المشاريع المستقبلية
projects = ["تطبيق ورد", "تحليل بيانات", "متجر إلكتروني"]

print("--- قائمة مشاريعي القادمة ---")
for project in projects:
    print(f"- مشروع: {project}")

# النتيجة:
# --- قائمة مشاريعي القادمة ---
# - مشروع: تطبيق ورد
# - مشروع: تحليل بيانات
# - مشروع: متجر إلكتروني


# مشروع: العد التنازلي
print("بدء العد التنازلي:")

for i in range(5, 0, -1):
    print(f"التبقي: {i} ثوانٍ")

print("انطلق! 🚀")

# النتيجة:
# بدء العد التنازلي:
# التبقي: 5 ثوانٍ
# التبقي: 4 ثوانٍ
# التبقي: 3 ثوانٍ
# التبقي: 2 ثوانٍ
# التبقي: 1 ثوانٍ
# انطلق! 🚀


# مشروع: بطاقة ملف برمجية
name = "علي"
track = "الذكاء الاصطناعي وبايثون"
completed_lessons = 4

print("=" * 25)
print(f"الاسم: {name}")
print(f"المسار التعليمي: {track}")
print(f"عدد الدروس المكتملة: {completed_lessons}")
print("=" * 25)

# النتيجة:
# =========================
# الاسم: علي
# المسار التعليمي: الذكاء الاصطناعي وبايثون
# عدد الدروس المكتملة: 4
# =========================


# حاسبة الخصم والضريبة للمتاجر

def calculate_final_price(price, discount_percent, tax_percent=15):
    # حساب قيمة الخصم
    discount_amount = price * (discount_percent / 100)
    price_after_discount = price - discount_amount
    
    # حساب الضريبة
    tax_amount = price_after_discount * (tax_percent / 100)
    final_price = price_after_discount + tax_amount
    
    return final_price, discount_amount, tax_amount

# تجربة البرنامج
original_price = 200.0
discount = 20.0  # خصم 20%

final, saved, tax = calculate_final_price(original_price, discount)

print("--- تفاصيل الفاتورة ---")
print(f"السعر الأصلي: {original_price} دولار")
print(f"المبلغ الموفر بالخصم: {saved} دولار")
print(f"مبلغ الضريبة: {tax} دولار")
print(f"السعر النهائي للشراء: {final} دولار")



