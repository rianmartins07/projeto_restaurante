
var formSearch = document.querySelector('#formSearch')

var filter = {
    "order_by": "status",
}

$(function () {
    getListObjectFromApi()
    
})

function getListObjectFromApi(filter) {
    if (filter == '') {
        var settings = {
            "url": location.protocol + "//" + location.host + '/api/orders',
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    } else {
        var settings = {
            "url": buildURLWithFilter(location.protocol + "//" + location.host + '/api/orders', filter),
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    }
    $.ajax(settings).done(function (response) {
        $('#table_wait').html('');
        $('#table_requested').html('');
        $('#table_finished').html('');
        console.log(response)
        for (i in response) {
            buildOrders(response[i])
        }


    })

}

function buildOrders(obj){

    html=`<a class="mesa-single" href="home/orders/${obj.id_order}/view/">${obj.table_number}</a>`
    if (obj.status == 'PEDIDO NA COZINHA'){
        $("#table_requested").append(html);
    }else if (obj.status == 'EM PREPARO'){
        $("#table_wait").append(html);
    }else if (obj.status == 'PRONTO'){
        $('#table_finished').append(html);
    }

    



}