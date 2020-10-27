$(function () {
    $.datepicker.setDefaults({
        minDate: new Date(),
    });
    $("#id_check_in").datepicker({
        onSelect: function (selectedDate) {
            var date = $(this).datepicker("getDate");
            if (date) {
                date.setDate(date.getDate() + 1);
            }
            $("#id_check_out").datepicker("option", "minDate", date || new Date());
        },
    });
    $("#id_check_out").datepicker({
        onSelect: function (selectedDate) {
            var date = $(this).datepicker("getDate");
            if (date) {
                date.setDate(date.getDate() - 1);
            }
            $("#id_check_in").datepicker("option", "maxDate", date);
        },
    });
});