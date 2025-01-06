const employees = [
    { name: 'John', info: 'My favorite employee', status: 'active' },
    { name: 'Иван', info: 'Мой любимый стажер', status: 'active' },
    { name: 'Александр', info: 'Перспективный стажер', status: 'active' },
    { name: 'Петр', info: 'Племянник босса', status: 'requested' }
]

const employeesElement = document.querySelector('.employees-list');
const employeeTemplate = document.querySelector('.employee-template').content.querySelector('li');
const employeesFragment = document.createDocumentFragment();

employees.forEach(employee => {
    if (employee.status === 'active') {
        const employeeElement = employeeTemplate.cloneNode(true);
        employeeElement.querySelector('.employee-name').textContent = employee.name;
        employeeElement.querySelector('.employee-info').textContent = employee.info;
        employeesFragment.appendChild(employeeElement);
    }
});

employeesElement.appendChild(employeesFragment);