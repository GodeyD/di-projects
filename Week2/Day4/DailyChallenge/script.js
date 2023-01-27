let words = []
let wordLength = 0
for (let i = 0; i < 4; i++) {
    let word = prompt('word plz', 'worldchampion')
    words.push(word)
}

function longestStringForLoop(words) {
    let word = "";
    for (let i = 0; i < words.length; i++) {
        if (word.length < words[i].length) {
            word = words[i];
        }
    }
    return word.length;
}

function stars() {
    let star = ""
    for (let i = 0; i < longestStringForLoop(words) + 4; i++) {
        star += "*"
    }
    return star
}

function starSpace(x) {
    let space = ""
    for (let i = 0; i < Number(longestStringForLoop(words)) - x+1; i++) {
        space += " "
    }
    return space
}

function display () {
    console.log(stars())
    for (let i=0; i<words.length;i++) {
        console.log(`* ${words[i]}${starSpace(words[i].length)}*`)
    }
    console.log(stars())
}
display()
