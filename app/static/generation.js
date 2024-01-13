let CryptoJS;

if (typeof window === 'undefined') {
    // Jest environment
    CryptoJS = require("crypto-js");
} else {
    // Browser environment
    CryptoJS = window.CryptoJS;
}


function generateAndEncryptPassword(masterPassword) {
    var length = parseInt(document.getElementById('length').value);
    var useUppercase = document.getElementById('uppercase').checked;
    var useDigits = document.getElementById('digits').checked;
    var useSymbols = document.getElementById('symbols').checked;
    var generatedPassword = generatePassword(length, useUppercase, useDigits, useSymbols);


    if (masterPassword) {
      var encrypted = encryptPassword(generatedPassword, masterPassword);
      document.getElementById('encrypted_password').value = encrypted;
      document.getElementById('GeneratePasswordForm').submit();
    }
}


function generatePassword(length, useUppercase, useDigits, useSymbols) {
    var charset = "abcdefghijklmnopqrstuvwxyz";
    if (useUppercase) charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (useDigits) charset += "0123456789";
    if (useSymbols) charset += "!@#$%^&*()_+~";

    var password = "";
    for (var i = 0; i < length; i++) {
        var randomIndex = Math.floor(Math.random() * charset.length); 
        password += charset[randomIndex];
    }
    return password;
}

function encryptPassword(password, masterPassword) {
    var encrypted = CryptoJS.AES.encrypt(password, masterPassword);
    return encrypted.toString();
}


module.exports = { generatePassword, encryptPassword };
