$(function() {
    // $('.class_del').click(function() {
    $(document).on('click', '.class_del', function() {
        let row = $(this).closest("tr").remove();
        $(row).remove();
    });

    // $('.class_add').click(function() {
    $(document).on('click', '.class_add', function() {
            // let $row = $(this).closest("tr");
        // let $newRow = $row.clone(true);
        let html = '<tr class="normal_row"><td style="width:600px;"><input type="file" name="attach" required id="id_attach"></td>';
        html += '<td style="width:50px">';
        html += '    <input type="button" id="add" name="add" class="class_add square_btn_small" value="追加" />';
        html += '</td>';
        html += '<td style="width:50px">';
        html += '    <input type="button" id="del" name="del" class="class_del square_btn_small" value="削除" />';
        html += '</td></tr>';
        // $newRow.insertAfter($row);
        $('#shiryou_tbody').append(html);
    });
});