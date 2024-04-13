const flipNumbers = document.querySelectorAll('.flip-number');

function updateTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');

    flipNumbers[0].textContent = hours.charAt(0);
    flipNumbers[1].textContent = hours.charAt(1);
    flipNumbers[2].textContent = ':';
    flipNumbers[3].textContent = minutes.charAt(0);
    flipNumbers[4].textContent = minutes.charAt(1);
    flipNumbers[5].textContent = ':';
    flipNumbers[6].textContent = seconds.charAt(0);
    flipNumbers[7].textContent = seconds.charAt(1);

    flipNumbers.forEach((flipNumber, index) => {
        if (index % 2 === 0) {
            flipNumber.classList.remove('even');
            flipNumber.classList.add('odd');
        } else {
            flipNumber.classList.remove('odd');
            flipNumber.classList.add('even');
        }
    });
}

updateTime();
setInterval(updateTime, 1000);