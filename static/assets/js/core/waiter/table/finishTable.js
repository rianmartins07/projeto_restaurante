function finishTable (id){
    var settings = {
        "url": 'http://127.0.0.1:8000/api/waiter/table/' + id + '/finish/',
        "method": "PATCH",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken')
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
    };  

    Swal.fire({
        title: 'Deseja finalizar a mesa?',
        showDenyButton: true,
        confirmButtonText: 'Sim!',
        confirmButtonColor: '#b31616',
        cancelButtonColor: '#b31616',
        denyButtonText: `Não`,
      }).then((result) => {
        if (result.isConfirmed) {
                $.ajax(settings).done(function(response){
                    
                    Swal.fire({
                        position: 'center',
                        icon: 'success',
                        title: `Mesa finalizada com sucesso!`,
                        showConfirmButton: true,
                        confirmButtonColor: '#b31616',
                        timer: 3000,
                        
                    });
                }).fail(function (response){
                    
                    Swal.fire({
                        position: 'center',
                        icon: 'error',
                        title: `Erro!`,
                        text: JSON.parse(response.responseText).error,
                        showConfirmButton: true,
                        confirmButtonColor: '#b31616',
                        timer: 3000
                    });
                });
            
        } else if (result.isDenied) {

        }
      })
}

    

