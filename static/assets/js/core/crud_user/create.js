

$('#create_user').click(function (e) {

    user = $('#id_user').val();
    nome = $('#id_nome').val();
    cpf = $('#id_cpf').val();
    email = $('#id_email').val();
    dtnasc = $('#id_dtnasc').val();
    celular = $('#id_celular').val();
    sexo = $('#id_sexo :selected').text();


    data = new FormData()

    data.append('nome', user)
    data.append('user', nome)
    data.append('cpf', cpf)
    data.append('email', email)
    data.append('sexo', sexo)
    data.append('data_nascimento', dtnasc)
    data.append('numero_celular', celular)



    var settings = {
        "url": 'http://127.0.0.1:8000/api/user/user/',
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
        console.log(response) 
    }).fail(function (response){
        console.log(response)
    });



});


