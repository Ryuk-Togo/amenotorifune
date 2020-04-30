$(document).ready(function(){
    $('#btnPlaceList').hide();
});

$(function() {
    $('#id_place_name').change(function() {
        $('#btnPlaceList').click();
        $('#id_place_id').val($('#id_place_name').val());
    });

    $('#btn_cancel').click(function() {
        history.back();
    });
});
