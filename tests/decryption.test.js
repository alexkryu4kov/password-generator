const CryptoJS = require("crypto-js");
const { decryptPassword } = require('../app/static/decryption.js');


beforeAll(() => {
  global.alert = jest.fn();
});


test('decrypts password correctly', () => {
    const password = 'TestPassword';
    const masterPassword = 'MasterPassword';
    var encrypted = CryptoJS.AES.encrypt(password, masterPassword).toString();

    // Decrypt and test
    var decrypted = decryptPassword(encrypted, masterPassword);
    expect(decrypted).toBe(password);
});