function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function SendFile(inputElement) {
    const file = inputElement.files[0];
    const fileURL = URL.createObjectURL(file);

    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const month = (now.getMonth() + 1).toString().padStart(2, '0'); // getMonth() возвращает месяц от 0 (январь) до 11 (декабрь)
    const year = now.getFullYear();

    const time = `${hours}:${minutes}ㅤ${day}.${month}.${year}`;

    const formData = new FormData();
    formData.append('room_id', document.getElementById('roomid').textContent);
    formData.append('filee', file);
    formData.append('time', time);


    return fetch('/save_files_url/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const note_container = document.getElementsByClassName('note_container')[0];

        const note = document.createElement('div');
        note.className = 'note';

        const note_text = document.createElement('p');
        note_text.className = 'note_text';
        note_text.textContent = file.name;
        note.appendChild(note_text);

        const note_text_date = document.createElement('p');
        note_text_date.className = 'note_text_date';
        note_text_date.textContent = time;
        note.appendChild(note_text_date);

        const load_but = document.createElement('button');
        load_but.className = 'but';
        load_but.id = 'load_but';
        load_but.addEventListener('click', function() {
            const fileUrl = 'media/files/' + get_text(this);

            // Создаем временную ссылку для загрузки
            const tempLink = document.createElement('a');
            tempLink.href = fileUrl;
            tempLink.setAttribute('download', get_text(this));

            // Добавляем ссылку в DOM и клинаем по ней
            document.body.appendChild(tempLink);
            tempLink.click();

            // Удаляем временную ссылку из DOM
            document.body.removeChild(tempLink);
        });
        note.appendChild(load_but);

        const delete_but = document.createElement('button');
        delete_but.className = 'but';
        delete_but.id = 'delete_but';
        delete_but.addEventListener('click', function() {
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                    }
                }
            });

            $.ajax({
                url: '/delete_file/',  // Замените на свой URL-адрес
                type: 'POST',
                data: {
                    // Передаем параметры, необходимые для удаления элемента
                    room_id: parseInt(room_id),
                    file: get_text(this)
                },
                success: function(response) {
                    // Обработка успешного ответа от сервера
                    console.log('Элемент успешно удален!');
                },
                error: function(xhr, errmsg, err) {
                    // Обработка ошибки
                    console.log('Ошибка удаления элемента!');
                }
            });

            del_file(this);
        });
        note.appendChild(delete_but);
        note_container.appendChild(note);
    })
    .catch(error => {
        console.error('Error:', error);
        // Не добавляем элемент 'note' на страницу в случае ошибки
    });
}


function del_file(element) {
    // Получение родительского элемента
    var parentDiv = element.parentNode;

    // Добавление класса clickedball ко всем дочерним элементам
    for (var i = 0; i < parentDiv.children.length; i++) {
        parentDiv.children[i].remove();
    }

    // Добавление класса clickedball к самому div
    parentDiv.remove();
}


function get_text(element) {
    var parentDiv = element.parentNode;
    return parentDiv.querySelector('.note_text').textContent;
}
