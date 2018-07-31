window.addEventListener("load", 
    function(){
        var thumbnail = document.getElementById("thumbnails");
        var bigPic = document.getElementById("featured").getElementsByTagName("*")
    
        thumbnail.addEventListener("click", 
            function(e){
                
                bigPic[0].src = e.target.src; 
            });
        });





 