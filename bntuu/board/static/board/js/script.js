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

function displayImage(inputElement) {
    const file = inputElement.files[0];
    const imageURL = URL.createObjectURL(file);
    const imageContainer = document.getElementById('imageContainer');
    const imgElement = document.createElement('img');
    imgElement.id = 'ball';
    imgElement.src = imageURL;
    imgElement.alt = 'Превью изображения';

    imgElement.onload = function () {
        URL.revokeObjectURL(imageURL);
        imageContainer.appendChild(imgElement);
        performActions();
    };

    const formData = new FormData();
    formData.append('room_id', document.getElementById('roomid').textContent);
    formData.append('src', imageURL);
    formData.append('image', file);

    fetch('/save_img_url/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Обработка результатов после запроса
    })
    .catch(error => console.error('Error:', error));
}




function showMenu() {
  var tarea = document.getElementById("textInput");
  tarea.value = '';
  var menu = document.getElementById("menu");
  menu.style.display = "flex";
  tarea.focus();

}

function create() {
  const imageContainer = document.getElementById('imageContainer');
  const pElement = document.createElement('p');
  pElement.id = 'ball';
  pElement.className = 'ptext'
  pElement.textContent = document.getElementById('textInput').value;

  imageContainer.appendChild(pElement);
  performActions();

  var menu = document.getElementById("menu");
  menu.style.display = "none";
}

function performActions() {
  const ball = document.getElementById('ball');
  ball.style.opacity = 1;

  ball.addEventListener('mousedown', onMouseDown);
  ball.addEventListener('dragstart', onDragStart);

  function onMouseDown(event) {
    this.classList.toggle('clickedball');
    let shiftX = event.clientX - ball.getBoundingClientRect().left;
    let shiftY = event.clientY - ball.getBoundingClientRect().top;

    ball.style.position = 'absolute';
    ball.style.zIndex = 1;

    document.body.append(ball);

    moveAt(event.pageX, event.pageY);

    function moveAt(pageX, pageY) {
      ball.style.left = pageX - shiftX + 'px';
      ball.style.top = pageY - shiftY + 'px';
    }

    function onMouseMove(event) {
      moveAt(event.pageX, event.pageY);
    }

    document.addEventListener('mousemove', onMouseMove);

    ball.onmouseup = function () {
      document.removeEventListener('mousemove', onMouseMove);
      ball.onmouseup = null;
    };
  }

  function onDragStart(event) {
    event.preventDefault();
  }
}

