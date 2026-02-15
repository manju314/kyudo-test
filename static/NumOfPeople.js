const NumOfPeople = document.getElementById('NumOfPeople');
const highHit = document.getElementById('highHit');
const lowHit = document.getElementById('lowHit');

function updateHitRange() {

    const selectedValue = NumOfPeople.value;
    let max = 16;  // デフォルト（4人立ち）

    if (selectedValue === "5") {
        max = 20;
    } else if (selectedValue === "6") {
        max = 24;
    }

    // 両方クリア
    highHit.innerHTML = "";
    lowHit.innerHTML = "";

    for (let i = 0; i <= max; i++) {

        // highHit
        const highOption = document.createElement("option");
        highOption.value = i;
        highOption.textContent = i;

        if (i === max) {
            highOption.selected = true;
        }

        highHit.appendChild(highOption);

        // lowHit
        const lowOption = document.createElement("option");
        lowOption.value = i;
        lowOption.textContent = i;

        if (i === Math.ceil(max/2)) {
            lowOption.selected = true;
        }

        lowHit.appendChild(lowOption);
    }
}

// 変更時
NumOfPeople.addEventListener('change', updateHitRange);

// ページ読み込み時にも反映
window.addEventListener("DOMContentLoaded", updateHitRange);

lowHit.addEventListener("change", () => {
    if (parseInt(lowHit.value) > parseInt(highHit.value)) {
        highHit.value = lowHit.value;
    }
});

highHit.addEventListener("change", () => {
    if (parseInt(highHit.value) < parseInt(lowHit.value)) {
        lowHit.value = highHit.value;
    }
});
