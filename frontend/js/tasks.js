tasksListElement = document.querySelector('.tasks-list');
taskTemplate = document.querySelector('.task-template').content.querySelector('.task-item');

const tasks = [
    {id: 0, name: "1-дневная задача", description: 'Описание 1', start: new Date(2024, 11, 17), end: new Date(2024, 11, 17), color: "#e7f6fd", status: "completed"},
    {id: 1, name: "1-дневная задача 2", description: 'Описание 2', start: new Date(2024, 11, 17), end: new Date(2024, 11, 17), color: "#71ff53", status: "completed"},
    {id: 2, name: "Задача в рамках 1-й недели", description: 'Описание 3', start: new Date(2024, 11, 19), end: new Date(2024, 11, 22), color: '#ffe8f4', status: "active"},
    {id: 3, name: "Задача на 2 недели", description: 'Описание 4 со слишком уж длинным текстом, который ну никак не поместится в блок с описанием. Описание настолько большое, что [вставить шутку]!', 
        start: new Date(2024, 11, 3), end: new Date(2024, 11, 13), color: '#fef6e7', status: "active"}
]


function fillTasks(tasks) {
    tasksFragment = document.createDocumentFragment();
    tasks.forEach(task => {
        const taskElement = taskTemplate.cloneNode(true);
        taskElement.querySelector('.task-name').textContent = task.name;
        taskElement.querySelector('.task-description').textContent = task.description;
        taskElement.querySelector('.task-end-date span').textContent = task.end.toLocaleDateString();
        
        // TODO: Добавить ссылку
        taskElement.querySelector('.task-link').href = '#'
        taskElement.style.backgroundColor = task.color;
        tasksFragment.appendChild(taskElement);
    });
    tasksListElement.appendChild(tasksFragment);
}


fillTasks(tasks);