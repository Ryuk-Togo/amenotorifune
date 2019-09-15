$(document).ready(function(){
    $('input[name="action_selection"]').prop('disabled', true);
    $('input[name="delivery_date"]').prop('disabled', true);
    $('input[name="single_action"]').prop('disabled', true);
    $('input[name="can_do_tow_minite"]').prop('disabled', true);
    $('input[name="should_myself"]').prop('disabled', true);
    $('input[name="should_do_than_2min"]').prop('disabled', true);
});
$(function() {
    // 行動を起こす必要がある
    $('input[name="should_action"]').change(function() {
        var is_should_action = $('input[name="should_action"]').prop('checked');
        if (is_should_action) {
            // 行動を起こす必要がある
            $('input[name="action_selection"]').prop('disabled', false);
            $('input[name="delivery_date"]').prop('disabled', false);
            $('input[name="single_action"]').prop('disabled', false);
        } else {
            // 行動を起こす必要はない
            $('input[name="action_selection"]').prop('disabled', true);
            $('input[name="delivery_date"]').prop('disabled', true);
            $('input[name="single_action"]').prop('disabled', true);
            $('input[name="can_do_tow_minite"]').prop('disabled', true);
            $('input[name="should_myself"]').prop('disabled', true);
            $('input[name="should_do_than_2min"]').prop('disabled', true);
        }
    });

    // アクションは１つ
    $('input[name="should_action"]').change(function() {
        var is_should_action = $('input[name="should_action"]').prop('disabled');
    });
});