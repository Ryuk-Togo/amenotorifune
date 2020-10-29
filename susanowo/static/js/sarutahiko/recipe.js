function displayDataRecipeName(data) {
    $('#recipe_id').val(data.code);
    $('#id_url').val(data.url);
    // for (let i=0; i<data.items.length; i++) {
    //     displayDataItemName(data.items[i],data.items[i].row);
    // }
}

function displayDataItemName(data,row) {
    $('#id_form-' + row + '-recipe_id',).val(data.recipe_id);
    $('#id_form-' + row + '-id',).val(data.id);
    $('#id_form-' + row + '-item_name',).val(data.item_name);
    $('#id_form-' + row + '-item_id',).val(data.item_id);
    $('#id_form-' + row + '-item_amt',).val(data.item_amt);
    $('#id_form-' + row + '-row',).val(row);
}
