

$(function(){
    var settings = {
        "url": 'http://127.0.0.1:8000/api/menu/info/',
        "method": "GET",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken')
        },
    };  
    
    
    
    
    $.ajax(settings).done(function(response){
        console.log(response)
        for (i in response){
            buildMenuList(response[i])
        }

        
    }).fail(function (response){
        console.log(response)
    });
})


function buildMenuList(obj){
    html = `
    
        <a href="../${obj.id}/update/" class="list-menu-single">
            <div class="info-menu">  
                <img src='${obj.foto}' alt="img">
                <!--<div class="img-menu"></div>-->
                <h2>${obj.nome} - R$ ${obj.valor}</h2>
            </div><!--info-menu-->
            <h2>${obj.status}</h2>
        </a><!--list-menu-single-->
    
    
    `

    
    appendList(html)
}

function appendList(html){
    
    $('#list_menu').append(html);
}