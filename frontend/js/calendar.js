const selectedMonth = document.querySelector('.selected-month');
const previousMonthButton = document.querySelector('.previous-month');
const nextMonthButton = document.querySelector('.next-month');
const calendarGrid = document.querySelector('.calendar-grid');

const tasks = [
    {name: "1-дневная задача", start: new Date(2024, 10, 17), end: new Date(2024, 10, 17), color: "#e7f6fd"},
    {name: "Задача в рамках 1-й недели", start: new Date(2024, 10, 19), end: new Date(2024, 10, 22), color: '#ffe8f4'},
    {name: "Задача на 2 недели", start: new Date(2024, 10, 6), end: new Date(2024, 10, 14), color: '#fef6e7'}
]

function getCalendarDays(year, month) {
    const days = [];
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const startDayOfWeek = firstDay.getDay() - 1;
    const endDayOfWeek = lastDay.getDay();
    const lastDateOfPrevMonth = new Date(year, month, 0);
    for (let i = startDayOfWeek; i > 0; i--) {
        days.push(new Date(lastDateOfPrevMonth.getFullYear(), lastDateOfPrevMonth.getMonth(), lastDateOfPrevMonth.getDate() - i + 1)); // последние дни предыдущего месяца
    }
    for (let day = 1; day <= lastDay.getDate(); day++) {
        days.push(new Date(year, month, day));
    }
    for (let i = 1; days.length % 7 !== 0; i++) {
        days.push(new Date(year, month + 1, i));
    }
    return days;
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
        if (date.getFullYear() === currentDate.getFullYear() && date.getMonth() === currentDate.getMonth() && date.getDate() === currentDate.getDate()) {
            dayElement.classList.add('current-day');
        }
        // Задачи
        tasks.forEach(task => {
            if (date.getTime() >= task.start.getTime() && date.getTime() <= task.end.getTime()) {
                const taskElement = document.createElement('div');
                taskElement.classList.add('calendar-task');
                taskElement.textContent = task.name;
                
                // Если у сроков задач добавится время, нужно будет getTime заменить на дату
                if (date.getTime() === task.start.getTime() || index == 0) {
                    taskElement.classList.add('calendar-task-start');
                }
                if (date.getTime() === task.end.getTime()) {
                    taskElement.classList.add('calendar-task-end');
                }
                taskElement.style.backgroundColor = task.color;
                taskElement.classList.add('task');
                dayElement.appendChild(taskElement);
            }
        });

        weekDaysFragment.appendChild(dayElement);
    });
    calendarGrid.appendChild(weekDaysFragment);

}
    

const currentDate = new Date(Date.now());
fillCalendar(currentDate);

previousMonthButton.addEventListener('click', function () {
    currentDate.setMonth(currentDate.getMonth() - 1);
    fillCalendar(currentDate);
});

nextMonthButton.addEventListener('click', function () {
    currentDate.setMonth(currentDate.getMonth() + 1);
    fillCalendar(currentDate);
});