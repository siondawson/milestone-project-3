$(function () {
    $('#date').datepicker({
        minDate: 0
    });

});

document.getElementById("year").innerHTML = new Date().getFullYear();
