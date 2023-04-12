

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
        for (i in response){
            buildMenuList(response[i])
        }
    })
})




function getListObjectFromApi(filter = '') {
    if (filter == '') {
        var settings = {
            "url": location.protocol + "//" + location.host + '/api/menu/info/',
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    } else {
        var settings = {
            "url": buildURLWithFilter(location.protocol + "//" + location.host + '/api/menu/info/', filter),
            "method": "GET",
            "timeout": 0,
            "headers": {
                "X-CSRFToken": getCookie('csrftoken')
            },
        };
    }
    $.ajax(settings).done(function (response) {
        $('#list_menu').html('');
        
        for (i in response) {
            buildMenuList(response[i])
        }


    })

}



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

formSearch.addEventListener('keyup', function () {
    let optionSearch = formSearch.querySelector('#optionSearch');
    optionSearch = 'nome'

    let search = formSearch.querySelector('#search').value;

    let last_offset = filter["offset"]
    if (search) {

        filter["offset"] = 0
        var newfilter = {};

        let filter_search = optionSearch + '__icontains';

        if (search) {
            newfilter[filter_search] = search;
        }

        getListObjectFromApi(newfilter);
        filter["offset"] = last_offset
    } else {
        filter["offset"] = last_offset
        getListObjectFromApi();
    }
});
