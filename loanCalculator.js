// حاسبة الأقساط الشهرية للقروض والتمويل

function calculateMonthlyPayment(loanAmount, annualInterestRate, years) {
    let monthlyRate = (annualInterestRate / 100) / 12;
    let totalMonths = years * 12;
    
    // معادلة حساب القسط الشهري
    let monthlyPayment = (loanAmount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -totalMonths));
    let totalPayment = monthlyPayment * totalMonths;
    let totalInterest = totalPayment - loanAmount;

    return {
        monthly: monthlyPayment.toFixed(2),
        total: totalPayment.toFixed(2),
        interest: totalInterest.toFixed(2)
    };
}

// --- تجربة الحاسبة ---
// مبلغ القروض: 10,000 دولار | فائدة سنوية: 5% | المدة: 3 سنوات
let loanDetails = calculateMonthlyPayment(10000, 5, 3);

console.log("--- تفاصيل القسط والتمويل ---");
console.log("القسط الشهري: " + loanDetails.monthly + " دولار");
console.log("إجمالي المبلغ المسدد: " + loanDetails.total + " دولار");
console.log("إجمالي الفائدة: " + loanDetails.interest + " دولار");
