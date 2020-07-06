//让背景动起来
    var jsmainScreen = document.getElementById("mainScreen")
//    console.log(jsmainScreen.offsetLeft)
    var jsBg1 = document.getElementById("bg1")
    var jsBg2 = document.getElementById("bg2")

    var timerBg = setInterval(function(){
    jsBg1.style.top = jsBg1.offsetTop + 1 +"px";
    jsBg2.style.top = jsBg2.offsetTop + 1 +"px";

    if(jsBg1.offsetTop >= 576){
        jsBg1.style.top = "-576px";
    }
    if(jsBg2.offsetTop >= 576){
        jsBg2.style.top = "-576px";
    }
    },10)


    //拖拽效果
    var jsPlane = document.getElementById("plane");
    document.onmousedown = function (e) {
            var disx = e.pageX - jsPlane.offsetLeft;
            var disy = e.pageY - jsPlane.offsetTop;
            document.onmousemove = function (e) {
                jsPlane.style.left = e.pageX - disx + 'px';
                jsPlane.style.top = e.pageY - disy + 'px';
            }
            }

     document.onmouseup = function(e){
          document.onmousemove = null;
     }

     //创建子弹
     var timerBullet =setInterval(function(){
        var bullet = document.createElement("div");
        jsmainScreen.appendChild(bullet);
        bullet.style.width = "10px";
        bullet.style.height = "10px";
        bullet.style.backgroundColor = "yellow";
        bullet.style.position = "absolute";
        bullet.style.left = jsPlane.offsetLeft + 35 + "px";
        bullet.style.top = jsPlane.offsetTop + "px";

        //子弹向上移动
        var timerBulletFly = setInterval(function(){

            bullet.style.top = bullet.offsetTop - 10 + "px";
//            console.log(jsPlane.offsetTop)
            if(bullet.offsetTop <= -20){
                clearInterval(timerBulletFly)
                jsmainScreen.removeChild(bullet)
            }
        },50)
     },1000)


     //创建坦克
     var timerTank =setInterval(function(){
        var tank = document.createElement("div");
        jsmainScreen.appendChild(tank);
        tank.className = "tank";
        tank.style.left = parseInt(Math.random()*(470 - 0 + 1) + 0) + "px";
//        tank.style.left = 470 +"px";
        tank.style.top = "0px";

        //坦克向下移动
        var timerTankFly = setInterval(function(){

            tank.style.top = tank.offsetTop + 5 + "px";

            if(tank.offsetTop >= 600){
                clearInterval(timerTankFly)
                jsmainScreen.removeChild(tank)
            }
        },50)
     },1000)


/*
//碰撞检测函数
window.onload = function (oDiv, oDiv2) {
    var disX = 0;
    var disY = 0;
    oDiv.onmousedown = function (ev) {
      var ev = ev || window.event;
      disX = ev.clientX - oDiv.offsetLeft;
      disY = ev.clientY - oDiv.offsetTop;
      document.onmousemove = function (ev) {
        var ev = ev|| window.event;
        var t1 = oDiv.offsetTop;
        var l1 = oDiv.offsetLeft;
        var r1 = oDiv.offsetLeft + oDiv.offsetWidth;
        var b1 = oDiv.offsetTop + oDiv.offsetHeight;
        var t2 = oDiv2.offsetTop;
        var l2 = oDiv2.offsetLeft;
        var r2 = oDiv2.offsetLeft + oDiv2.offsetWidth;
        var b2 = oDiv2.offsetTop + oDiv2.offsetHeight;
        if(b1<t2 || l1>r2 || t1>b2 || r1<l2){// 表示没碰上
            return false;
        }else{
          return true;
        }
        oDiv.style.left = ev.clientX - disX +'px';
        oDiv.style.top = ev.clientY - disY +'px';
      }

      }
      return false;
    }

*/
