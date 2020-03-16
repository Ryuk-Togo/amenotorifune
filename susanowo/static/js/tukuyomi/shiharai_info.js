$(document).ready(function(){
});

$(function() {
    // 編集
    $('.submenu_shiharai').change(function() {
        if ($(this).val() != '') {
            window.location.href = $(this).val();
        }
    });
});
