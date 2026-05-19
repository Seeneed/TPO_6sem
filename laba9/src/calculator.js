const Calculator = {
    applyTax: (amount, taxPercent) => amount - (amount * (taxPercent / 100)),
    calculateBudget: (income, expenses) => income - expenses
};
module.exports = Calculator;