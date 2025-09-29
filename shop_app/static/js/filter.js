$(document).ready(function(){
    $('#filter').on('click', function(){
       $.ajax({
            contentType: "aplication/json",
            url: "/shop/filter",
            type: "post",
            data: $("#type-product").val(),
            success: function(response){
                // видалити усі минулі товари

                // створити нові товари з response
            }
       })
    })
})