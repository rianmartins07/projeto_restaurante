function processOrder(id) {
    data = new FormData()
    data.append('status', 'EM PREPARO')

    var settings = {
        "url": 'http://127.0.0.1:8000/api/orders/' + id + '/',
        "method": "PATCH",
        "timeout": 0,
        "headers": {
            "X-CSRFToken": getCookie('csrftoken')
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": data,
    };

    if ($('#status_order').html() != 'PEDIDO NA COZINHA') {
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: `Pedido está cancelado ou pronto!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            timer: 2000
        });
    } else {
        $.ajax(settings).done(function (response) {
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: `Pedido em preparação!`,
                showConfirmButton: true,
                confirmButtonColor: '#b31616',
                timer: 2000
            });
            response = JSON.parse(response)
            $('#status_order').html(response.status);
            
        })
    }
}

function finishOrder(id) {
    data = new FormData()
    data.append('status', 'PRONTO')

    var settings = {
        "url": 'http://127.0.0.1:8000/api/orders/' + id + '/',
        "method": "PATCH",
        "timeout": 0,
        "headers": {
            "X-CSRFToken": getCookie('csrftoken')
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": data,
    };

    if ($('#status_order').html() != 'EM PREPARO') {
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: `Pedido não está sendo preparado!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            timer: 2000
        });
    } else {
        $.ajax(settings).done(function (response) {
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: `Pedido pronto!`,
                showConfirmButton: true,
                confirmButtonColor: '#b31616',
                timer: 2000
            });
            response = JSON.parse(response)
            $('#status_order').html(response.status);
            
        })
    }


}

function cancelOrder(id) {

    data = new FormData()
    text_canceled = $('#text_canceled').val();
    data.append('status', 'CANCELADO')
    data.append('canceled_by', text_canceled)
    if (text_canceled.length <= 0){
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: `Motivo não pode ser vazio!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            timer: 2000
        });
        return 0
    }
    
    var settings = {
        "url": 'http://127.0.0.1:8000/api/orders/' + id + '/',
        "method": "PATCH",
        "timeout": 0,
        "headers": {
            "X-CSRFToken": getCookie('csrftoken')
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": data,
    };

    if ($('#status_order').html() == 'PRONTO') {
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: `Pedido não pode ser cancelado!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            timer: 2000
        });
    } else {
        $.ajax(settings).done(function (response) {
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: `Pedido cancelado!`,
                showConfirmButton: true,
                confirmButtonColor: '#b31616',
                timer: 2000
            });
            response = JSON.parse(response)
            $('#status_order').html(response.status);
            
        })
    }

}