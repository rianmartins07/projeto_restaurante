$(function(){

    $('#reports').change(function(){
        var report = ($(this).val());

        if(report == 'vendas'){
            $("#view-report").attr("href", "view-report-sales.html");
        } else if(report == 'pedidos'){
            $("#view-report").attr("href", "view-report-requests.html");
        } else if(report == 'clientes'){
            $("#view-report").attr("href", "view-report-customers.html");
        } else if(report == 'tempo'){
            $("#view-report").attr("href", "view-report-time.html");
        } else if(report == 'periodo'){
            $("#view-report").attr("href", "view-report-time-course.html");
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