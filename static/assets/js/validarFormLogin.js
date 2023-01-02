$(function(){

    submitForm();
    focusInput("#inputCpfLogin",".messageCPF");
    focusInput("#inputCodigoLogin",".messageCodigo");

    function submitForm(){

        $(".box-login form").submit(() => {

            var cpf = $("#inputCpfLogin").val();
            var codigo = $("#inputCodigoLogin").val();
    
            if(validarCPF(cpf) == false){
                aplicarCampoInválido(".cpfIncorrect");
                return false;
            }
    
            else if(validarCodigo(codigo) == false){
                aplicarCampoInválido(".codigoIncorrect");
                return false;
            }
    
        });
    }

    function aplicarCampoInválido(val){

        $(val).fadeIn(800);
        setTimeout(function(){
            $(val).fadeOut(800);
        },3000);
    }


    function validarCPF(cpf){

        if(!cpf.match(/^[0-9]{11}$/)){
            return false;
        }
    }

    function validarCodigo(codigo){

        if(!codigo.match(/^[A-Za-z0-9]{6}$/)){
            return false;
        }
    }

    function focusInput(id,val){
        
        $(id).focus(() => {
            $(val).fadeIn(800);
            setTimeout(function(){
                $(val).fadeOut(800);
            },3000);
        });
    }

});