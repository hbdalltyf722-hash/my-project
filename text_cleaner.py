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
