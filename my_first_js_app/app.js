let attempts = 3
const savedLogin = "admin";
const savedPassword = "1234"

const loginInput = document.getElementById("login");
const passwordInput = document.getElementById("password");
const loginBtn = document.getElementById("loginBtn");
const message = document.getElementById("message");
const menu = document.getElementById("menu");
const logoutBtn = document.getElementById("logoutBtn");
const calcBtn = document.getElementById("calcBtn");
const calculator = document.getElementById("calculator");
const num1Input = document.getElementById("num1");
const num2Input = document.getElementById("num2");
const sumBtn = document.getElementById("sumBtn");
const calcResult = document.getElementById("calcResult");


loginBtn.addEventListener("click", function() {

    const loginValue = loginInput.value;
    const passwordValue = passwordInput.value;

    if (loginValue === savedLogin && passwordValue === savedPassword) {
        message.style.color = "green";
        message.textContent = "Вход выполнен успешно";
        loginBtn.disabled = true; //блокиреум кнопку
        menu.classList.remove("hidden");
        loginInput.disabled = true;
        passwordInput.disabled = true;
    } else {
        attempts--;
        message.style.color = "red";
        message.textContent = "Неверный логин или пароль";
        
        if (attempts === 0) {
            message.textContent = "Доступ заблокирован";
            loginBtn.disabled = true;
        }
    }
    
});

logoutBtn.addEventListener("click", function() {
    location.reload();
});

calcBtn.addEventListener("click", function() {
    calculator.classList.remove("hidden");
});

sumBtn.addEventListener("click", function() {
    const n1 = +num1Input.value;
    const n2 = +num2Input.value;

    const result = n1 + n2;

    calcResult.textContent = `Результат: ${result}`;
});