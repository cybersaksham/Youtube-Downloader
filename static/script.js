function showError($msg){
    $('#errorText').empty();
    $('#errorText').append($msg);
}

function appendTypes($data){
    $('#selectInput').empty();
    $.each($data, function(index, value){
        $appendTxt = "<option value=\"" + value + "\">" + value + "</option>";
        $('#selectInput').append($appendTxt);
    });
}

$(document).ready(function(){
    // Getting Video types
    $('#getTypes').click(function(e){
        e.preventDefault();
        if($('#urlInput').val() == ""){
            showError("Enter URL");
        }
        else{
            showError("");
            $.ajax({
                url: '/get_types',
                method: 'POST',
                data: $('#basicForm').serialize(),
                success: function(res){
                    if(res["error"] != null){
                        showError(res["error"]);
                    }
                    else{
                        appendTypes(res["types"]);
                        $('#typesModal').modal('show');
                    }
                }
            });
        }
    });

    // Pressing download button
    $('#downloadBtn').click(function(e){
        e.preventDefault();
        $('#mainForm').submit();
    });
});