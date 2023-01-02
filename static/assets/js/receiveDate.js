$(function(){
    var dateStart = localStorage.getItem("dateIni");
    var dateEnd = localStorage.getItem("dateFim");


    $(".time-course p span:nth-of-type(1)").text(dateStart);
    $(".time-course p span:nth-of-type(2)").text(dateEnd);

});