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
    const employeeElement = employeeTemplate.cloneNode(true);
    employeeElement.querySelector('.employee-name').textContent = employee.name;
    employeeElement.querySelector('.employee-info').textContent = employee.info;

    employeeElement.addEventListener('click', () => {
        // TODO: Переход на страницу со стажером
    });
    
    if (employee.status ==='requested') {
        employeeElement.classList.add('requested');
        
        const linkEmployeeButton = document.createElement('button');
        linkEmployeeButton.classList.add('link-employee-button');
        linkEmployeeButton.textContent = 'Привязать стажера';

        linkEmployeeButton.addEventListener('click', () => {
            // TODO: Привязать стажера
        })

        employeeElement.appendChild(linkEmployeeButton);
    }

    employeesFragment.appendChild(employeeElement);
});

employeesElement.appendChild(employeesFragment);