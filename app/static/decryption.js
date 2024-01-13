let CryptoJS;

if (typeof window === 'undefined') {
    // Jest environment
    CryptoJS = require("crypto-js");
} else {
    // Browser environment
    CryptoJS = window.CryptoJS;
}


function decryptPassword(password, masterPassword) {
    if (masterPassword) {
        var decrypted = CryptoJS.AES.decrypt(password, masterPassword).toString(CryptoJS.enc.Utf8);
        console.log(decrypted);
        if (decrypted) {
          alert("Decrypted Password: " + decrypted);
        } else {
          alert("Decryption failed. Incorrect master password?");
        }
        return decrypted;
    }
}


module.exports = { decryptPassword };