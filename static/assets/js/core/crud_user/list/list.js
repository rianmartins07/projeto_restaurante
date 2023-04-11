

$(function(){
    var settings = {
        "url": 'http://127.0.0.1:8000/api/user/info/',
        "method": "GET",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken')
        },
    };  
    
    
    
    
    $.ajax(settings).done(function(response){
        console.log(response)
        for (i in response){
            buildUserList(response[i])
        }

        
    }).fail(function (response){
        console.log(response)
    });
})


function buildUserList(obj){
    html = `
    
            <tr>
                <td class="priority-1">${obj.nome}</td>
                <td class="priority-3">${obj.numero_celular}</td>
                <td class="priority-4">${obj.email}</td>
                <td class="priority-2">${obj.role}</td>
                <td class="d-flex justify-content-end priority-1">
                    <div class="btn-group">
                        <a href="/home/user/update/">
                            <img src="../../../static/assets/images/3dots.ico"
                                style="width: 20px !important ; height: 20px impr !important;"
                                alt="">
                        </a>
                    </div>
                </td>
            </tr>
            
    
    `

    
    appendList(html)
}

function appendList(html){
    console.log('oi')
    $('#list_user').append(html);
}