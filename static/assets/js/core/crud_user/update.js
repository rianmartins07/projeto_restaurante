function updateUser (id){
    data = new FormData()
    data = getData()

    form_valid = isFormValid()
    if (!form_valid){
        return
    }
    var settings = {
        "url": 'http://127.0.0.1:8000/api/user/info/' + id + '/',
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
    
    
  

    $.ajax(settings).done(function(response){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: `Atualizado com sucesso!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            preConfirm: () => {
                url = `${location.protocol}//${location.host}/home/user/list/`;
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

}