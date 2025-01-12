$(document).ready(function () {
    $('#search-box').on('input', function () {
        let query = $(this).val();
        $.ajax({
            url: searchInternsUrl,
            data: { q: query },
            success: function (data) {
                let results = data.results;
                let list = $('#interns-list');
                list.empty();
                if (results.length > 0) {
                    results.forEach(function (intern) {
                        urlTask = addTaskForInternUrl.replace('/0/', `/${intern.slug}/`),
                        list.append(`<li><a href="${intern.profile_url}">${intern.full_name} (${intern.email})</a>
                            <a href=${urlTask}>Поставить задачу</a></li>`);
                    });
                } else {
                    list.append('<li>У вас нет стажеров</li>');
                }
            }
    });
    });
});