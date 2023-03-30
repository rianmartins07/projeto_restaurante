$(function(){

    showMenu();
    showBox();

    function showMenu(){
        $("#icon-menu").click(function(){
            $(".menu-perfil-mobile nav").slideToggle(100);
        });
    }

    function showBox(){

        verifyButton();

        $(".esqueci-codigo").click((e) => {
            e.stopPropagation();
            $(".esqueciSenha").fadeIn(200);
        });

        function verifyButton(){
            var aux = $("body, .iconClose");

            aux.click(function(){
                $('.esqueciSenha').fadeOut(100);
            });
    
            $('.boxSenha').click(function(e){
                e.stopPropagation();
            });
        }    
    }
    
});


