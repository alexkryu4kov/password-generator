const { generatePassword, encryptPassword } = require('../app/static/generation.js');


test('generates password of correct length', () => {
    const length = 10;
    const password = generatePassword(length, false, false, false);
    expect(password).toHaveLength(length);
});


test('encrypts password correctly', () => {
    const password = 'TestPassword';
    const masterPassword = 'MasterPassword';
    const encrypted = encryptPassword(password, masterPassword);

    // Check if encrypted is a non-empty string
    expect(encrypted).toBeDefined();
    expect(encrypted).not.toBe('');
});