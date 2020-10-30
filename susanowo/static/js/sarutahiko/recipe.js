$(document).ready(function(){
    var totalManageElement = $('input#id_form-TOTAL_FORMS');
    var currentFileCount = parseInt(totalManageElement.val());

    for (i=0; i<currentFileCount; i++) {
        // 材料のオートコンプリートを動的に追加
        var s = document.createElement("script");
        s.innerHTML = "autocompleteGetItemData('#id_id','#id_form-" + i + "-item_name','/sarutahiko/item_list/',displayDataItemName," + i + ");";
        var ele = document.getElementById("detail_body_class");
        ele.appendChild(s);
    }
});

function displayDataRecipeName(data) {
    $('#id_id').val(data.code);
    $('#id_url').val(data.url);
    // for (let i=0; i<data.items.length; i++) {
    //     displayDataItemName(data.items[i],data.items[i].row);
    // }
    window.location.href = '/sarutahiko/recipe/' + data.name;
}

function displayDataItemName(data,row) {
    // $('#id_form-' + row + '-recipe_id',).val(data.recipe_id);
    // $('#id_form-' + row + '-id',).val(data.id);
    $('#id_form-' + row + '-item_name',).val(data.item_name);
    $('#id_form-' + row + '-item_id',).val(data.item_id);
    $('#id_form-' + row + '-item_amt',).val(data.item_amt);
    // $('#id_form-' + row + '-row',).val(row);
}
