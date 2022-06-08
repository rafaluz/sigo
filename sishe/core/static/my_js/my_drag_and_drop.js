    /** help */
function log(message) {
    console.log('> ' + message)
}

/** app */
const cards = document.querySelectorAll('.curricular_component')
const dropzones = document.querySelectorAll('.dropzone')


/** our cards */
cards.forEach(card => {
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)
})

function dragstart() {
    // log('CARD: Start dragging ')
    dropzones.forEach( dropzone => dropzone.classList.add('highlight'))

    // this = card
    this.classList.add('is-dragging')
}

function drag() {
    // log('CARD: Is dragging ')
}

function dragend() {
    // log('CARD: Stop drag! ')
    dropzones.forEach( dropzone => dropzone.classList.remove('highlight'))

    // this = card
    this.classList.remove('is-dragging')

    
    //----------------- codigo do rafa

    dropzone_id = this.parentNode.getAttribute("id")
    weekday = this.parentNode.getAttribute("data-dayOfWeek")
    curricular_component = this.getAttribute("data-curricularComponent")

    url_schedule_create = "/schedule/create"
    $.ajax({
        url: url_schedule_create,
        type: 'post',
        data : { 
            'curricular_component': curricular_component,
            'weekday': weekday,
            'dropzone': dropzone_id,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
        },
        success: function (d) {
            log("deu certo")
            if (d.codigo == 0) {
               log("Cadastrado com sucesso")
            } else if(d.codigo == 1) {
                log("Nada feito")
            };
        }
        });

    // -----------------------



}

// rafa

{% for disciplina in object_list %}
    
    {% for horario in disciplina.schedules.all %}
        dropzones.forEach( dropzone => {
            log("estou aqui")
            if (dropzone.getAttribute("id") == "{{ horario.dropzone }}") {
                log("agora estou aqui")
                dropzone.appendChild(document.querySelector('[data-curricularComponent="{{disciplina.pk}}"]'))
            }
        })
    {% endfor %}
{% endfor %}

    


/** place where we will drop cards */
dropzones.forEach( dropzone => {
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)
})

function dragenter() {
    // log('DROPZONE: Enter in zone ')
}

function dragover() {
    // this = dropzone
    this.classList.add('over')

    // get dragging card
    const cardBeingDragged = document.querySelector('.is-dragging')

    // this = dropzone
    this.appendChild(cardBeingDragged)
}

function dragleave() {
    // log('DROPZONE: Leave ')
    // this = dropzone
    this.classList.remove('over')

}

function drop() {
    // log('DROPZONE: dropped ')
    this.classList.remove('over')
}
