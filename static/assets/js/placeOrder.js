$(function(){

    var noticeTable = 0;
    var i = 0;

    var nMesa = localStorage.getItem("nMesa");

    $("h1.nMesa").text("Pedidos da mesa " + nMesa);

    var cont = 0;
    var cont2 = 0;

    var commands = $(".content-commands");

    $(".mesa-single").click((e) => {
        e.stopPropagation();
        $('.place-waiter').fadeIn(100);
    });

    var el = $('body,.closeWindow');

    el.click(function(){
        $('.place-waiter').fadeOut(100);
    });

    $('.place-waiter .box').click(function(e){
        e.stopPropagation();
    });

    $("input[name=take-order]").click(() => {

        var nameOrder = $("input[name=search-order]").val();
        var qtdOrder = $("input[name=qtd-order]").val();

        if(nameOrder == "" || qtdOrder == "" || parseFloat(qtdOrder) <= 0){
            var messageOrder = $(".messageOrder");
            showMessage(messageOrder);
        }
        else{

            cont++;
            cont2++;

            if(cont == 1){
                commands.prepend("<tr class='legendCommands' style='background-color: rgb(179 22 22); color: #fff;'><td>Nome</td><td>Valor unitário</td><td>Qtd.</td><td colspan='2'>Valor total</td></tr>");
            }

            var valueOrder = 20.00;
            var valueTotal = valueOrder * qtdOrder;

            i++;
            commands.append("<tr class='pedido'><td>"+nameOrder+"</td><td>R$"+valueOrder.toFixed(2)+"</td><td>"+qtdOrder+"</td><td class='valueOrderSingle'>R$"+valueTotal.toFixed(2)+"</td><td class='btnRemoveOrder'><i class='fa-solid fa-trash-can'></i></td></tr>");

            $("td.btnRemoveOrder").click(function(){ 

                $(this).closest('.pedido').remove();

                var qtdTd = document.querySelectorAll("tr.pedido");

                if(qtdTd.length == 0){
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

        if(nameOrder == "" || qtdOrder == "" || parseFloat(qtdOrder) <= 0 || /*qtdPeople == "" || parseFloat(qtdPeople) < 0 ||*/ cont2 == 0){
            var messageOrderAll = $(".messageOrderAll");
            showMessage(messageOrderAll);
        }
        else{
            window.location.href = "../tables-waiter/waiter-tables.html";
            noticeTable++;
            localStorage.setItem("noticeTable", noticeTable);
            localStorage.setItem("idMesa", nMesa);
        }
    });

    $(".button-update-profile input").click(() => {
        var messageUpdateProfile = $(".messageUpdateProfile");
        showMessage(messageUpdateProfile);
    });

    function showMessage(val){
        val.fadeIn(800);
        setTimeout(function(){
            val.fadeOut(800);
        },3000);
    }

});