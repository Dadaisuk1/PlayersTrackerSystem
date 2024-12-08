function toggleSubmitButton() {
    const checkbox = document.getElementById('confirmCheckbox');
    const submitButton = document.getElementById('submitButton');
    submitButton.disabled = !checkbox.checked;
}

function validatePasswords() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorSpan = document.getElementById('passwordError');

    if (password !== confirmPassword) {
        errorSpan.style.display = 'none';
        return false;
    } else {
        errorSpan.style.display = 'block';
        return true;
    }
}

function togglePassword(inputId) {
    const input = document.getElementById(inputId);
    const icon = input.nextElementSibling.querySelector('i');
    const type = input.type === 'password' ? 'text' : 'password';
    input.type = type;
    icon.classList.toggle('fa-eye-slash');
}
