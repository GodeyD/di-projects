const firstForm = document.forms[0];
firstForm.addEventListener("submit", retrieveValue);
function retrieveValue(evt) {
    evt.preventDefault()
    const allInputs = firstForm.querySelectorAll('input')
    // var noun = document.forms.libform.noun.value
    
    let allValues = []
    for (let input of allInputs) {
        allValues.push(input.value)
    }
    document.querySelector('p').textContent = `Generated story: Sr./a ${allValues[0]} is know as ${allValues[1]} but his friend ${allValues[2]} ho is really ${allValues[3]} tell about ${allValues[4]} `
    
    
}