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
                        let button = intern.manager_id === null
                            ? `<button class="add-intern-btn" data-id="${intern.id}">Добавить стажера</button>`
                            : `<span>Уже привязан</span>`;
                        list.append(`<li><a href="${intern.profile_url}">${intern.full_name} (${intern.email})</a> ${button}</li>`);
                    });

                    $('.add-intern-btn').on('click', function () {
                        let internId = $(this).data('id');
                        $.ajax({
                            url: addInternUrl.replace('/0/', `/${internId}/`),
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrfToken,
                            },
                            success: function () {
                                alert('Стажер добавлен!');
                                $(`[data-id="${internId}"]`).parent().html('<span>Уже привязан</span>');
                            },
                            error: function () {
                                alert('Ошибка при добавлении стажера.');
                            }
                        });
                    });
                } else {
                    list.append('<li>Стажеры не найдены</li>');
                }
            }
        });
    });
});
