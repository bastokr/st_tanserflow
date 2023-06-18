var resetBtn = document.querySelector('#reset');
resetBtn.addEventListener("click", resetCanvas);

function resetCanvas(event){
    var canvas = document.querySelector('canvas');
    var context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.beginPath();
}

// ajax
var sendBtn = document.querySelector('#send');
sendBtn.addEventListener("click", sendAjax);
function sendAjax(event){
    const canvas = document.getElementById('canvas');  
    //const ctx = canvas.getContext("2d");
     
  
    // Convert canvas to dataURL and log to console
    const dataURL = canvas.toDataURL();
    const SENDDATA =JSON.stringify({"image":dataURL});
    console.log(SENDDATA);  

    alert('test');
    $.ajax({
        type:'POST',
        url:"http://localhost:5000/test",
        dataType:'json', 
        contentType: "application/json; charset=utf-8",
        data:SENDDATA,
        success:function(responce){
    
                                 console.log(responce);
                    },
                        error: function (response) {
                        // alert the error if any error occured
                        alert("this one is error");
                        alert(response["responseJSON"]["error"]);
                        },
        })
}