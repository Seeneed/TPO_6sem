const Validator = require('./validator');
const Calculator = require('./calculator');

class FinanceManager {
    constructor(db) { this.db = db; }

    async addTransaction(amount, category) {
        if (!Validator.isValidAmount(amount)) throw new Error("Invalid amount");
        if (!Validator.isValidCategory(category)) throw new Error("Invalid category");
        
        return await this.db.save({ amount, category, date: new Date() });
    }
}
module.exports = FinanceManager;