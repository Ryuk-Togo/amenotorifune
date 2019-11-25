$(document).ready(function(){
//     $('input[name="user_id"]').prop('disabled', true);
// //    $('input[name="action_selection"]').prop('disabled', true);
//     $('#id_action_selection').prop('disabled', false);
//     $('input[name="delivery_date"]').prop('disabled', true);
//     $('input[name="single_action"]').prop('disabled', true);
//     $('input[name="can_do_tow_minite"]').prop('disabled', true);
//     $('input[name="should_myself"]').prop('disabled', true);
//     $('input[name="request_pertner"]').prop('disabled', true);
//     $('input[name="should_do_oneday"]').prop('disabled', true);
    controlObuject();
});
$(function() {
    // 行動を起こす必要がある
    $('input[name="should_action"]').change(function() {
        // var is_should_action = $('input[name="should_action"]').prop('checked');
        // if (is_should_action) {
        //     // 行動を起こす必要がある
        //     $('#id_action_selection').prop('disabled', true);
        //     $('input[name="delivery_date"]').prop('disabled', false);
        //     $('input[name="single_action"]').prop('disabled', false);
        // } else {
        //     // 行動を起こす必要はない
        //     $('#id_action_selection').prop('disabled', false);
        //     $('input[name="delivery_date"]').prop('disabled', true);
        //     $('input[name="single_action"]').prop('disabled', true);
        //     $('input[name="can_do_tow_minite"]').prop('disabled', true);
        //     $('input[name="should_myself"]').prop('disabled', true);
        //     $('input[name="request_pertner"]').prop('disabled', true);
        //     $('input[name="should_do_oneday"]').prop('disabled', true);
        //         }
        controlObuject();
    });

    // アクションは１つ
    $('input[name="single_action"]').change(function() {
        // var is_single_action = $('input[name="single_action"]').prop('checked');
        // if (is_single_action) {
        //     $('input[name="can_do_tow_minite"]').prop('disabled', false);
        // } else {
        //     $('input[name="can_do_tow_minite"]').prop('disabled', true);
        //     $('input[name="should_myself"]').prop('disabled', true);
        //     $('input[name="request_pertner"]').prop('disabled', true);
        //     $('input[name="should_do_oneday"]').prop('disabled', true);
        //         }
        controlObuject();
    });

    // 2分以内でおわる？
    $('input[name="can_do_tow_minite"]').change(function() {
        // var is_can_do_tow_minite = $('input[name="can_do_tow_minite"]').prop('checked');
        // if (is_can_do_tow_minite) {
        //     $('input[name="should_myself"]').prop('disabled', false);
        // } else {
        //     $('input[name="should_myself"]').prop('disabled', true);
        //     $('input[name="request_pertner"]').prop('disabled', true);
        //     $('input[name="should_do_oneday"]').prop('disabled', true);
        // }
        controlObuject();
    });

    // 自分でやるべき
    $('input[name="should_myself"]').change(function() {
        // var is_should_myself = $('input[name="should_myself"]').prop('checked');
        // if (is_should_myself) {
        //     $('input[name="request_pertner"]').prop('disabled', false);
        //     $('input[name="should_do_oneday"]').prop('disabled', false);
        // } else {
        //     $('input[name="request_pertner"]').prop('disabled', true);
        //     $('input[name="should_do_oneday"]').prop('disabled', true);
        // }
        controlObuject();
    });

    // 特定の日にやるべき
    $('input[name="should_do_oneday"]').change(function() {
        controlObuject();
    });

});

function controlObuject() {

    // 初期状態
    $('#id_action_selection').prop('disabled', false);
    $('input[name="delivery_date"]').prop('disabled', true);
    $('input[name="single_action"]').prop('disabled', true);
    $('input[name="can_do_tow_minite"]').prop('disabled', true);
    $('input[name="should_myself"]').prop('disabled', true);
    $('input[name="request_pertner"]').prop('disabled', true);
    $('input[name="should_do_oneday"]').prop('disabled', true);
    $('input[name="date_should_do"]').prop('disabled', true);

    var is_should_action = $('input[name="should_action"]').prop('checked');
    if (is_should_action) {
        // 行動を起こす必要がある
        $('#id_action_selection').prop('disabled', true);
        $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', true);
        $('input[name="should_myself"]').prop('disabled', true);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);
        $('#id_action_selection').val('');
    } else {
        // 行動を起こす必要はない
        $('#id_action_selection').prop('disabled', false);
        $('input[name="delivery_date"]').prop('disabled', true);
        $('input[name="single_action"]').prop('disabled', true);
        $('input[name="can_do_tow_minite"]').prop('disabled', true);
        $('input[name="should_myself"]').prop('disabled', true);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);

        $('input[name="delivery_date"]').val('');
        $('input[name="single_action"]').prop('checked', false);
        $('input[name="can_do_tow_minite"]').prop('checked', false);
        $('input[name="request_pertner"]').val('');
        $('input[name="should_do_oneday"]').prop('checked', false);
        $('input[name="date_should_do"]').val('');
    }

    var is_single_action = $('input[name="single_action"]').prop('checked');
    if (is_single_action) {
        // アクションは１つ
        $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', true);
        $('input[name="should_myself"]').prop('disabled', true);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);
    } else {
        // アクションは複数
        // $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', true);
        $('input[name="single_action"]').prop('disabled', true);
        $('input[name="can_do_tow_minite"]').prop('disabled', true);
        $('input[name="should_myself"]').prop('disabled', true);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);

        $('input[name="can_do_tow_minite"]').prop('checked', false);
        $('input[name="request_pertner"]').val('');
        $('input[name="should_do_oneday"]').prop('checked', false);
        $('input[name="date_should_do"]').val('');
    }

    var is_can_do_tow_minite = $('input[name="can_do_tow_minite"]').prop('checked');
    if (is_can_do_tow_minite) {
        // 2分以上かかる
        $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', false);
        $('input[name="should_myself"]').prop('disabled', false);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);
    } else {
        // 2分以内で終わる
        // $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', false);
        $('input[name="should_myself"]').prop('disabled', true);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);

        $('input[name="should_myself"]').prop('checked', false);
        $('input[name="request_pertner"]').val('');
        $('input[name="should_do_oneday"]').prop('checked', false);
        $('input[name="date_should_do"]').val('');
    }

    var is_should_myself = $('input[name="should_myself"]').prop('checked');
    if (is_should_myself) {
        // 自分で行う
        $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', false);
        $('input[name="should_myself"]').prop('disabled', false);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', true);
        $('input[name="date_should_do"]').prop('disabled', true);
        $('input[name="request_pertner"]').val('');
    } else {
        // 誰かに依頼する
        // $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', false);
        $('input[name="should_myself"]').prop('disabled', false);
        if (is_can_do_tow_minite) {
            $('input[name="request_pertner"]').prop('disabled', false);
        } else {
            $('input[name="request_pertner"]').prop('disabled', true);
            $('input[name="request_pertner"]').val('');
        }
        $('input[name="should_do_oneday"]').prop('disabled', false);
        $('input[name="date_should_do"]').prop('disabled', true);

        $('input[name="request_pertner"]').val('');
        $('input[name="should_do_oneday"]').prop('checked', false);
        $('input[name="date_should_do"]').val('');
    }
    
    var is_should_do_oneday = $('input[name="should_do_oneday"]').prop('checked');
    if (is_should_do_oneday) {
        // 特定の日に行う
        $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', false);
        $('input[name="should_myself"]').prop('disabled', false);
        $('input[name="request_pertner"]').prop('disabled', true);
        $('input[name="should_do_oneday"]').prop('disabled', false);
        $('input[name="date_should_do"]').prop('disabled', false);
    } else {
        // $('#id_action_selection').prop('disabled', true);
        // $('input[name="delivery_date"]').prop('disabled', false);
        $('input[name="single_action"]').prop('disabled', false);
        $('input[name="can_do_tow_minite"]').prop('disabled', false);
        $('input[name="should_myself"]').prop('disabled', false);
        if (is_can_do_tow_minite && !is_should_myself) {
            $('input[name="request_pertner"]').prop('disabled', false);
        } else {
            $('input[name="request_pertner"]').prop('disabled', true);
            $('input[name="request_pertner"]').val('');
        }
        $('input[name="should_do_oneday"]').prop('disabled', false);
        $('input[name="date_should_do"]').prop('disabled', true);

        $('input[name="date_should_do"]').val('');
    }
}