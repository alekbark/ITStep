let attempts = 3;
let secretNumber = Math.floor(Math.random() * 100) + 1;
let gameAttempts = 0;

const users = [
    { login: "admin", password: "1234" },
    { login: "oleg", password: "7777" },
    { login: "test", password: "0000" }
];

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
const calcResult = document.getElementById("calcResult");
const operatorSelect = document.getElementById("operator");
const calcBtnDo = document.getElementById("calcBtnDo");

const ageBtn = document.getElementById("ageBtn");
const ageBlock = document.getElementById("ageBlock");
const ageInput = document.getElementById("ageInput");
const checkAgeBtn = document.getElementById("checkAgeBtn");
const ageResult = document.getElementById("ageResult");

const gameBtn = document.getElementById("gameBtn")
const gameBlock = document.getElementById("gameBlock")
const guessInput = document.getElementById("guessInput")
const guessBtn = document.getElementById("guessBtn")
const gameResult = document.getElementById("gameResult")


// Авторизация
loginBtn.addEventListener("click", function () {

    const loginValue = loginInput.value;
    const passwordValue = passwordInput.value;

    let isAuthorised = false;

    for (let i = 0; i < users.length; i++) {

        if (
            users[i].login === loginValue &&
            users[i].password === passwordValue
        ) {
            isAuthorised = true;
            break;
        }
    }

    if (isAuthorised) {
        
        message.style.color = "green";
        message.textContent = "Вход выполнен успешно";

        loginBtn.disabled = true;
        loginInput.disabled = true;
        passwordInput.disabled = true;

        menu.classList.remove("hidden");
    
    } else {

        attempts--;

        message.style.color = "red";
        message.textContent = `Неверный логин или пароль. Осталось попыток ${attempts}`;

        if (attempts === 0) {
            message.textContent = "Доступ заблокирован";
            loginBtn.disabled = true;
        }
    }
});


// Выход
logoutBtn.addEventListener("click", function () {
location.reload();
});


// Показ калькулятора
calcBtn.addEventListener("click", function () {
calculator.classList.remove("hidden");
ageBlock.classList.add("hidden");
gameBlock.classList.add("hidden");
});


// Логика калькулятора
calcBtnDo.addEventListener("click", function () {

    const n1 = +num1Input.value;
    const n2 = +num2Input.value;
    const operator = operatorSelect.value;

    let result;

    switch (operator) {
        case "+":
            result = n1 + n2;
            break;
        case "-":
            result = n1 - n2;
            break;
        case "*":
            result = n1 * n2;
            break;
        case "/":
            if (n2 === 0) {
                calcResult.textContent = "Деление на 0 невозможно";
                return;
            }
            result = n1 / n2;
            break;
        default:
            calcResult.textContent = "Неизвестная операция";
            return;
    }

    calcResult.textContent = `Результат: ${result}`;
});


// Показ блока возраста
ageBtn.addEventListener("click", function () {
ageBlock.classList.remove("hidden");
calculator.classList.add("hidden");
gameBlock.classList.add("hidden");
});


// Проверка возраста
checkAgeBtn.addEventListener("click", function () {

const age = +ageInput.value;

if (!Number.isInteger(age) || age < 0 || age > 120) {
ageResult.style.color = "red";
ageResult.textContent = "Некорректный возраст";
return;
}

ageResult.style.color = "green";
ageResult.textContent = "Возраст введён корректно";
});

// Показ игры
gameBtn.addEventListener("click", function () {
    gameBlock.classList.remove("hidden");
    calculator.classList.add("hidden");
    ageBlock.classList.add("hidden");
});

// Игра
guessBtn.addEventListener("click", function () {

    const guess = +guessInput.value;
    gameAttempts++;

    if (!Number.isInteger(guess) || guess < 1 || guess > 100) {
        gameResult.style.color = "red";
        gameResult.textContent = "Введите число от 1 до 100";
        return;
    }

    if (guess < secretNumber) {
        gameResult.style.color = "black";
        gameResult.textContent = "Слишком маленькое число";
    }
    else if (guess > secretNumber) {
        gameResult.style.color = "black";
        gameResult.textContent = "Слишком большое число";
    }
    else {
        gameResult.style.color = "green";
        gameResult.textContent = `Вы угадали за ${gameAttempts} попыток!`;
        guessBtn.disabled = true;
    }

});