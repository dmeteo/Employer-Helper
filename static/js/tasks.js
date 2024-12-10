tasksListElement = document.querySelector('.tasks-list');
taskTemplate = document.querySelector('.task-template').content.querySelector('.task-item');



function fillTasks(tasks) {
    tasksFragment = document.createDocumentFragment();
    tasks.forEach(task => {
        const taskElement = taskTemplate.cloneNode(true);
        taskElement.querySelector('.task-name').textContent = task.title;
        taskElement.querySelector('.task-description').textContent = task.description;
        taskElement.querySelector('.task-end-date span').textContent = task.deadline.toLocaleDateString();
        taskElement.querySelector('.task-link').href = '#'
        taskElement.style.backgroundColor = blue;
        tasksFragment.appendChild(taskElement);
    });
    tasksListElement.appendChild(tasksFragment);
}


fillTasks(tasks);