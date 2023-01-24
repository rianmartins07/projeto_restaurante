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
        mesaServiced.css("background-color","rgb(179 22 22)");
        mesaServiced.css("border-bottom","14px solid rgb(53 53 53)");
    }

});