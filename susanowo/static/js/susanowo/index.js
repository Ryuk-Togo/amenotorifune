$(document).ready(function(){
	// 行の色を変更
	var d=[];
	$('table tr').each(function(i, e){
		if (i!=0) {
			var id = ($(this)[0].id).replace('row','');
			modRowStyle(id,$('#completed_' + id).prop('checked'),$('#delete_' + id).prop('checked'));
		}
	});
});

function updStatus(id) {
	var form = $('#modstatus');
    // var param = {
    //     id : Number(id),
    //     complete : $('#completed_' + id).prop('checked'),
    //     delete : $('#delete_' + id).prop('checked'),
	// }
	$('#param_id').val(id);
	$('#param_complete').val(comfBoolean($('#completed_' + id).prop('checked')));
	$('#param_delete').val(comfBoolean($('#delete_' + id).prop('checked')));

	$.ajax({
		type: form.prop("method"),
        url: form.prop("action"),
		data: form.serialize(),
		dataType: 'text',
	}).done(function(data) {
	}).fail(function(jqXHR, textStatus, errorThrown) {
		console.log(textStatus);
		alert('処理失敗!! ' + jqXHR.responseText);
	});

	// 行の色を変更
	modRowStyle(id,$('#completed_' + id).prop('checked'),$('#delete_' + id).prop('checked'));
}

function modRowStyle(id,completed,deleted) {
	if (deleted) {
		$('#row' + id).removeClass('normal_row');
		$('#row' + id).removeClass('completed_row');
		$('#row' + id).addClass('deleted_row');
	} else if (completed) {
		$('#row' + id).removeClass('normal_row');
		$('#row' + id).removeClass('deleted_row');
		$('#row' + id).addClass('completed_row');
	} else {
		$('#row' + id).removeClass('deleted_row');
		$('#row' + id).removeClass('completed_row');
		$('#row' + id).addClass('normal_row');
	}
}

