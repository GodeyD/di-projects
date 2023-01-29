// Exercise 1 : Users
console.log(document.body.children[0])

const ul1 = document.body.children[1]
const lis = ul1.children[1]
lis.textContent = "Richard"

const lis2 = ul1.children[0]
lis2.textContent = "Diego"

const ul2 = document.body.children[2]
const lis3 = ul2.children[0]
lis3.textContent = "Diego"

ul1.classList.add("student_list", "university", "attendance")
ul2.classList.add("student_list")

//Exercise 2 : Users And Style
const div2 = document.body.children[3]
div2.style.backgroundColor = "lightblue"
div2.style.padding = "50px"
const ul3 = document.body.children[4]
const lis4 = ul3.children[0]
lis4.style.display = "none"
const lis5 = ul3.children[1]
lis5.style.border = "5px solid red"
document.body.style.fontSize = "20px"

function hello() {
    if (div2.style.backgroundColor = "lightblue") {
        return alert(`Hello ${lis4.textContent} and ${lis5.textContent}`)
    }
}

hello()

// Exercise 3 : Change The Navbar
const nav = document.querySelector("#navBar")
nav.setAttribute('id',"socialNetworkNavigation")
const ul4 = nav.children[0]
const newLi = document.createElement("li") 
newLi.textContent = "Logout"
ul4.appendChild(newLi)
console.log(ul4.firstElementChild.textContent)
console.log(ul4.lastElementChild.textContent)


// Exercise 4 : My Book List
allBooks = [
    book1 = {
        title: "Harry Potter y la piedra filosofal",
        author: "J.K. Rowling",
        image: "https://m.media-amazon.com/images/I/91R1AixEiLL.jpg",
        alreadyRead: "false",
    }, 
    book2 = {
        title: "Cincuenta sombras de Grey",
        author: "E.L. James",
        image: "https://m.media-amazon.com/images/I/81MmInErTOS.jpg",
        alreadyRead: "true",
    }
]

div3 = document.querySelector(".listBooks")

const table = document.createElement("table")
div3.appendChild(table)

const tr = document.createElement("tr")
table.appendChild(tr)

const thTitle = document.createElement("th")
thTitle.textContent = "Title"
tr.appendChild(thTitle)

const thAuthor = document.createElement("th")
thAuthor.textContent = "Author"
tr.appendChild(thAuthor)

const thImage = document.createElement("th")
thImage.textContent = ""
tr.appendChild(thImage)

const tr2 = document.createElement("tr")
table.appendChild(tr2)

const harry = document.createElement("th")
harry.textContent = `${Object.values(allBooks[0])[0]}`
tr2.appendChild(harry)

const rollin = document.createElement("th")
rollin.textContent = `${Object.values(allBooks[0])[1]}`
tr2.appendChild(rollin)

const imageBookHarry = document.createElement("th")
const imageTag = document.createElement("img")
imageTag.setAttribute('src', `${Object.values(allBooks[0])[2]}`)
imageTag.style.width = '100px'
tr2.appendChild(imageBookHarry)
imageBookHarry.appendChild(imageTag)


const tr3 = document.createElement("tr")
table.appendChild(tr3)

const gray = document.createElement("th")
gray.textContent = `${Object.values(allBooks[1])[0]}`
tr3.appendChild(gray)

const james = document.createElement("th")
james.textContent = `${Object.values(allBooks[1])[1]}`
tr3.appendChild(james)

const imageBookGray = document.createElement("th")
const imageTag2 = document.createElement("img")
imageTag2.setAttribute('src', `${Object.values(allBooks[1])[2]}`)
imageTag2.style.width = '100px'
tr3.appendChild(imageBookGray)
imageBookGray.appendChild(imageTag2)

function bookRead(alreadyRead1, alreadyRead2) {
    if (alreadyRead1 == "true") {
       tr2.style.color = "red" 
    }
    if (alreadyRead2 == "true") {
        tr3.style.color = "red" 
    }
} 

bookRead(Object.values(allBooks[0])[3], Object.values(allBooks[1])[3])



// `${Object.values(allBooks[0])[0]}`
