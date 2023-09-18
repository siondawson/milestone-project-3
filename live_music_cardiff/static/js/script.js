$(function () {
    $('#date').datepicker({
        minDate: 0
    });

});

$('.timepicker').timepicker({
    timeFormat: 'h:mm p',
    interval: 30,
    minTime: '7',
    maxTime: '6:00pm',
    defaultTime: '11',
    startTime: '10:00',
    dynamic: false,
    dropdown: true,
    scrollbar: true
});

document.getElementById("year").innerHTML = new Date().getFullYear();
