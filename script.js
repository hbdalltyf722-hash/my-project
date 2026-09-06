// 1. تعريف المتغيرات
let game = "كرة القدم";
let players = 11; 

// 2. الطباعة بأسلوب Template Literals
console.log(`اللعبة المفضلة هي ${game} وعدد لاعبيها ${players} لاعبين.`);

#النتيجة (المخرجات): 
اللعبة المفضلة هي كرة القدم وعدد لاعبيها 11 لاعبين.



// 1. تعريف المتغيرات
const game = "كرة القدم";
const players = 11;

// 2. الطباعة باستخدام Template Literals (باستخدام الأقواس ${})
console.log(`عدد لاعبين ${game} هو ${players} لاعباً`);

// النتيجة في الـ Console:
// عدد لاعبين كرة القدم هو 11 لاعباً



// 1. إنشاء مصفوفة (قائمة)
const drinks = ["شاي", "قهوة", "عصير"];

// 2. طباعة أول عنصر (Index 0)
console.log(drinks[0]);

// النتيجة في الـ Console:
// شاي


// حلقة تكرار لطباعة تسلسل من 0 إلى 2
for (let i = 0; i < 3; i++) {
    console.log("العدد", i);
}

// النتيجة في الـ Console:
// العدد 0
// العدد 1
// العدد 2


// فاحص قوة كلمة المرور

function checkPasswordStrength(password) {
    if (password.length >= 8) {
        return "كلمة مرور قوية ومقبولة ✅";
    } else {
        return "كلمة مرور ضعيفة، يجب أن تحتوي على 8 خانات على الأقل ❌";
    }
}

# تجربة الفحص
let pass1 = "12345";
let pass2 = "python_dev_2026";

console.log("فحص كلمة المرور الأولى: " + checkPasswordStrength(pass1));
console.log("فحص كلمة المرور الثانية: " + checkPasswordStrength(pass2));


