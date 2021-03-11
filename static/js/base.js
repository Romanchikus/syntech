$(document).ready(function () {
    $('#order_form').hide();
    // $(".row").children().css('filter', '');
}
)


$(document).on('click', '#target', function () {

    var a = $(".row").children();
    var b = Array()
    for (var i = 0; i < a.length; ++i) {
        if (getComputedStyle(a[i]).getPropertyValue("filter") == 'drop-shadow(rgb(0, 0, 0) 2px 4px 6px)') {
            b[i] = true
        } else { b[i] = false }
    }
    count_of_selected = b.reduce(function (a, b) { return b ? ++a : a; }, 0)

    if (
        $('#order_form').is(":visible") &
        $(this).css('filter') == 'drop-shadow(rgb(0, 0, 0) 2px 4px 6px)' &
        count_of_selected < 2) {

        $('#order_form').hide();
        $(this).css('filter', '');
    }
    else if ($(this).css('filter') == 'drop-shadow(rgb(0, 0, 0) 2px 4px 6px)' &
        count_of_selected >= 2) {
        $(this).css('filter', '');
    }
    else {
        $('#order_form').show();
        $(this).css('filter', 'drop-shadow(rgb(0, 0, 0) 2px 4px 6px)');
    }
    // console.log($(".row").children().css('filter', '').css('filter') == 'drop-shadow(rgb(0, 0, 0) 2px 4px 6px)' );


    console.log();
});