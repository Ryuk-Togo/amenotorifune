$(function () {
    // 日付は、年/月/日 の形式でお願いする。
    let dateFormat = 'yy/mm/dd';
    $('#id_start_date').datepicker({
        dateFormat: dateFormat
    });
    $('#id_end_date').datepicker({
        dateFormat: dateFormat
    });
});

