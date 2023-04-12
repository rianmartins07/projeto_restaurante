
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
        console.log(response)
        for (i in response) {
            buildUserList(response[i])
        }


    })

}


function buildUserList(obj) {
    html = `
    
            <tr>
                <td class="priority-1">${obj.nome}</td>
                <td class="priority-3">${obj.numero_celular}</td>
                <td class="priority-4">${obj.email}</td>
                <td class="priority-2">${obj.role}</td>
                <td class="d-flex justify-content-end priority-1">
                    <div class="btn-group">
                        <a href="/home/user/update/">
                            <img src="../../../static/assets/images/3dots.ico"
                                style="width: 20px !important ; height: 20px impr !important;"
                                alt="">
                        </a>
                    </div>
                </td>
            </tr>
    `

    appendList(html)
}

function appendList(html) {

    $('#list_user').append(html);
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
