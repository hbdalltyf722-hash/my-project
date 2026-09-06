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

