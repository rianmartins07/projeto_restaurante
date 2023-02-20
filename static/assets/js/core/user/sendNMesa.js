$(function(){

    var mesaSingle = $(".mesa-single");

    mesaSingle.click((e) => {
        var nMesa = e.target;
        var id = nMesa.id;
        localStorage.setItem("nMesa", id);
    });
    
    var noticeTable = localStorage.getItem("noticeTable");
    var idMesa = localStorage.getItem("idMesa");

    if(noticeTable > 0){
        var mesaServiced = $("#"+idMesa+"");
        mesaServiced.addClass("atendida");
    }

});