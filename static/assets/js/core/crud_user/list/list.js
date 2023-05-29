
var formSearch = document.querySelector('#formSearch')

var filter = {
    "order_by": "last_update",
}

$(function () {
    getListObjectFromApi(filter)
})

function getListObjectFromApi(filter) {
    if (filter == '') {
        var settings = {
            "url": location.protocol + "//" + location.host + '/api/user/info/',
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    } else {
        var settings = {
            "url": buildURLWithFilter(location.protocol + "//" + location.host + '/api/user/info/', filter),
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    }
    $.ajax(settings).done(function (response) {
        $('#list_user').html('');
        
        for (i in response) {
            buildUserList(response[i])
            console.log(response[i])
        }


    })

}


function buildUserList(obj) {
    
    html = `
    <tr>
    <td class="priority-1">${obj.full_name}</td>
    <td class="priority-3">${obj.numero_celular}</td>
    <td class="priority-4">${obj.email}</td>
    <td class="priority-2">${obj.group_name}</td>
    <td class="d-flex justify-content-end priority-1">
        <div class="btn-group">
            <button type="button" class="btn btn-icon btn-trigger "  style="background-color: transparent !important" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <em class="fas fa-ellipsis-h"></em>
            </button>
            <div class="dropdown-menu dropdown-menu-right">
                <a class="dropdown-item" href="${obj.id}/update/">
                    <em class="fas fa-edit"></em><span>Editar</span>
                </a>
                <a class="dropdown-item" href="#" onclick="deleteUser(${obj.id})">
                    <em class="fas fa-trash"></em><span>Excluir</span>
                </a>

            </div>
        </div>
        
        
        </td>
    </tr>
    `

    appendList(html)
}

function appendList(html) {

    $('#list_user').append(html);
}


function deleteUser(id) {
    let settings = {
        "url": location.protocol + "//" + location.host + '/api/user/info/' + id + '/',
        "method": "DELETE",
        "timeout": 0,
        "headers": {
            "X-CSRFToken": getCookie('csrftoken')
        },
    };


    Swal.fire({
        title: 'Voce quer realmente exluir?',
        showDenyButton: true,

        confirmButtonText: 'Sim!',
        confirmButtonColor: '#b31616',
        cancelButtonColor: '#b31616',
        denyButtonText: `Não`,
      }).then((result) => {
        if (result.isConfirmed) {
            $.ajax(settings).done(function (){
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: `Excluido com sucesso`,
                    showConfirmButton: true,
                    confirmButtonColor: '#b31616',
                    timer: 3000
                });
                getListObjectFromApi();
            })
        } else if (result.isDenied) {

        }
      })

}

formSearch.addEventListener('keyup', function () {
    let optionSearch = formSearch.querySelector('#optionSearch');
    optionSearch = optionSearch.options[optionSearch.selectedIndex].value;

    let search = formSearch.querySelector('#search').value;

    let last_offset = filter["offset"]
    if (search) {

        filter["offset"] = 0
        var newfilter = {};

        let filter_search = optionSearch + '__icontains';

        if (search) {
            newfilter[filter_search] = search;
        }

        getListObjectFromApi(newfilter);
        filter["offset"] = last_offset
    } else {
        filter["offset"] = last_offset
        getListObjectFromApi();
    }
});
