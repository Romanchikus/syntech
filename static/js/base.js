$(document).ready(function () {
    $('#order_form').hide();
    $('.tables_checked').hide();
}
)


$(document).on('click', '#target', function () {

    var a = $(".hall_schema").children();
    var b = Array()
    for (var i = 0; i < a.length; ++i) {
        if (getComputedStyle(a[i]).getPropertyValue("filter") == 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)') {
            b[i] = true
        } else { b[i] = false }
    }
    count_of_selected = b.reduce(function (a, b) { return b ? ++a : a; }, 0)
    console.log(count_of_selected)

    if (
        $('#order_form').is(":visible") &
        $(this).css('filter') == 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)' &
        count_of_selected < 2) {

        $('#order_form').hide();
        $(this).css('filter', '');
        input_tag = 'input[value='+ $(this).attr( "value" )+']'
        $('.tables_checked').find(input_tag).attr("checked",false);
    }
    else if ($(this).css('filter') == 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)' &
        count_of_selected >= 2) {
        $(this).css('filter', '');
        input_tag = 'input[value='+ $(this).attr( "value" )+']'
        $('.tables_checked').find(input_tag).attr("checked",false);

        selected_li = 'li[id='+ $(this).attr( "value" )+']'
        $('.selected_obj').find(selected_li).css('display', 'none')
    }
    else {
        $('#order_form').show();
        $(this).css('filter', 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)');
        input_tag = 'input[value='+ $(this).attr( "value" )+']'
        $('.tables_checked').find(input_tag).attr("checked",true);

        selected_li = 'li[id='+ $(this).attr( "value" )+']'
        $('.selected_obj').find(selected_li).css('display', '')

        console.log(input_tag)
    }
    // console.log($(".row").children().css('filter', '').css('filter') == 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)' );


    console.log();
});