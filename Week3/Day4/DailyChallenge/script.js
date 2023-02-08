const tasks = []
const firstForm = document.forms[0];

firstForm.addEventListener("submit", addTask);

function addTask(evt) {
    evt.preventDefault()
    const input = firstForm.querySelector('input')
    if (input.value.length == 0) {
        alert('plz create a task')
        evt.preventDefault()
    } else if (tasks[tasks.length - 1] != input.value) {
        tasks.push(input.value)
        console.log(tasks);
    } else {
        alert('put a diferent task')
        evt.preventDefault()
    }
    let newTask = document.createElement('div')
    let newTextNode = document.createTextNode(`${tasks[tasks.length - 1]}`)
    newTask.appendChild(newTextNode)
    let list = document.getElementsByClassName('listTasks')[0]
    list.appendChild(newTask)
}