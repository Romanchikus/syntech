$(document).ready(function () {

    if ($( ".ERRORS" ).length ==0){
        $('#order_form').hide();
    }

    $('.tables_checked').hide();

    var a = $(".hall_schema").children();
    hall_h = $(".hall_schema").height()
    hall_w = $(".hall_schema").width()
    hall_pos = $(".hall_schema").position()

    checked_visible()

    for (var i = 0; i < a.length; ++i) {
        $(a[i]).height(hall_h / 100 * $(a[i]).height())
        $(a[i]).width(hall_w / 100 * $(a[i]).width())

        img_pos = $(a[i]).position()

        per_top = hall_pos.top + (hall_h * 0.6) / 100 * img_pos.top
        per_left = hall_pos.left + (hall_w * 0.7) / 100 * img_pos.left

        $(a[i]).css({ top: per_top, left: per_left });
    }
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

    if (
        $('#order_form').is(":visible") &
        $(this).css('filter') == 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)' &
        count_of_selected < 2) {

        $('#order_form').hide();
        $(this).css('filter', '');
        input_tag = 'input[value=' + $(this).attr("value") + ']'
        $('.tables_checked').find(input_tag).attr("checked", false);
    }
    else if ($(this).css('filter') == 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)' &
        count_of_selected >= 2) {
        $(this).css('filter', '');
        input_tag = 'input[value=' + $(this).attr("value") + ']'
        $('.tables_checked').find(input_tag).attr("checked", false);
    }
    else {
        $('#order_form').show();
        $(this).css('filter', 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)');
        input_tag = 'input[value=' + $(this).attr("value") + ']'
        $('.tables_checked').find(input_tag).attr("checked", 'checked');
    }

    checked_visible()

});








function checked_visible() {
    var a = $('.tables_checked').children().children();
    for (var i = 0; i < a.length; ++i) {
        num = $(a[i]).find('input').attr("value")
        if ($(a[i]).find('input').attr("checked") == 'checked' | $(a[i]).find('input').is("[checked]")) {
            selected_li = 'li[id=' + num + ']'
            console.log(selected_li)
            $('.selected_obj').find(selected_li).css('display', '')

            $(this).css('filter', 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)');
            selected_img = 'img[value=' + num + ']'
            $(".hall_schema").find(selected_img).css('filter', 'drop-shadow(rgb(0, 128, 0) 2px 4px 6px)');
        }
        else {
            selected_li = 'li[id=' + num + ']'

            $('.selected_obj').find(selected_li).css('display', 'none')
        }
        // console.log(    selected_li   )
    }
}