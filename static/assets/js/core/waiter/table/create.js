function createTable(){
    data = getData()

    var settings = {
        "url": 'http://127.0.0.1:8000/api/waiter/table/',
        "method": "POST",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken')
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": data,
    };


    $.ajax(settings).done(function(response){
        
        buildTableOfObjects(JSON.parse(response))
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: `Criado com Sucesso!!`,
            confirmButtonColor: '#b31616',
            showConfirmButton: true,
            preConfirm: () => {
                url = `${location.protocol}//${location.host}/home/waiter/tables_operator/`;
                window.location.href = url;
            },
            timer: 3000
        }); 
    }).fail(function (response){
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: `Erro!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            timer: 3000
        });
    });

}

function buildTableOfObjects(obj) {
        html = `<a class="mesa-single" href="update/${obj.id}">${obj.table_number}</a>`
        $("#list_tables").append(html);
    

}


