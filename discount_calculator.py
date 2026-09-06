# مشروع: حاسبة الخصم للشركات والمتاجر
customer_name = "علي"
original_price = 200
discount_percent = 15

# حساب قيمة الخصم والسعر النهائي
discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount

print("--- تفاصيل الفاتورة ---")
print(f"اسم العميل: {customer_name}")
print(f"السعر الأصلي: {original_price} ريال")
print(f"نسبة الخصم: {discount_percent}%")
print(f"قيمة الخصم: {discount_amount} ريال")
print(f"السعر النهائي بعد الخصم: {final_price} ريال")
print("-----------------------")

# النتيجة في المخرجات:
# --- تفاصيل الفاتورة ---
# اسم العميل: علي
# السعر الأصلي: 200 ريال
# نسبة الخصم: 15%
# قيمة الخصم: 30.0 ريال
# السعر النهائي بعد الخصم: 170.0 ريال
# -----------------------


# نظام إدارة المهام اليومية البسيط

tasks_list = []

def add_task(task_name):
    tasks_list.append({"task": task_name, "status": "قيد التنفيذ"})
    print(f"تمت إضافة المهام: '{task_name}' بنجاح.")

def show_tasks():
    print("\n--- قائمة المهام الحالية ---")
    if not tasks_list:
        print("لا توجد مهام حالياً.")
        return
    
    for index, item in enumerate(tasks_list, 1):
        print(f"{index}. {item['task']} - [{item['status']}]")

# تشغيل وتجربة النظام
add_task("مراجعة كود العميل")
add_task("رفع المشاريع على جيت هوب")
add_task("تعلم أساسيات الجافا سكريبت")

show_tasks()


import random
import string

def generate_password(length=10):
    # تجميع الأحرف والأرقام
    characters = string.ascii_letters + string.digits
    # اختيار عناصر عشوائية
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# تجربة المولد
new_password = generate_password(12)

print("--- مولد كلمات المرور الآمنة ---")
print(f"كلمة المرور المقترحة: {new_password}")

