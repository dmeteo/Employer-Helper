let asideNavBar = document.querySelector('.aside-navbar');
let homeLink = document.querySelector('.home-link');
let navLinks = document.querySelectorAll('.nav-link');


$(document).ready(function () {
    function loadNotifications() {
        $.ajax({
            url: "/notifications/",
            success: function (data) {
                let notifications = data.notifications;
                let notificationList = $('#notification-list');
                notificationList.empty();
                if (notifications.length > 0) {
                    notifications.forEach(function (notification) {
                        notificationList.append(`
                            <li>
                                ${notification.message} - ${notification.created_at}
                                <button class="mark-read" data-id="${notification.id}">Отметить как прочитанное</button>
                            </li>
                        `);
                    });
                    attachMarkAsReadHandler();
                } else {
                    notificationList.append('<li>Нет новых уведомлений</li>');
                }
            },
        });
    }

    function attachMarkAsReadHandler() {
        $('.mark-read').on('click', function () {
            let notificationId = $(this).data('id');
            $.ajax({
                url: `/notifications/read/${notificationId}/`,
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                success: function () {
                    loadNotifications(); 
                },
            });
        });
    }

    loadNotifications();

    setInterval(loadNotifications, 30000);
});



asideNavBar.addEventListener('mouseover', function() {
    homeLink.querySelector('h2').hidden = false;
    navLinks.forEach(function(navLink) {
        navLink.querySelector('p').hidden = false;
    })
});

asideNavBar.addEventListener('mouseout', function() {
    homeLink.querySelector('h2').hidden = true;
    navLinks.forEach(function(navLink) {
        navLink.querySelector('p').hidden = true;
    })
});
