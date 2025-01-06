const task = { 
    id: 7,
    name: "Выполнение тест-кейсов и документирование результатов. ", 
    description: 
`1. Подготовка к тестированию:
    - Ознакомление с функциональными требованиями и спецификациями продукта.

2. Выполнение тест-кейсов:
    - Последовательное выполнение каждого тест-кейса, следуя описанным шагам.`, 

    filesRequires: 
`1. Тест-кейсы: Документ (например, в формате Excel или специализированной системы управления тестами)

2. Отчет о тестировании: Документ или система, куда вносятся результаты тестирования`,

    end: new Date(2025, 0, 17), 
    status: "completed"}


const pageName = document.querySelector('.page-name');
pageName.insertAdjacentHTML('beforeend', task.id);

const taskName = document.querySelector('.task-name');
taskName.innerHTML = task.name;

const taskEnd = document.querySelector('.deadline-value');
taskEnd.innerHTML = task.end.toLocaleDateString();

const taskDescription = document.querySelector('.task-description');
taskDescription.insertAdjacentHTML('beforeend', task.description);

const filesRequires = document.querySelector('.task-files-requires');
filesRequires.insertAdjacentHTML('beforeend', task.filesRequires);