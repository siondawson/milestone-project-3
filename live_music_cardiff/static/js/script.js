$(function () {
    $('#date').datepicker({
        dateFormat: "dd-mm-yy",
        minDate: 0
    });

});

document.getElementById("year").innerHTML = new Date().getFullYear();