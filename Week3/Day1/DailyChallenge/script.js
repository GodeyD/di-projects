solarSystem = [
    planet = {
        planetName : "Mercury",
        moon : 0,
        color : "grey",
    },
    planet = {
        planetName : "Venus",
        moon : 0,
        color : "beige",
    },
    planet = {
        planetName : "Earth",
        moon : 1,
        color : "green",
    },
    planet = {
        planetName : "Mars",
        moon : 2,
        color : "red",
    },
    planet = {
        planetName : "Jupiter",
        moon : 57,
        color : "brown",
    },
    planet = {
        planetName : "Saturn",
        moon : 63,
        color : "yellow",
    }
    ,planet = {
        planetName : "Uranus",
        moon : 27,
        color : "skyblue",
    },
    planet = {
        planetName : "Neptune",
        moon : 14,
        color : "blue",
    }

]


function addPlanets() {
    const sectionPlanets = document.querySelector(".listPlanets")
    for(let planet of solarSystem){
        const planetDiv = document.createElement("div")
        const content = document.createTextNode(planet["planetName"])
        const classEachPlanet = planet["planetName"].toLowerCase()
        planetDiv.classList.add("planet", classEachPlanet)
        planetDiv.appendChild(content)
        sectionPlanets.appendChild(planetDiv)
        planetDiv.style.backgroundColor = `${planet["color"]}`

        for (let i = 1; i<= planet["moon"]; i++) {
            const moonDiv = document.createElement("div")
            moonDiv.classList.add("moon")
            planetDiv.appendChild(moonDiv)
            moonDiv.style.left = "80px"
        }
    }
}
addPlanets()