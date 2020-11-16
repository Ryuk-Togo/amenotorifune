$(document).ready(function(){
    var totalManageElement = $('input#id_form-TOTAL_FORMS');
    var currentFileCount = parseInt(totalManageElement.val());

    // autocompleteGetRecipeData('.recipe_name_class','/sarutahiko/recipe_list/',displayDataRecipeName,0)
    // autocompleteGetItemData('#id_id','#id_form-' + currentFileCount + '-item_name','/sarutahiko/item_list/',displayDataItemName,0);

    for (i=0; i<currentFileCount; i++) {
        // 材料のオートコンプリートを動的に追加
        var s = document.createElement("script");
        s.innerHTML = "autocompleteGetRecipeData('#id_form-" + i + "-recipe_name','/sarutahiko/recipe_list/',displayDataRecipeName," + i + ");";
        var parentDiv = $('#id_form-' + i + '-recipe_name').parent().parent().attr('id');
        var ele = document.getElementById(parentDiv);
        ele.appendChild(s);
    }
    // var s = document.createElement("script");
    // s.innerHTML = "autocompleteGetRecipeData('.recipe_name_class','/sarutahiko/recipe_list/',displayDataRecipeName," + 0 + ");";
    // var parentDiv = $('#id_form-' + 0 + '-recipe_id').parent().parent().attr('id');
    // var ele = document.getElementById(parentDiv);
    // ele.appendChild(s);
});

function displayDataRecipeName(data,row) {
    $('#id_form-' + row + '-recipe_id').val(data.code);
    // window.location.href = '/sarutahiko/recipe/' + data.name;
}
