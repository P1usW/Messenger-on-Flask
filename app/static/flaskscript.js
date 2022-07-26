"use strict"
function translate(sourceElem, destElem, language) {
    $(destElem).html("<img src='{{ url_for('static', filename='loading.gif') }}'>");
    $.post('/translate', {
        text: $(sourceElem).text(),
        target_language: language,
    }).done(function(response) {
        $(destElem).text(response)
    }).fail(function() {
        $(destElem).text("{{ _('Error: Could not contact server.') }}");
    });
}

$(function() {
    let timer = null;
    let xhr = null;
    $('.user_popup').hover(
        function(event) {
            // обработчик события mouse in
            //извлекаю элемент используя event.currentTarget
            let elem = $(event.currentTarget);
            timer = setTimeout(function() {
                timer = null;
                xhr = $.ajax(
                    '/user/' + elem.first().text().trim() + '/popup').done(
                        function(data) {
                            //  здесь создаём и отображаем всплывающее окно
                            xhr = null;
                            elem.popover({
                                trigger: 'manual',
                                html: true,
                                animation: true,
                                container: elem,
                                content: data
                            }).popover('show');
                            flask_moment_render_all();
                        }
                    );
            }, 1000);
        },
        function(event) {
            // mouse out event handler
            let elem = $(event.currentTarget);
            if (timer) {
                clearTimeout(timer);
                timer = null;
            }
            else if (xhr) {
                //.abort() остановит запрос до его завершения.
                xhr.abort();
                xhr = null;
            }
            else {
                elem.popover('destroy');
            }
        }
    )
});

function set_message_count(n) {
    $('#message_count').text(n);
    $('#message_count').css('visibility', n ? 'visible' : 'hidden');
}

{% if current_user.is_authenticated %}
$(function() {
    let since = 0;
    setInterval(function() {
        $.ajax('{{ url_for('main.notifications') }}?since=' + since).done(
            function(notifications) {
                for (let i = 0; i < notifications.length; i++) {
                    if (notifications[i].name == 'unread_message_count')
                        set_message_count(notifications[i].data);
                    since = notifications[i].timestamp;
                }
            }
        );
    }, 10000);
});
{% endif %}