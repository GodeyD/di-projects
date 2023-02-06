let inputT = document.createElement("input")
document.body.appendChild(inputT)

function mach(e) {
let regex = /^[a-zA-Z]*$/i
if(e.target.value.match(regex)) {    
    alert('its a valid text plz incert another')
    return true
} else {
    alert('its no a valid text')
    return false
}
}

inputT.addEventListener("keydown", mach)