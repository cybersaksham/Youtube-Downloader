function showError($msg){
    $('#errorText').empty();
    $('#errorText').append($msg);
}

function appendTypes($data){
    $('#selectInput').empty();
    $.each($data, function(index, value){
        $appendTxt = "<option value=\"" + index + "\">" + value["type"] + " - " + value["mime_type"];
        if(value["type"] == "video"){
            $appendTxt += " - " + value["res"]
        }
        else{
            $appendTxt += " - " + value["abr"]
        }
        $appendTxt += "</option>";
        $('#selectInput').append($appendTxt);
    });
}

$(document).ready(function(){
    // Submitting URL
    $('#getTypes').click(function(e){
        e.preventDefault();
        if($('#urlInput').val() == ""){
            showError("Enter URL");
        }
        else{
            showError("");
            // Sending request to get types
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
        console.log($('#selectInput').val());
    });
});