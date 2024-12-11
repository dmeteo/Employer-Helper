
tasksListElement = document.querySelector('.tasks-list');
taskTemplate = document.querySelector('.task-template').content.querySelector('.task-item');

const tasks = JSON.parse(JSON.parse(document.getElementById('tasks').textContent));

function fillTasks(tasks) {
    let len = tasks.length;
    let i = 0;
    tasksFragment = document.createDocumentFragment();
    while (i < len) {
        console.log(tasks[i])
        const taskElement = taskTemplate.cloneNode(true);
        taskElement.querySelector('.task-name').textContent = tasks[i].fields.title;
        taskElement.querySelector('.task-description').textContent = tasks[i].fields.description;
        taskElement.querySelector('.task-end-date span').textContent = tasks[i].fields.deadline;
        taskElement.querySelector('.task-link').href = "/tasks/" + tasks[i].pk;
        taskElement.style.backgroundColor = "#ccc5f9";
        tasksFragment.appendChild(taskElement);
        i++;
    };
    tasksListElement.appendChild(tasksFragment);
}


fillTasks(tasks);