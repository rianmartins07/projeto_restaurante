$(function(){

    $('#reports').change(function(){
        var report = ($(this).val());

        if(report == 'vendas'){
            $("#view-report").attr("href", location.protocol + "//" + location.host + '/home/user/reports/sales/');
        } else if(report == 'pedidos'){
            $("#view-report").attr("href", location.protocol + "//" + location.host + '/home/user/reports/requests/');
        } else if(report == 'clientes'){
            $("#view-report").attr("href", location.protocol + "//" + location.host + '/home/user/reports/customers/');
        } else if(report == 'tempo'){
            $("#view-report").attr("href", location.protocol + "//" + location.host + '/home/user/reports/time/');
        } else if(report == 'periodo'){
            $("#view-report").attr("href", location.protocol + "//" + location.host + '/home/user/reports/time_course/');
        }
    });

    /*----------------------------------*/

    var inputView = $("#view-report");

    inputView.click((e) => {

        var dateIni = $("input[name=date-ini]").val();
        var dateFim = $("input[name=date-fim]").val();

        var nameStrIni = dateIni.split("-");
        var nameStrFim = dateFim.split("-");

        i = 0;
        var anoIni = nameStrIni[i];
        var mesIni = nameStrIni[i + 1];
        var diaIni = nameStrIni[i + 2];

        j = 0;
        var anoFim = nameStrFim[j];
        var mesFim = nameStrFim[j + 1];
        var diaFim = nameStrFim[j + 2];

        if(anoIni > anoFim){
            e.preventDefault();
            showMessage($(".messageDate p"));
        }
        else if(mesIni == mesFim && diaIni > diaFim){
            e.preventDefault();
            showMessage($(".messageDate p"));
        }
        else if(anoIni == anoFim && mesIni > mesFim){
            e.preventDefault();
            showMessage($(".messageDate p"));
        }
        else if(diaIni == diaFim && mesIni == mesFim && anoIni == anoFim){
            var dateStart = diaIni+"/"+mesIni+"/"+anoIni;
            var dateEnd = diaFim+"/"+mesFim+"/"+anoFim;
        }
        else{
            var dateStart = diaIni+"/"+mesIni+"/"+anoIni;
            var dateEnd = diaFim+"/"+mesFim+"/"+anoFim;
        }

        /*--------------*/

        var reportVazio = $('#reports option:selected').val();

        if(reportVazio == "vazio"){
            e.preventDefault();
            showMessage($(".messageSelect p"));
        }

        else if(dateIni == "" || dateFim == ""){
            e.preventDefault();
            showMessage($(".messageDate p"));
        }

        else{
            localStorage.setItem("dateIni", dateStart);
            localStorage.setItem("dateFim", dateEnd);
        }
    });

    function showMessage(val){
        val.fadeIn(800);
        setTimeout(function(){
            val.fadeOut(800);
        },3000);
    }

});