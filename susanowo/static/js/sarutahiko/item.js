$(document).ready(function(){
    autocompleteGetItemData('#id_id','#id_item_name','/sarutahiko/item_list/',displayDataItemName,0);
    $('#id_item_name').change(function(e) {
        $('#id_item_name_upd').val($('#id_item_name').val());
    });
});

function displayDataItemName(data,row) {
    $('#id_item_name').val(data.item_name);
    $('#id_id').val(data.item_id);
}
