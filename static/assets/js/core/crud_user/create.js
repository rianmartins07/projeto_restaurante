

$('#create_user').click(function (e) {

    let data = new FormData();
    data = get_data();


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


