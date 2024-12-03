const selectedMonth = document.querySelector('.selected-month');
const previousMonthButton = document.querySelector('.previous-month');
const nextMonthButton = document.querySelector('.next-month');
const calendarGrid = document.querySelector('.calendar-grid');
const currentDate = new Date(Date.now());

// Месяц нумеруется с 0
// start и end включительно
const tasks = [
    {id: 0, name: "1-дневная задача", description: 'Описание 1', start: new Date(2024, 11, 17), end: new Date(2024, 11, 17), color: "#e7f6fd", status: "completed"},
    {id: 1, name: "1-дневная задача 2", description: 'Описание 2', start: new Date(2024, 11, 17), end: new Date(2024, 11, 17), color: "#71ff53", status: "completed"},
    {id: 2, name: "Задача в рамках 1-й недели", description: 'Описание 3', start: new Date(2024, 11, 19), end: new Date(2024, 11, 22), color: '#ffe8f4', status: "active"},
    {id: 3, name: "Задача на 2 недели", description: 'Описание 4', start: new Date(2024, 11, 3), end: new Date(2024, 11, 13), color: '#fef6e7', status: "active"}
]

function getCalendarDays(year, month) {
    const days = [];
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const startDayOfWeek = (firstDay.getDay() + 6) % 7;
    const endDayOfWeek = lastDay.getDay();
    const lastDateOfPrevMonth = new Date(year, month, 0);
    for (let i = startDayOfWeek; i > 0; i--) {
        days.push(new Date(lastDateOfPrevMonth.getFullYear(), lastDateOfPrevMonth.getMonth(), lastDateOfPrevMonth.getDate() - i + 1));
    }
    for (let day = 1; day <= lastDay.getDate(); day++) {
        days.push(new Date(year, month, day));
    }
    for (let i = 1; days.length % 7 !== 0; i++) {
        days.push(new Date(year, month + 1, i));
    }
    return days;
}

function getDayId(date) {
    const millisecondsSinceEpoch = date.getTime();
    const millisecondsInOneDay = 24 * 60 * 60 * 1000;
    return Math.floor(millisecondsSinceEpoch / millisecondsInOneDay);
}

function fillCalendar(currentDate) {
    // Дни недели
    selectedMonth.textContent = `${currentDate.toLocaleString('ru', { month: 'long' })} ${currentDate.getFullYear()}`;
    calendarGrid.innerHTML = '';
    const weekDayNames = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье'
    ]
    const weekDayNameTemplate = document.querySelector('.day-name-template').content.querySelector('.calendar-header');
    const weekDayNamesFragment = document.createDocumentFragment();
    weekDayNames.forEach(function (weekDay) {
        const dayNameElement = weekDayNameTemplate.cloneNode(true);
        dayNameElement.querySelector('.week-day-name').textContent = weekDay.toUpperCase();
        weekDayNamesFragment.appendChild(dayNameElement);
    });
    calendarGrid.appendChild(weekDayNamesFragment);

    // Контент
    const weekDayTemplate = document.querySelector('.day-template').content.querySelector('.calendar-day');
    const weekDaysFragment = document.createDocumentFragment();
    getCalendarDays(currentDate.getFullYear(), currentDate.getMonth()).forEach(function (date, index) {
        const dayElement = weekDayTemplate.cloneNode(true);
        dayElement.querySelector('.day').textContent = date.getDate();
        if (date.getDay() in [0, 6]) {
            dayElement.classList.add('weekend')
        }
        if (index < 7 && date.getDate() > 20 || index > 20 && date.getDate() < 7) {
            dayElement.classList.add('another-month-day');
        }
        if (getDayId(date) + 1 === getDayId(new Date(Date.now()))) {
            dayElement.classList.add('current-day');
        }
        // Задачи
        tasks.forEach(task => {

            if (getDayId(date) >= getDayId(task.start) && getDayId(date) <= getDayId(task.end)) {
                const taskElement = document.createElement('div');
                taskElement.classList.add('calendar-task');
                taskElement.textContent = task.name;
                taskElement.style.width = `calc(${100 * Math.min(getDayId(task.end) - getDayId(date) + 1, 8 - date.getDay())}% - 4px)`;
                taskElement.style.backgroundColor = task.color;
                taskElement.classList.add('task');
                if (getDayId(date) !== getDayId(task.start) && date.getDay() !== 1) {
                    taskElement.classList.add('invisible');
                }
                dayElement.appendChild(taskElement);
            }
        });

        weekDaysFragment.appendChild(dayElement);
    });
    calendarGrid.appendChild(weekDaysFragment);
}
    

previousMonthButton.addEventListener('click', function () {
    currentDate.setMonth(currentDate.getMonth() - 1);
    fillCalendar(currentDate);
});

nextMonthButton.addEventListener('click', function () {
    currentDate.setMonth(currentDate.getMonth() + 1);
    fillCalendar(currentDate);
});


// Список задач
const tasksListElement = document.querySelector('.tasks-list');
const taskTemplate = document.querySelector('.task-template').content.querySelector('li');


function fillTasksList(date) {
    tasksListElement.innerHTML = '';
    const tasksFragment = document.createDocumentFragment();

    tasks.forEach(task => {

        if (getDayId(date) >= getDayId(task.start) && getDayId(date) <= getDayId(task.end)) {
            taskItem = taskTemplate.cloneNode(true);
            const label = taskItem.querySelector('.task-label');
            const checkbox = taskItem.querySelector('.task-checkbox');
            const checkboxId = 'task-' + task.id;

            checkbox.id = checkboxId;
            label.setAttribute('for', checkboxId)
            label.textContent = task.name;

            if (task.status === 'completed') {
                checkbox.checked = true;
            }


            tasksFragment.appendChild(taskItem);
        }
    })
    tasksListElement.appendChild(tasksFragment);
}

function fill(date=currentDate) {
    fillCalendar(date);
    fillTasksList(date);
}


fill();