function showError($msg){
    $('#errorText').empty();
    $('#errorText').append($msg);
}

$(document).ready(function(){
    // Submitting Form
    $('#basicForm').on('submit', function(e){
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
                        console.log(res["types"]);
                    }
                }
            });
        }
    });
});