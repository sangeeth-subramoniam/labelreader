function infomsg() {
    if(document.getElementById("touroku_info_msg").value == "登録しました"){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '修正しました！',
            showConfirmButton: false,
            timer: 2000,
            color: '#9e665d'
            })
        document.getElementById("touroku_info_msg").value == null;
    }

}


function formsubmit1(){
    form = document.getElementById("kensakushuseiform");
    form.submit();
}

function formsubmit2(){

    var radios = document.getElementsByTagName('input');
    var value;
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].type === 'radio' && radios[i].checked) {
            // get value, set checked flag or do whatever you need to
            value = radios[i].value;       
        }
    }

    alert(value)

    if (value != null){
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '帳票をダウンロードしました！',
            showConfirmButton: false,
            timer: 2000,
            color: '#9e665d'
            })   
    }

    form = document.getElementById("kensakushuseiform");
    form.submit();
}


function shusei() { 
    document.getElementById("checkvalue_for_chohyou").value = "1";
    a = document.getElementById("checkvalue_for_chohyou").value;     
    formsubmit1();
}


function chohyou() {
    document.getElementById("checkvalue_for_chohyou").value = '2';
    b = document.getElementById("checkvalue_for_chohyou").value;
    formsubmit2();
}