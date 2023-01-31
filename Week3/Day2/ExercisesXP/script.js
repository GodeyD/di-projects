//  Exercise 1 : Change The Article
console.log(document.querySelector("h1"))
const deletePargf = document.querySelector("article").lastElementChild 

deletePargf.remove()

document.querySelector('h2').onclick = function() {
    const h2Color = document.querySelector('h2')
    h2Color.style.backgroundColor = "red"
}

document.querySelector('h3').onclick = function() {
    const h3Ninja = document.querySelector('h3')
    h3Ninja.style.display = "none"
}

const newBtn = document.createElement("button")
let newTextNode = document.createTextNode('BOLD me baby')
newBtn.appendChild(newTextNode);
document.body.appendChild(newBtn);

document.querySelector('button').onclick = function() {
    const pBold = document.querySelectorAll('p')
    for(i=0;i<pBold.length;i++)
{
    pBold[i].style.fontWeight = "900";
}
}

document.querySelector("h1").onmouseover = function() {
    const h1Rand = document.querySelector("h1")
    h1Rand.style.fontSize = `${Math.random(100)}px`
}

// Exercise 2 : Work With Forms
console.log(document.querySelector('form'))
console.log(document.querySelector('#fname'))
console.log(document.querySelector('#lname'))
console.log(document.querySelector('#submit'))

function inputNames() {
    for (i=0;i<document.querySelectorAll('input').length;i++) {
        console.log(document.querySelectorAll('input')[i].name)
    }
}
inputNames()

const firstForm = document.forms[0];
firstForm.addEventListener("submit", retrieveValue);
function retrieveValue (evt) {
    evt.preventDefault(); 
    const valueInput = evt.target.fname.value;
    const valueInput2 = evt.target.lname.value;
    const para =  document.createElement("li");
    const para2 =  document.createElement("li");    
    const text = document.createTextNode(`first name of the user ${valueInput}`)
    const text2 = document.createTextNode(`last name of the user ${valueInput2}`)
    para.appendChild(text);
    para2.appendChild(text2);
    let newUl = document.createElement('ul')
    newUl.classList.add('usersAnswer')
    document.body.appendChild(newUl)
    newUl.appendChild(para)
    newUl.appendChild(para2)
}

// Exercise 3 : Transform The Sentence
const allBoldItems = []
function getBold_items() {
    for (let i=0;i<document.querySelectorAll('strong').length;i++) {
        allBoldItems.push(document.querySelectorAll('strong')[i].textContent)
    }    
}
getBold_items()
console.log(allBoldItems)

function highlight() {
    for (let i=0;i<document.querySelectorAll('strong').length;i++) {
        document.querySelectorAll('strong')[i].style.color = 'blue'
    }  
}


function return_normal() {
    for (let i=0;i<document.querySelectorAll('strong').length;i++) {
        document.querySelectorAll('strong')[i].style.color = 'black'
    }  
}

function mouse() {
    for (let i=0;i<document.querySelectorAll('strong').length;i++) {
        document.querySelectorAll('strong')[i].addEventListener("mouseover", highlight);
        document.querySelectorAll('strong')[i].addEventListener("mouseout", return_normal)
    }      
}
mouse()

// Exercice 4 : Volume Of A Sphere
function volume(Radio) {
   let Volumen = 3/4 * Math.PI * Radio^3
   return Volumen
}

const secondForm = document.forms[1];
secondForm.addEventListener("submit", retrieveValue2);
function retrieveValue2(evt) {
    evt.preventDefault()
    const valueInput = evt.target.radius.value
    secondForm[1].defaultValue = `${volume(valueInput)}`   
}

//Exercise 5 : Event Listeners
document.querySelectorAll("p")[4].onmouseout = function() {
    const h1Rand = document.querySelectorAll("p")[4]
    h1Rand.style.fontSize = `${Math.random(400) * (100 - 20) + 20}px`
}
document.querySelectorAll("p")[4].onmouseover = function() {
    const h1Rand = document.querySelectorAll("p")[4]
    h1Rand.style.color = `red`
}
document.querySelectorAll("p")[4].onclick = function() {
    const h1Rand = document.querySelectorAll("p")[4]
    h1Rand.style.textShadow = `1px 1px 2px red, 0 0 1em blue, 0 0 0.2em blue`
}
document.querySelectorAll("p")[4].onclick = function() {
    const h1Rand = document.querySelectorAll("p")[4]
    h1Rand.style.textShadow = `1px 1px 2px red, 0 0 1em blue, 0 0 0.2em blue`
}
document.querySelectorAll("p")[4].ondblclick = function() {
    const h1Rand = document.querySelectorAll("p")[4]
    h1Rand.style.textDecoration = `underline overline #FF3028`
}