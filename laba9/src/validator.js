const Validator = {
    isValidAmount: (amount) => typeof amount === 'number' && amount > 0,
    isValidCategory: (category) => ['food', 'salary', 'fun', 'rent'].includes(category)
};
module.exports = Validator;