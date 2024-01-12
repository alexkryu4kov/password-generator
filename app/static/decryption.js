function decryptPassword(password, masterPassword) {
    console.log(password);
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