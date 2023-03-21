$(document).ready(function() {
    $("#dept").change(function() {
        var dept_id = $(this).val();
        var url = "/get-course/?dept_id="+dept_id;
        $.get(url, function(data, status){
            $("#course").html(data);
        });
    });
});



