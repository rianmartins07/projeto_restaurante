$(function(){

    openWindow();
    verifyButton();

    function openWindow(){

        $('#cancelOrder').click(function(e){
            e.stopPropagation();
            $('.cancel-order').fadeIn(100);
        });

    }

    function verifyButton(){

        var el = $('body,.close-window,#fechar');

        el.click(function(){
            $('.cancel-order').fadeOut(100);
        });

        $('.box-cancel-order').click(function(e){
            e.stopPropagation();
        });
    }

});