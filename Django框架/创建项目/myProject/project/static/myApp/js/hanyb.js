$(document).ready(function(){
   document.getElementById("btn").onclick=function(){
   $.ajax({
           type:"get",
           url:"/hanyb/getstudentsinfo/",
           dataType:"json",
           success:function(data,textStatus){
               var d = data["students"]
               console.log(d)
               for(var i = 0; i < d.length; i++){
                   document.write('<p>'+d[i]+'</p>')
                   }
               }
           })
   }
})