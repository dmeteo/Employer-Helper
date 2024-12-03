inputPasswords = document.querySelectorAll('input[type=password]');
passwordEyeButtons = document.querySelectorAll('.password-eye-button');

for (let i = 0; i < inputPasswords.length; i++) {
    passwordEyeButtons[i].addEventListener('click', function() {
        passwordEyeButtons[i].classList.toggle('open');
        if (passwordEyeButtons[i].classList.contains('open')) {
            inputPasswords[i].setAttribute('type', 'text');
        } else {
            inputPasswords[i].setAttribute('type', 'password');
        }
})};

