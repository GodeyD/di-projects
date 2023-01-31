let newAlert = setTimeout(alerts, 2000)

function alerts() {
    console.log('in function');
    alert('Hello World')
    clearInterval(newAlert)
}

let newP = setTimeout(parah, 2000)

function parah() {
    console.log('in second function');
    const parah = document.createElement('p')
    const container = document.getElementById('container')
    parah.textContent = 'Hello World'
    container.appendChild(parah)
    clearInterval(newP)
}

let every2sec = setInterval(loop, 2000)

let cont = 2

function loop() {
    console.log('in tird function');
    if (cont == 5) {
        clearInterval(every2sec)
    }
    cont++
    const parah = document.createElement('p')
    const container = document.getElementById('container')
    parah.textContent = 'Hello World'
    container.appendChild(parah)
}

// document.getElementById('clear').addEventListener("click", stopInterval);
// function stopInterval() {
//     clearInterval(every2sec)   
// }
// Exercise 2 : Move The Box


document.querySelectorAll('button')[1].addEventListener('click', myMove)


function myMove() {
    let box = document.getElementById('animate')
    let move1px = setInterval(move, 1)
    let position = 0
    let container = document.getElementById('container')

    function move() {
        if (position >= container.offsetWidth - box.offsetWidth) {
            clearInterval(move1px)
        } else {
            console.log(position);
            position++
            box.style.left = `${position}px`
        }
    }
}

// 🌟 Exercise 3: Drag & Drop
let boxDrag = document.getElementById("box")
boxDrag.setAttribute('draggable', 'true');

boxDrag.addEventListener("dragstart", function(event) {
    event.target.style.backgroundColor = "lightpink";    
  });
  
  boxDrag.addEventListener("dragend", function(event) {
      event.target.style.backgroundColor = "lightgreen";
      let _x = event.clientX;
      let _y = event.clientY;      
      event.target.style.left = _x + "px";
      event.target.style.top = _y + "px";
      event.target.style.position = "absolute";      
    });