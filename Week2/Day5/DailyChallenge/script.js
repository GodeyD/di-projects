let bottleInWall = 99
let bottleInTheBoys = giveNumber()

function giveNumber() {
    let number = prompt('give a number', '0')
    while (isNaN(number)) {
        number = prompt('that is no a number', '0')
    }
    return Number(number)
}

function song(bottleInWall, bottleInTheBoys) {
    while (bottleInTheBoys == 1) {
        bottleInWall -= 1
        console.log(`99 bottles of beer on the wall`)
        console.log(`99 bottles of beer`)
        console.log(`Take 1 down, pass it around`)
        console.log(`${bottleInWall} bottles of beer on the wall`)
        console.log(" ")
        break
    }

    while (bottleInTheBoys > 0 && bottleInWall >= 0) {
        console.log(`${bottleInWall} bottles of beer on the wall`)
        console.log(`${bottleInWall} bottles of beer`)
        bottleInWall -= bottleInTheBoys
        bottleInTheBoys += 1
        console.log(`Take ${bottleInTheBoys} down, pass them around`)
        if (bottleInWall < 0) {
            console.log("no bottle of beer on the wall")
        } else {
            console.log(`${bottleInWall} bottles of beer on the wall`)
            console.log(" ")
        }
    }
}

song(bottleInWall, bottleInTheBoys)