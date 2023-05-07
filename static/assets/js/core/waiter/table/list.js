$(function () {
    getListObjectFromApi()
})

function getListObjectFromApi(filter = '') {
    if (filter == '') {
        var settings = {
            "url": location.protocol + "//" + location.host + '/api/waiter/table',
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    } else {
        var settings = {
            "url": buildURLWithFilter(location.protocol + "//" + location.host + '/api/waiter/table', filter),
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    }

    $.ajax(settings).done(function (response) {
        $('#list_tables').html('');
        
        for (i in response) {
            buildTableList(response[i])
        }


    })
}
function buildTableList(obj){
    html = `<a class="mesa-single" href="${location.protocol}//${location.host}/home/orders/${obj.id}/create/">${obj.table_number}</a>`
        $("#list_tables").append(html);
    
}
