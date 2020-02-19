$(document).ready(function(){
    $('#btnUserList').hide();
});

$(function() {
    $('#id_user_name').change(function() {
        $('#btnUserList').click();
        $('#id_user_id').val($('#id_user_name').val());
    });

    $('#btn_cancel').click(function() {
        history.back();
    });
});
