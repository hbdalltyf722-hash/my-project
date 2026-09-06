// مشروع: فاحص الدرجات والتقييم
const studentName = "علي";
const score = 95;

console.log(`طالب/ـة: ${studentName}`);
console.log(`الدرجة: ${score}`);

// اختبار النتيجة باستخدام الشروط
if (score >= 50) {
    console.log("النتيجة: ناجح 🎯");
} else {
    console.log("النتيجة: يحتاج إلى تحسين");
}

// النتيجة في الـ Console:
// طالب/ـة: علي
// الدرجة: 95
// النتيجة: ناجح 🎯



// برنامج تحويل العملات البسيط

function convertCurrency(amountInUSD, exchangeRate) {
    let convertedAmount = amountInUSD * exchangeRate;
    return convertedAmount;
}

// تجربة التحويل من دولار إلى ريال (مثال سعر الصرف = 3.75)
let usdAmount = 100;
let saudiRate = 3.75;

let totalInSAR = convertCurrency(usdAmount, saudiRate);

console.log("--- محول العملات ---");
console.log(usdAmount + " دولار تساوي = " + totalInSAR + " ريال سعودي");



// حاسبة معدل درجات الطالب

function evaluateStudent(marks) {
    let total = 0;
    for (let i = 0; i < marks.length; i++) {
        total += marks[i];
    }
    let average = total / marks.length;
    let status = average >= 50 ? "ناجح ✅" : "راسب ❌";
    
    return { average: average, status: status };
}

// تجربة درجات الطالب
let studentMarks = [85, 90, 78, 92];
let result = evaluateStudent(studentMarks);

console.log("--- التقرير الأكاديمي ---");
console.log("المعدل النهائي: " + result.average);
console.log("النتيجة: " + result.status);



// نظام سلة التسوق الإلكترونية

let cart = [
    { item: "قميص", price: 25 },
    { item: "حذاء", price: 60 },
    { item: "حقيبة", price: 40 }
];

function calculateTotal(cartItems) {
    let totalPrice = 0;
    for (let i = 0; i < cartItems.length; i++) {
        totalPrice += cartItems[i].price;
    }
    return totalPrice;
}

console.log("--- إجمالي سلة الشراء ---");
console.log("المبلغ الإجمالي المطلوب: " + calculateTotal(cart) + " دولار");



// أداة تحليل النصوص

function analyzeText(text) {
    let characterCount = text.length;
    let wordCount = text.trim().split(/\s+/).length;
    
    return {
        words: wordCount,
        characters: characterCount
    };
}

let sampleText = "تعلم البرمجة يقودك إلى فرص عمل ممتازة";
let analysis = analyzeText(sampleText);

console.log("--- تحليل النص ---");
console.log("عدد الكلمات: " + analysis.words);
console.log("عدد الحروف: " + analysis.characters);



// نظام الترحيب التلقائي

function getGreeting(hour) {
    if (hour >= 5 && hour < 12) {
        return "صباح الخير! ☀️";
    } else if (hour >= 12 && hour < 18) {
        return "مساء الخير! 🌤️";
    } else {
        return "تصبح على خير! 🌙";
    }
}

// تجربة الساعة 10 صباحاً والساعة 8 مساءً
console.log("الساعة 10: " + getGreeting(10));
console.log("الساعة 20: " + getGreeting(20));


