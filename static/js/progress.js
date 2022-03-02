$(document).ready(function(){

    $('#indicator').on('click', function(event){


        window.setInterval(function(){
            ajaxCallFunction();  //calling every 5 seconds
        }, 1000);

    });

});

function ajaxCallFunction(){

    $.ajax({
        data:{
            tester : 'test'
        },
        type :'POST',
        url : "/ajax_progress",
        error: function(obj, status, err) { alert(err); console.log(err); }
    })

    .done(function(data){
        console.log(data.percent)
        var resp = data.percent + " % " + "読み込み中... "
        $(".indicator-message").html(resp);  
    });
}