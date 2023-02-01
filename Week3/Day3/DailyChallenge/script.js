let inputT = document.createElement("input")
document.body.appendChild(inputT)

function mach(e) {
let regex = /^[a-zA-Z]*$/i
if(e.target.value.match(regex)) {
    document.body.style.backgroundColor = "blue"
    return true
} else {
    document.body.style.backgroundColor = "red"
    return false
}
}

inputT.addEventListener("keydown", mach)