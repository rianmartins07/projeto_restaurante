
    function getListFromAPI(){

        var settings = {
            "url": 'http://127.0.0.1:8000/api/user/user/',
            "method": "GET",
            "timeout": 0,
            "headers" : {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };

        $.ajax(settings).done(function(response){
            console.log(response);
        }).fail(function(response){
            console.log(response);
        })

    }

    getListFromAPI();