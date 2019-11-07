function updCompleted(id) {
    var checked = $('#completed_' + id).prop('checked');
    var param = {
        'id': id,
        'value': checked,
    }

	$.ajax({
		type: 'POST',
        url: '/susanowo/complete',
		dataType: 'json',
		data: JSON.stringify(param),
		contentType: 'application/json;charset=utf-8',
		cache : false,
		async : false
	}).done(function(data) {
        alert('test');
	}).fail(function(jqXHR, textStatus, errorThrown) {
		console.log(textStatus);
		alert('更新失敗');
	});
}