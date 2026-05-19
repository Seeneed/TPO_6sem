const Validator = require('../src/validator');
const Calculator = require('../src/calculator');
const FinanceManager = require('../src/manager');

describe('Finance App Unit Tests', () => {

    test('1. calculateBudget: correct calculation', () => {
        expect(Calculator.calculateBudget(1000, 300)).toBe(700);
    });
    test('2. calculateBudget: zero expenses', () => {
        expect(Calculator.calculateBudget(500, 0)).toBe(500);
    });
    test('3. applyTax: correct deduction', () => {
        expect(Calculator.applyTax(200, 20)).toBe(160);
    });

    test('4. validator: valid amount', () => {
        expect(Validator.isValidAmount(100)).toBe(true);
    });
    test('5. validator: zero amount', () => {
        expect(Validator.isValidAmount(0)).toBe(false);
    });
    test('6. validator: valid category', () => {
        expect(Validator.isValidCategory('food')).toBe(true);
    });
    test('7. validator: invalid category', () => {
        expect(Validator.isValidCategory('casino')).toBe(false);
    });

    test('8. addTransaction: successful save', async () => {
        const mockDb = { save: jest.fn().mockResolvedValue({ id: 1 }) };
        const manager = new FinanceManager(mockDb);
        const result = await manager.addTransaction(100, 'salary');
        expect(result).toEqual({ id: 1 });
    });

    test('9. addTransaction: throws error for invalid amount', async () => {
        const manager = new FinanceManager({});
        await expect(manager.addTransaction(-10, 'food')).rejects.toThrow("Invalid amount");
    });

    test('10. addTransaction: throws error for invalid category', async () => {
        const manager = new FinanceManager({});
        await expect(manager.addTransaction(100, 'travel')).rejects.toThrow("Invalid category");
    });
});