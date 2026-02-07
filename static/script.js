const cells = Array.from(document.querySelectorAll(".cell"));

const order = [];
for (let r = 3; r >= 0; r--) {
    for (let c = 5; c >= 0; c--) {
        order.push(r * 6 + c);
    }
}

let i = 0;

function showNext() {
    if (i >= res.length || i >= order.length) return;

    const cellIndex = order[i];
    cells[cellIndex].textContent = res[i];
    i++;
}

setInterval(showNext, 5000);