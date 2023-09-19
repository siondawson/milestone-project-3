$(function () {
    $('#date').datepicker({
        minDate: 0
    });

});

$('.timepicker').timepicker({ // timepicker from https://timepicker.co/
    timeFormat: 'HH:mm',
    interval: 30,
    minTime: '7',
    maxTime: '11:30pm',
    defaultTime: '19',
    startTime: '6:00',
    dynamic: false,
    dropdown: true,
    scrollbar: true
});

document.getElementById("year").innerHTML = new Date().getFullYear();
