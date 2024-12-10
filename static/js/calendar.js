const selectedMonth = document.querySelector('.selected-month');
const previousMonthButton = document.querySelector('.previous-month');
const nextMonthButton = document.querySelector('.next-month');
const calendarGrid = document.querySelector('.calendar-grid');
const currentDate = new Date(Date.now());

// Месяц нумеруется с 0
// start и end включительно
const tasks = []



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