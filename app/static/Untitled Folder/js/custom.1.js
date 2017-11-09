$(function() {
    $('#submit-button').click(function() {
        var user = $('#orangeForm-name').val();
        var user = $('#orangeForm-name2').val();
        var pass = $('#orangeForm-pass').val();
        $.ajax({
            url: '/register',
            data: $('#login-form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                //$('#employee_detail').html(data);  
                $('#modalRegisterForm').modal('show'); 
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});