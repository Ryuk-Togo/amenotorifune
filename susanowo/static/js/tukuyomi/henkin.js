var row_count = 0

$(document).ready(function(){
    // $('#btnUserList').hide();
    // row_count = Number($('#row_count').val());
    row_count = Number($('#id_form-TOTAL_FORMS').val());

    // 合計の計算
    sumAmtBalance();
    $('#zandaka').val($('#id_sum_refund_balance').val());
});

$(function() {
    // 購入者の入力
    $('#id_buyer_name').change(function() {
        // $('#btnUserList').click();
        $('#id_buyer_id').val($('#id_buyer_name').val());
    });

    // 戻るボタン押下
    $('#btn_cancel').click(function() {
        history.back();
    });

    // 返金額の入力
    $('#id_sum_refund_balance').change(function() {

        // // チェックを全て付ける
        // checkAll();

        // // 返金額の計算
        // computeSelectBalance();

        // 合計の計算
        sumAmtBalance();
    });

    // チェックON/OFF
    $('.is_selected').change(function() {
        // 返金額の計算
        computeSelectBalance(this);

        // 合計の計算
        sumAmtBalance();
    });

    // 明細の返金額を変更
    $('.refund_balance').change(function() {
        // // 返金額の計算
        // computeSelectBalance();

        // 合計の計算
        sumAmtBalance();
    });

});

// チェックを全て付ける
function checkAll() {
    var i = 0
    for (i=0; i<row_count; i++) {
        $("#id_form-" + i + "-is_selected").prop('checked', true);;
    }
}

// 返金額の計算
function computeSelectBalance(chk_box) {
    var name = chk_box.name;
    var row = name.split('-')[1];
    var user_amt = Number($("#id_form-" + row + "-sum_user_amt").val());
    var refund_balance = Number($("#id_form-" + row + "-refund_balance").val());
    var sum_refund_balance = Number($('#zandaka').val());
    var add_amt = user_amt - refund_balance;
    var moto_refund_balance = Number($("#id_form-" + row + "-moto_refund_balance").val());

    if ($("#id_form-" + row + "-is_selected").prop('checked')) {
        // チェックオン
        if (sum_refund_balance - user_amt > 0) {
            // 残高残る
            $("#id_form-" + row + "-refund_balance").val(user_amt);
            sum_refund_balance = sum_refund_balance - add_amt;
        } else {
            // 残高が残らない
            if (user_amt < (sum_refund_balance + refund_balance)) {
                $("#id_form-" + row + "-refund_balance").val(user_amt);
                sum_refund_balance = (sum_refund_balance + refund_balance) - user_amt;
            } else {
                $("#id_form-" + row + "-refund_balance").val(sum_refund_balance + refund_balance);
                sum_refund_balance = 0;
            }
        }
    } else {
        // チェックOFF
        if (moto_refund_balance==0) {
            // 登録前の途中までの返金があった
            sum_refund_balance = sum_refund_balance + refund_balance;
            $("#id_form-" + row + "-refund_balance").val(0);
        } else {
            // 登録前から返金は無かった
            sum_refund_balance = sum_refund_balance + (refund_balance - moto_refund_balance);
            $("#id_form-" + row + "-refund_balance").val(moto_refund_balance);
        }
    }
    $('#zandaka').val(sum_refund_balance);

}

function computeSelectBalance_del2(chk_box) {
    var name = chk_box.name;
    var row = name.split('-')[1];
    var user_amt = Number($("#id_form-" + row + "-sum_user_amt").val());
    var refund_balance = Number($("#id_form-" + row + "-refund_balance").val());
    var add_amt = user_amt - refund_balance;
    var sum_refund_balance = Number($('#zandaka').val());
    var moto_refund_balance = $("#id_form-" + row + "-moto_refund_balance").val();


    if ($("#id_form-" + row + "-is_selected").prop('checked')) {
        // チェックオン
        if (sum_refund_balance - add_amt > 0) {
            // 残高が残る
            $("#id_form-" + row + "-refund_balance").val(user_amt);
            sum_refund_balance = sum_refund_balance - add_amt;
        } else {
            // 残高が残らない
            $("#id_form-" + row + "-refund_balance").val(sum_refund_balance);
            sum_refund_balance = 0;
        }
    } else {
        // チェックオフ
        $("#id_form-" + row + "-refund_balance").val(moto_refund_balance);
        sum_refund_balance = sum_refund_balance + refund_balance - moto_refund_balance;
    }
    $('#zandaka').val(sum_refund_balance);

}

function computeSelectBalance_del() {
    var sum_usr_amt = 0;
    var sum_refund_balance = Number($('#zandaka').val());

    var i = 0
    for (i=0; i<row_count; i++) {
        if ($("#id_form-" + i + "-is_selected").prop('checked')) {
            var user_amt = Number($("#id_form-" + i + "-sum_user_amt").val());
            var refund_balance = Number($("#id_form-" + i + "-refund_balance").val());
            var add_amt = user_amt - refund_balance;

            if (sum_refund_balance - add_amt > 0) {
                $("#id_form-" + i + "-refund_balance").val(refund_balance + add_amt);
                sum_refund_balance = sum_refund_balance - add_amt;
            } else {
                $("#id_form-" + i + "-refund_balance").val(refund_balance + sum_refund_balance);
                sum_refund_balance = 0;
                break;
            }
        } else {
            $("#id_form-" + i + "-refund_balance").val($("#id_form-" + i + "-moto_refund_balance").val());
            sum_refund_balance = sum_refund_balance + Number($("#id_form-" + i + "-moto_refund_balance").val());
            $('#zandaka').val(sum_refund_balance);
        }

    }

}

// 合計の計算
function sumAmtBalance() {
    var sum_usr_amt = 0;
    var sum_refund_balance = 0;

    var i = 0
    for (i=0; i<row_count; i++) {
        sum_usr_amt = sum_usr_amt + Number($("#id_form-" + i + "-sum_user_amt").val());
        // if ($("#id_form-" + i + "-is_selected").prop('checked')) {
            sum_refund_balance = sum_refund_balance + Number($("#id_form-" + i + "-refund_balance").val());
        // }
    }

    $('#sum_user_amt').val(sum_usr_amt);
    $('#sum_refund_balance').val(sum_refund_balance);
    // $('#zandaka').val(sum_refund_balance);

}