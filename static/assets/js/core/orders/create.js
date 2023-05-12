

$(function () {

    //var noticeTable = 0;
    var i = 0;

    //var nMesa = localStorage.getItem("nMesa");

    //$("h1.nMesa").text("Pedidos da mesa "/* + nMesa*/);

    var cont = 0;
    var cont2 = 0;

    var commands = $("#content-commands");

    /*$(".mesa-single").click((e) => {
        e.stopPropagation();
        $('.place-waiter').fadeIn(100);
    });

    var el = $('body,.closeWindow');

    el.click(function(){
        $('.place-waiter').fadeOut(100);
    });

    $('.place-waiter .box').click(function(e){
        e.stopPropagation();
    });*/

    $("input[name=take-order]").click(() => {

        var nameOrder = $("#menu_select").val();
        var qtdOrder = $("input[name=qtd-order]").val();

        if (nameOrder == "" || qtdOrder == "" || parseFloat(qtdOrder) <= 0) {
            var messageOrder = $(".messageOrder");
            showMessage(messageOrder);
        }
        else {

            cont++;
            cont2++;

            if (cont == 1) {
                commands.prepend("<tr class='legendCommands' style='background-color: rgb(179 22 22); color: #fff;'><td>Nome</td><td>Valor unitário</td><td>Qtd.</td><td colspan='2'>Valor total</td></tr>");
            }

            var valueOrder = Number($("#menu_select :selected").attr('price'));
            var valueTotal = valueOrder * qtdOrder;
            let id = $("#menu_select :selected").attr('id')
            let table = $("#menu_select :selected").attr('table')


            i++;
            commands.append("<tr class='pedido' id=" + id + " table="+table+"  quantity="+ qtdOrder+"><td>" + nameOrder + "</td><td>R$" + valueOrder.toFixed(2) + "</td><td>" + qtdOrder + "</td><td class='valueOrderSingle'>R$" + valueTotal.toFixed(2) + "</td><td class='btnRemoveOrder'><i class='fa-solid fa-trash-can'></i></td></tr>");

            $("td.btnRemoveOrder").click(function () {

                $(this).closest('.pedido').remove();

                var qtdTd = document.querySelectorAll("tr.pedido");

                if (qtdTd.length == 0) {
                    $(".legendCommands").html(" ");
                    cont = 0;
                }

                return false;
            });

        }
    });

    $("#submit-commands").click(() => {

        var nameOrder = $("#search-order").val();
        var qtdOrder = $("#qtd-order").val();
        //var qtdPeople = $("#qtd-people").val();

        if (nameOrder == "" || qtdOrder == "" || parseFloat(qtdOrder) <= 0 || /*qtdPeople == "" || parseFloat(qtdPeople) < 0 ||*/ cont2 == 0) {
            var messageOrderAll = $(".messageOrderAll");
            showMessage(messageOrderAll);
        }
        /*else{
            window.location.href = "../tables-waiter/waiter-tables.html";
            noticeTable++;
            localStorage.setItem("noticeTable", noticeTable);
            localStorage.setItem("idMesa", nMesa);
        }*/
    });

    $(".button-end input").click(() => {
        var messageOrderEnd = $(".messageEndOrder");
        showMessage(messageOrderEnd);
    });

    $(".button-update-profile input").click(() => {
        var messageUpdateProfile = $(".messageUpdateProfile");
        showMessage(messageUpdateProfile);
    });

    function showMessage(val) {
        val.fadeIn(800);
        setTimeout(function () {
            val.fadeOut(800);
        }, 3000);
    }

});

function getData() {

        let JSON = new Array()
        $("#content-commands .pedido").each(function (index, element) {
            obj = {
                "dish":`${$(element).attr("id")}`,
                "quantity": `${$(element).attr("quantity")}`,
                "table": `${$(element).attr("table")}`,
                "waiter": 4,
            }
            JSON.push(obj)

        });

        return JSON
}

function createOrder(){
    data = getData()
    
    var settings = {
        "url": `${location.protocol}//${location.host}/api/orders/`,
        "method": "POST",
        "timeout": 0,
        "headers" : {
            "X-CSRFToken": getCookie('csrftoken'),
            "Content-Type": "application/json",
        },
        "data": JSON.stringify(data),
    };  
    

    $.ajax(settings).done(function(response){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: `Criado com Sucesso!!`,
            showConfirmButton: true,
            confirmButtonColor: '#b31616',
            preConfirm: () => {
                url = `${location.protocol}//${location.host}/home/waiter/tables_operator/`;
                window.location.href = url;
            },
            timer: 3000,
            
        });
    }).fail(function (response){
        console.log(response)
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
$("#menu").select2();