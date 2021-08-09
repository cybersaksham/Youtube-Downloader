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
    });
});