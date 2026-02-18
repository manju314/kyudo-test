fetch("/static/mode.json")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        console.log(data.mode);

        if (data.mode === "on") {
            realMode();
        } else {
            nomalMode();
        }
    })
    .catch(error => {
        console.error("JSON読み込みエラー:", error);
    });

const cells = Array.from(document.querySelectorAll(".cell"));

const lenRes = res.length;

console.log(res)
function realMode() {
    console.log("realMode")
    for (let i = 0; i < lenRes; i++) { 
        let results = document.createTextNode(res[i]);
        cells[i].appendChild(results);
        let cellId = String(i);
        cells[i].setAttribute("id",cellId);
        let cell = document.getElementById(cellId);
        cell.style.opacity = 0
    }

    let i = lenRes - 1;
    function showNext() {
        if (i >= 0) {
            let cellId = String(i); 
            let cell = document.getElementById(cellId);
            cell.style.opacity = 1
            i = i - 1;
        }
    }
    setInterval(showNext, 5000);
    setInterval(totalResView, 5000*(lenRes+0.25));
}

function nomalMode() {
    console.log("nomalMode")
    for (let i = 0; i < lenRes; i++) { 
        let result = document.createTextNode(res[i]);
        cells[i].appendChild(result);
        let cellId = String(i);
        cells[i].setAttribute("id",cellId);
        let cell = document.getElementById(cellId);
        cell.style.opacity = 1
    }
    totalResView()
}

function totalResView() {
    const totalRes = document.getElementById('totalRes');
    totalRes.style.opacity = 1
    toKyousya.style.opacity = 1
}



// const cells = Array.from(document.querySelectorAll(".cell"));
// const toggle = document.getElementById("mode");

// console.log("cells:", cells.length);
// console.log("res:", res.length);
// console.log(res);

// if (typeof res !== "undefined" && typeof mode !== "undefined") {

//     const lenRes = res.length;

//     if (mode) {
//         realMode();
//     } else {
//         nomalMode();
//     }

//     if (toggle) {
//         toggle.addEventListener("change", function () {
//             if (toggle.checked) {
//                 realMode();
//             } else {
//                 nomalMode();
//             }
//         });
//     }





// function realMode() {
//     for (let i = 0; i < lenRes; i++) { 
//         cells[i].textContent = res[i];
//         cells[i].style.opacity = 0;
//     }

//     let i = lenRes - 1;
//     function showNext() {
//         if (i >= 0) {
//             cells[i].style.opacity = 1;
//             i--;
//         }
//     }
//     setInterval(showNext, 5000);
// }

// function nomalMode() {
//     for (let i = 0; i < lenRes; i++) { 
//         cells[i].textContent = res[i];
//         cells[i].style.opacity = 1;
//     }
// }
