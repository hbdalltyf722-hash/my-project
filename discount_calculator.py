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
