$(document).ready(function(){
});

$(function() {
    $('.check_class').change(function() {
        var id = $(this).val();
        if ($(this).is(':checked')) {
            $('#user_pw' + String(id)).attr("type", "text");
        } else {
            $('#user_pw' + String(id)).attr("type", "password");
        }
    });

});
