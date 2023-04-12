

$('#button-update-profile').click(function (e) {

    let data = new FormData();
    data = getData();

    
    form_valid = isFormValid()
    if (!form_valid){
        return
    }
    var settings = {
        "url": 'http://127.0.0.1:8000/api/menu/info/' + data.get('id') + '/',
        "method": "PATCH",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken')
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": data,
    };  
    
    
    console.log(settings)

    $.ajax(settings).done(function(response){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: `Criado com Sucesso!!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            preConfirm: () => {
                url = `${location.protocol}//${location.host}/home/menu/list/`;
                window.location.href = url;
            },
            timer: 3000,
            
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



});



