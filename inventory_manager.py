# نظام إدارة مخزون المنتجات للمتاجر

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, name, price, quantity):
        """إضافة منتج جديد للمخزون"""
        self.inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        print(f"✅ تم إضافة المنتج: {name}")

    def update_quantity(self, product_id, new_quantity):
        """تحديث كمية منتج موجود"""
        if product_id in self.inventory:
            self.inventory[product_id]["quantity"] = new_quantity
            print(f"🔄 تم تحديث كمية ({self.inventory[product_id]['name']}) إلى {new_quantity}")
        else:
            print("❌ المنتج غير موجود!")

    def calculate_total_value(self):
        """حساب القيمة الإجمالية لجميع البضائع في المخزن"""
        total_value = sum(item["price"] * item["quantity"] for item in self.inventory.values())
        return total_value

# --- تجربة النظام ---
store = InventoryManager()
store.add_product("P101", "قميص قطني", 25.0, 50)
store.add_product("P102", "بنطال جينز", 40.0, 30)

store.update_quantity("P101", 45)

total = store.calculate_total_value()
print(f"\n💰 القيمة الإجمالية للمخزون: {total} دولار")


# أداة معالجة وتنظيف النصوص للبيانات

def clean_and_analyze_text(raw_text):
    """تنظيف النص وحساب إحصائياته"""
    # إزالة المسافات الزائدة من البداية والنهاية
    cleaned = raw_text.strip()
    
    # تقسيم النص إلى كلمات
    words = cleaned.split()
    
    # حساب الإحصائيات
    word_count = len(words)
    char_count_no_spaces = sum(len(w) for w in words)
    
    return {
        "cleaned_text": " ".join(words),
        "word_count": word_count,
        "char_count": char_count_no_spaces
    }

# --- تجربة الأدوات ---
sample_input = "   تعلم   البرمجة   يفتح   لك   آفاقاً   جديدة    "
result = clean_and_analyze_text(sample_input)

print("--- نتائج معالجة النص ---")
print(f"النص بعد التنظيف: '{result['cleaned_text']}'")
print(f"عدد الكلمات: {result['word_count']}")
print(f"عدد الحروف (بدون مسافات): {result['char_count']}")

