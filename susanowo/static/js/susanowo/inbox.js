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
    $('input[name="single_action"]').change(function() {
        var is_single_action = $('input[name="single_action"]').prop('checked');
        if (is_single_action) {
            $('input[name="can_do_tow_minite"]').prop('disabled', false);
        } else {
            $('input[name="can_do_tow_minite"]').prop('disabled', true);
            $('input[name="should_myself"]').prop('disabled', true);
            $('input[name="should_do_than_2min"]').prop('disabled', true);
        }
    });

    // 2分以内でおわる？
    $('input[name="can_do_tow_minite"]').change(function() {
        var is_can_do_tow_minite = $('input[name="can_do_tow_minite"]').prop('checked');
        if (is_can_do_tow_minite) {
            $('input[name="should_myself"]').prop('disabled', false);
        } else {
            $('input[name="should_myself"]').prop('disabled', true);
            $('input[name="should_do_than_2min"]').prop('disabled', true);
        }
    });

    // 自分でやるべき
    $('input[name="should_myself"]').change(function() {
        var is_should_myself = $('input[name="should_myself"]').prop('checked');
        if (is_should_myself) {
            $('input[name="should_do_than_2min"]').prop('disabled', false);
        } else {
            $('input[name="should_do_than_2min"]').prop('disabled', true);
        }
    });

});