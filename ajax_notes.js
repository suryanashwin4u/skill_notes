$.ajax({
    type: "POST",
    url: /target_route or filename,                                 //url
    data: {
        "key": value,                               //json data
    },
    dataType: "json",                           
    success: function (obj) {                       //success function         
        
    },
    error: function (errors) {                      //error function

    }
}); 