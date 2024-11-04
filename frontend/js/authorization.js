inputPassword = document.querySelector('#password');
passwordEyeButton = document.querySelector('.password-eye-button');

passwordEyeButton.addEventListener('click', function() {
    passwordEyeButton.classList.toggle('open');
    if (passwordEyeButton.classList.contains('open')) {
        inputPassword.setAttribute('type', 'text');
    } else {
        inputPassword.setAttribute('type', 'password');
    }
});