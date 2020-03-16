$(document).ready(function(){
});

$(function() {
    // 翌月
    $('#plus_month').click(function() {
        $('#add_month').val(1);
    });

    // 前月
    $('#minus_month').click(function() {
        $('#add_month').val(-1);
    });

});
