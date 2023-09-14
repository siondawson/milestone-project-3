const { event } = require('jquery');

$(function () {
    $('#date').datepicker({
        minDate: 0
    });

});

document.getElementById("year").innerHTML = new Date().getFullYear();

document.querySelectorAll("a").forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        
    });
});