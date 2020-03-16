$(document).ready(function(){
});

$(function() {
    // イベント
    var totalCount = parseInt($('#total_count').val());
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

        var item_nmElement = $('<input>', {
            type: 'text',
            name: 'form-' + totalCount + '-item_nm',
            id: 'id_form-' + totalCount + '-item_nm',
            maxlength: '30',
        });

        var buyser_choiceElement = $('#id_form-0-buyer_choice').clone();
        buyser_choiceElement.attr('id', 'id_form-' + totalCount + '-item_nm');
        buyser_choiceElement.attr('name', 'form-' + totalCount + '-item_nm');

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

        totalCount += 1
        $('#total_count').val(totalCount)
    });

    // $('#delete').click(function() {
    $(document).on("click", "#delete", function () {

        let row = $(this).closest("tr").remove();
        $(row).remove();
    });


});
