$(document).ready(function(){
});

$(function() {
    // イベント
    var totalCount = parseInt($('#shiharai_total_row').val());
    var base_buyser_choiceElement = $('#id_form-0-buyer_choice').clone();

    // $('#insert').click(function() {
    $(document).on("click", "#insert", function () {
        var row = $(this).attr('name');

        var trElement = $('<tr>', {
            class: 'tr_class',
            id: 'row' + totalCount,
        });

        var item_nm_tdElement = $('<td>', {
            class: 'td_class',
            style: 'width:200px',
        });
        var buyer_choice_tdElement = $('<td>', {
            class: 'td_class',
            style: 'width:200px',
        });
        var sum_user_amt_tdElement = $('<td>', {
            class: 'td_class',
            style: 'width:200px; text-align:right;',
        });
        var btn_insert_tdElement = $('<td>', {
            class: 'td_class',
            style: 'width:50px',
        });
        var btn_delete_tdElement = $('<td>', {
            class: 'td_class',
            style: 'width:50px',
        });
        var id_tdElement = $('<td>');
        var shiharai_row_tdElement = $('<td>');
        var delete_flg_tdElement = $('<td>');

        var item_nmElement = $('<input>', {
            type: 'text',
            name: 'form-' + totalCount + '-item_nm',
            id: 'id_form-' + totalCount + '-item_nm',
            maxlength: '30',
        });

        var buyser_choiceElement = base_buyser_choiceElement.clone();
        buyser_choiceElement.attr('id', 'id_form-' + totalCount + '-buyer_choice');
        buyser_choiceElement.attr('name', 'form-' + totalCount + '-buyer_choice');

        var sum_user_amtElement = $('<input>', {
            type: 'number',
            name: 'form-' + totalCount + '-sum_user_amt',
            id: 'id_form-' + totalCount + '-sum_user_amt',
        });

        var btn_insertElement = $('<img>', {
            id: 'insert',
            src: '/static/png/common/insert.png',
            name: totalCount,
        })

        var btn_deleteElement = $('<img>', {
            id: 'delete',
            src: '/static/png/common/delete.png',
            name: totalCount,
        })

        var idElement = $('<input>', {
            type: 'hidden',
            name: 'form-' + totalCount + '-id',
            id: 'id_form-' + totalCount + '-id',
            value: '',
        });

        var shiharai_rowElement = $('<input>', {
            type: 'hidden',
            name: 'form-' + totalCount + '-shiharai_row',
            id: 'id_form-' + totalCount + '-shiharai_row',
            value: totalCount,
        });

        var delete_flgElement = $('<input>', {
            type: 'hidden',
            name: 'form-' + totalCount + '-delete_flg',
            id: 'id_form-' + totalCount + '-delete_flg',
            value: 'False'
        });

        $('tr#row' + row).after(trElement);
        trElement.append(item_nm_tdElement);
        item_nm_tdElement.append(item_nmElement);

        trElement.append(buyer_choice_tdElement);
        buyer_choice_tdElement.append(buyser_choiceElement);

        trElement.append(sum_user_amt_tdElement);
        sum_user_amt_tdElement.append(sum_user_amtElement);

        trElement.append(btn_insert_tdElement);
        btn_insert_tdElement.append(btn_insertElement);

        trElement.append(btn_delete_tdElement);
        btn_delete_tdElement.append(btn_deleteElement);

        trElement.append(id_tdElement);
        id_tdElement.append(idElement);

        trElement.append(shiharai_row_tdElement);
        shiharai_row_tdElement.append(shiharai_rowElement);

        trElement.append(delete_flg_tdElement);
        delete_flg_tdElement.append(delete_flgElement);

        totalCount += 1
        $('#shiharai_total_row').val(totalCount)
        $('#id_form-TOTAL_FORMS').val(totalCount)
        buyser_choiceElement.val(' ');
    });

    // $('#delete').click(function() {
    $(document).on("click", "#delete", function () {
        var del_row = $(this).attr('name');
        $('#' + 'id_form-' + (del_row) + '-delete_flg').val("True");

        let row = $(this).closest("tr").hide();
        $(row).hide();


    });


});
