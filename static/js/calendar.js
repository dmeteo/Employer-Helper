const selectedMonth = document.querySelector('.selected-month');
const previousMonthButton = document.querySelector('.previous-month');
const nextMonthButton = document.querySelector('.next-month');
const calendarGrid = document.querySelector('.calendar-grid');
const currentDate = new Date(Date.now());

const tasks = JSON.parse(JSON.parse(document.getElementById('tasks').textContent));
console.log(tasks)

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
        let datee = getDayId(date);
        if (date.getDay() in [0, 6]) {
            dayElement.classList.add('weekend')
        }
        if (index < 7 && date.getDate() > 20 || index > 20 && date.getDate() < 7) {
            dayElement.classList.add('another-month-day');
        }
        if (datee + 1 === getDayId(new Date(Date.now()))) {
            dayElement.classList.add('current-day');
        }
        // Задачи
        let len = tasks.length;
        let i = 0;
        while (i < len) {
            let deadline = getDayId(new Date(tasks[i].fields.deadline));
            let date_start = getDayId(new Date(tasks[i].fields.date_start));
            console.log(len, i)

            if (datee >= date_start && datee <= deadline) {
                const taskElement = document.createElement('div');
                console.log(tasks[i])
                taskElement.classList.add('calendar-task');
                taskElement.textContent = tasks[i].fields.title;
                taskElement.style.width = `calc(${100 * Math.min(deadline - datee + 1, 8 - date.getDay())}% - 4px)`;
                taskElement.style.backgroundColor = "#ccc5f9";
                taskElement.classList.add('task');
                if (datee !== date_start && date.getDay() !== 1) {
                    taskElement.classList.add('invisible');
                }
                dayElement.appendChild(taskElement);
            }
            i++;
        };

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

    let len = tasks.length;
    let i = 0;
    while (i < len) {
        console.log(tasks[i])

        if (getDayId(date) >= getDayId(new Date(tasks[i].fields.date_start)) && getDayId(date) <= getDayId(new Date(tasks[i].fields.deadline))) {
            taskItem = taskTemplate.cloneNode(true);
            const label = taskItem.querySelector('.task-label');
            const checkbox = taskItem.querySelector('.task-checkbox');
            const checkboxId = 'task-' + tasks[i].fields.id;

            checkbox.id = checkboxId;
            label.setAttribute('for', checkboxId)
            label.textContent = tasks[i].fields.title;

            if (tasks[i].fields.status === "True") {
                checkbox.checked = true;
            }


            tasksFragment.appendChild(taskItem);
        }
        i++;
    }
    tasksListElement.appendChild(tasksFragment);
}

function fill(date=currentDate) {
    fillCalendar(date);
    fillTasksList(date);
}


fill();