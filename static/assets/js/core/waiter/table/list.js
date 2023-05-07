var filter = {}

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
        console.log(settings.url);
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



formSearch.addEventListener('keyup', function () {
    let optionSearch = formSearch.querySelector('#optionSearch');
    optionSearch = 'table_number'

    let search = document.querySelector('#search').value;

    
    if (search) {

        filter["offset"] = 0
        var newfilter = {};

        let filter_search = optionSearch + '__icontains';

        if (search) {
            newfilter[filter_search] = search;
        }

        getListObjectFromApi(newfilter);
        
    } else {
        
        getListObjectFromApi();
    }
});
