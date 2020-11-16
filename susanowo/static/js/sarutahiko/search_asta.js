$(document).ready( function() {
    // autocompleteGetRecipeData('#id_recipe_name','/sarutahiko/recipe_list/',displayDataRecipeName)
    // autocompleteGetRecipeData('.recipe_name_class','/sarutahiko/recipe_list/',displayDataRecipeName,0)
    // autocompleteGetItemData('#id_id','#id_form-' + currentFileCount + '-item_name','/sarutahiko/item_list/',displayDataItemName,0);
    // autocompleteGetItemData('.recipe_id_class','.item_class_name','/sarutahiko/item_list/',displayDataItemName,0);
});

// function autocompleteGetRecipeData(selector_class,url,displayData,row) {
function autocompleteGetRecipeData(selector,url,displayData,row) {
    // selector = $('#' + $(selector_class).attr("id"));
    $(selector)
        .autocomplete({
            // source: wordlist
            source: function(req, resp){
                $.ajax({
                    url: url + $(selector).val() + "/S",
                    type: "GET",
                    cache: false,
                    dataType: "json",
                    data: "",
                    success: function(o){
                        var names = []
                        for (let i=0; i < o.length; i++) {
                            names.push(o[i].name);
                        }
                        resp(names);
                    },
                    error: function(xhr, ts, err){
                        resp(['']);
                    }
                });
            }
        })
        .change(function(e) {
            $.ajax({
                url: url + $(this).val() +"/C",
                type: "GET",
                cache: false,
                dataType: "json",
                data: "",
                success: function(o){
                    console.log(o);
                    if (o.length==1) {
                        displayData(o[0],row);
                    } else if (o.length==0) {
                        let recipeData = {name: $(selector).val() , code: 0 , url : ''};
                        displayData(recipeData,0);
                    }
                },
                error: function(xhr, ts, err){
                    resp(['']);
                }
            });
        });
}

function autocompleteGetItemData(recipe_id,recipeSelector,url,displayData,row) {
// function autocompleteGetItemData(recipe_id_class,recipeSelector_class,url,displayData,row) {
    // recipe_id = $('#' + $(recipe_id_class).attr("id"));
    // recipeSelector  = $('#' + $(recipeSelector_class).attr("id"));
    console.log($(recipe_id).val());
    var id_id = "0";
    if ($(recipe_id).val()!="") {
        id_id = $(recipe_id).val();
    }
    $(recipeSelector)
        .autocomplete({
            // source: wordlist
            source: function(req, resp){
                $.ajax({
                    url: url + id_id + '/' + $(recipeSelector).val() + "/S",
                    type: "GET",
                    cache: false,
                    dataType: "json",
                    data: "",
                    success: function(o){
                        var names = []
                        for (let i=0; i < o.length; i++) {
                            console.log(o[i].item_name);
                            names.push(o[i].item_name);
                        }
                        // console.log(o[0].name);
                        resp(names);
                    },
                    error: function(xhr, ts, err){
                        resp(['']);
                    }
                });
            }
        })
        .change(function(e) {
            // console.log('test');
            $.ajax({
                url: url + id_id + '/' + $(recipeSelector).val() + "/C",
                type: "GET",
                cache: false,
                dataType: "json",
                data: "",
                success: function(o){
                    if (o.length==1) {
                        displayData(o[0],row);
                    }
                },
                error: function(xhr, ts, err){
                    resp(['']);
                }
            });
        });
}
