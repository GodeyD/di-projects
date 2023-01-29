// Exercise 1 : Checking The BMI
let firstPerson = {
    FullName: "Keren Koala",
    Mass: 85,
    Height: 1.60,
    BMI: function bmi(x, y) {
        return x / Math.pow(y, 2)  
      },
}

let secondPerson = {
    FullName: "Kn Fitness",
    Mass: 70,
    Height: 1.60,
    BMI: function bmi(x, y) {
        return x / Math.pow(y, 2)  
      },
}

console.log(firstPerson.BMI(firstPerson.Mass, firstPerson.Height))
console.log(secondPerson.BMI(secondPerson.Mass, secondPerson.Height))

function comparate (firstBmi, secondBmi) {
    if (firstBmi < secondBmi) {
        console.log(secondPerson.FullName)
    } else {
        console.log(firstPerson.FullName)
    }
}

comparate(firstPerson.BMI(firstPerson.Mass, firstPerson.Height), secondPerson.BMI(secondPerson.Mass, secondPerson.Height))
// Exercise 2 : Grade Average
let gradesList = [90, 65, 35, 28, 100, 50]

function findAvg(gradesList) {
    gradesList.forEach(element => {
        let sum = sum=+element
        return sum/2
    });

}