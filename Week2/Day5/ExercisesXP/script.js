function playTheGame() {
    if (window.confirm("Do you want to play?")) {
        return number()
    } else {
        window.open("exit.html", "Thanks for Visiting!")
        alert("Never gonna let me down again plz")
    }

    function number() {
        let userNumber = prompt("Enter a number between 0 and 10 ", "5")
        while (isNaN(userNumber)) {
            alert("Sorry Not a number, try again")
            userNumber = prompt("Enter a number between 0 and 10 ", "5")
        }
        while (userNumber < 0 || userNumber > 10) {
            alert("Sorry it’s not a good number, try again")
            userNumber = prompt("Enter a number between 0 and 10 ", "5")
        }
            var computerNumber = Math.random() * 11
            return compareNumbers(userNumber, Math.floor(computerNumber))
        }
    }


function compareNumbers(userNumber, computerNumber) {
    count = 0

    while (userNumber > computerNumber) {
        count += 1
        if (count > 2) {
            return alert("out of chances")
        } else {
            alert("Your number is bigger then the computer’s, guess again")
            userNumber = prompt("Enter a number between 0 and 10 ", "5")
        }
    }
    while (userNumber < computerNumber) {
        count += 1
        if (count > 2) {
            return alert("out of chances")
        } else {
            alert("Your number is smaller then the computer’s, guess again")
            userNumber = prompt("Enter a number between 0 and 10 ", "5")
        }
    }
    do {
        if (isNaN(userNumber)) {
            alert("Sorry Not a number, Goodbye")
        } else if (userNumber < 0 || userNumber > 10) {
            alert("Sorry it’s not a good number, Goodbye")
        } else {
            return alert("WINNER!")
        }
    }
    while (Number(userNumber) == Number(computerNumber))
}