
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function isFormValid() {
    var formValid = true;
    $('input,textarea,select').filter('[required]:visible').each(function(){
    var elementError = `${$(this).attr('id')}`
        if ($.trim($(this).val()).length == 0){
            formValid = false;
            $(this).addClass("error");
            var html = '<label id="' + elementError + '-error" class="text-sm m-0 p-0 text-danger" for="' + elementError + '" style="">Campo Obrigatório</label>';
            $('#' + elementError + '-error').remove();
            $(this).after(html);
            scrollTo(this, 0)
        }   
        else{
            $('#' + elementError + '-error').remove();
            $(this).removeClass("error");
        }
    });

    return formValid;
}



function buildURLWithFilter(path, filter={}) {
    var filter_parms = [];

    Object.keys(filter).forEach(function (key) {
        filter_parms.push(key + "=" + filter[key]);
    });

    if (path.endsWith("?")) {
        return path + filter_parms.join("&");
    } else if (path.endsWith("/")) {
        return path + "?" + filter_parms.join("&");
    } else {
        return path + "/?" + filter_parms.join("&");
    }
}