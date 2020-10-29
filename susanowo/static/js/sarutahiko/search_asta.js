$(document).ready( function() {
    autocompleteGetRecipeData('#id_recipe_name','/sarutahiko/recipe_list/',displayDataRecipeName)
    autocompleteGetItemData('#recipe_id','#id_form-' + currentFileCount + '-item_name','/sarutahiko/item_list/',displayDataItemName,0);
});

function autocompleteGetRecipeData(selector,url,displayData) {
    $(selector)
        .autocomplete({
            // source: wordlist
            source: function(req, resp){
                $.ajax({
                    url: url + $(selector).val(),
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
                url: url + $(this).val(),
                type: "GET",
                cache: false,
                dataType: "json",
                data: "",
                success: function(o){
                    if (o.length==1) {
                        displayData(o[0]);
                    }
                },
                error: function(xhr, ts, err){
                    resp(['']);
                }
            });
        });
}

function autocompleteGetItemData(recipe_id,recipeSelector,url,displayData,row) {
    $(recipeSelector)
        .autocomplete({
            // source: wordlist
            source: function(req, resp){
                $.ajax({
                    url: url + $(recipe_id).val() + '/' + $(recipeSelector).val(),
                    type: "GET",
                    cache: false,
                    dataType: "json",
                    data: "",
                    success: function(o){
                        var names = []
                        for (let i=0; i < o.length; i++) {
                            console.log(o[i].name);
                            names.push(o[i].name);
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
                url: url + $(recipe_id).val() + '/' + $(this).val(),
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
