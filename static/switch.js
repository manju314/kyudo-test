const checkbox = document.getElementById("switch");
checkbox.addEventListener('click', () => {
    const title = document.querySelector('.title');
    title.textContent = checkbox.checked? 'ON' : 'OFF';
});