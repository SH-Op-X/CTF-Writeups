

 function typewrite()
 {
     let str="<可能对每一个CTFer来说<CTF就犹如夜空中闪亮的星星<也许这个过程很漫长、很枯燥<但在这些看似平凡的日子里<总能看到坚持的意义%在漫长的CTF生涯中<有争分夺秒的比赛，激烈的角逐<有志同道合、并肩作战的队友<更有，日复一日追逐的梦想%谨望各位师傅能牢记初心，不负热爱<一切的努力终有回报%<循此苦旅，以达繁星%刚刚输入的钥匙.....<包裹上SYC<就是你要找的答案";//利用<作为换行符 -作为空格
     let strp="";
     let i=0;
     function print1()
     {
         if(str[i]=='<')
         {
             document.getElementById("box1").innerHTML=strp+"<br><br>"+'|';
             strp+="<br><br>";
         }
         else
         if(str[i]=='-')
         {
             document.getElementById("box1").innerHTML=strp+'&nbsp&nbsp&nbsp';
             strp+="&nbsp&nbsp&nbsp";
         }
         else if (str[i] === '%') {
            strp = "";
            i++;
            return; 
        }
         else
         {
             strp+=str[i];
             document.getElementById("box1").innerHTML=strp+'|';
         }
         i++;
     }
     function print2()
     {
         setTimeout(()=>{document.getElementById("box1").innerHTML=strp+'&nbsp';},150);
         setTimeout(()=>{document.getElementById("box1").innerHTML=strp+'|';},780);
     }
     let printid=setInterval(() => {
         print1();
         if(i==str.length)
         clearInterval(printid);
     },90);  
     setTimeout(() => {
         id=setInterval(print2,2000);
     },(str.length-1)*150);
     
 }
 



let clickb=false;
 


function funclick()
 {
     let x = document.createElement("audio");
     x.setAttribute("src", "./video/55.mp3");
     x.setAttribute("autoplay", "autoplay");
     let yinyan=document.getElementById("yinyan");
     yinyan.style.opacity= 0;
     let bacg = document.getElementById("bac");
     setTimeout(function(){
         document.getElementById("fronclick").style.zIndex=-300;
         document.getElementById("box").style.opacity = 1;
         bacg.style.backgroundImage ='url(./img/2.png)';
     },1500);
     clickb=true;
 }

 
 let k={
     a:0,b:1,c:2,d:3,e:4,f:5,g:6,h:7,i:8,j:9,k:10,l:11,m:12,n:13,o:14,p:15,q:16,r:17,s:18,t:19,u:20,v:21,w:22,x:23,y:24,z:25,
     A:0,B:1,C:2,D:3,E:4,F:5,G:6,H:7,I:8,J:9,K:10,L:11,M:12,N:13,O:14,P:15,Q:16,R:17,S:18,T:19,U:20,V:21,W:22,X:23,Y:24,Z:25
 } 
 let a=[
     {name:"A",yin:9, str:"<br><br><br>乘着星光，<br><br>好像见到了从未想象过的风景。<br><br>似脉搏的悸动，<br><br>亦似心跳的合奏。"},
     {name:"B" ,yin:1, str:`<br><br><br><br>将玫瑰藏于身后，风起花落，<br><br>从此鲜花赠自己,<br><br>纵马踏花向自由。`},
     {name:"C" ,yin:2, str:"<br><br><br><br><br>所谓无底深渊，<br><br><br>下去也是前程万里。"},
     {name:"D" ,yin:3, str:"<br><br><br><br><br>日落跌入昭昭星野，<br><br>人间忽晚，<br><br>山河已秋。"},
     {name:"E" ,yin:4, str:"<br><br><br><br>那些看似不起波澜的日复一日，<br><br>会突然在某一天，<br><br>让人看到坚持的意义。"},
     {name:"F" ,yin:6, str:"<br><br><br><br><br>世界上没有两片完全相同的树叶，<br><br>每条河都有自己的方向。"},
     {name:"G" ,yin:7, str:"<br><br><br><br><br>生命久如暗室，<br><br><br>不妨我明写春诗。"},
     {name:"H" ,yin:11, str:"<br><br><br><br>不一定要长成玫瑰，<br></br>如果你愿意的话，做茉莉，做雏菊，<br></br>做无名小花，做干干万万。"},
     {name:"I" ,yin:12, str:"<br><br><br><br>我不想等待，<br>不想在无尽的山脚下看未来。<br><br>我只知道水会冷，风将停，春不再，<br>人生就在于逞一时之快。<br><br>明天太遥远了，我要现在。"},
     {name:"J" ,yin:13, str:"<br><br><br><br><br><br>一个能升起月亮的身体<br><br>必然驮住了无数次日落。"},
     {name:"k" ,yin:14, str:"<br><br><br><br>一坐不染不是不再有尘埃，而是尘埃。<br><br>让它飞扬，我自做我的阳光。<br><br>无论风暴把我带向何方，我都将以主人的身份上岸。"},
     {name:"L" ,yin:15, str:"<br><br><br><br><br>愿你，<br><br>以渺小启程，<br><br>以伟大结束。"},
     {name:"M" ,yin:16, str:"<br><br><br><br><br>我们只是在试图了解世界<br><br>努力接近真相。"},
     {name:"N" ,yin:17, str:"<br><br><br><br>人间骄阳正好，<br><br>风过林梢，<br><br>彼时我们正当年少。"},
     {name:"O" ,yin:18, str:"<br><br><br><br><br><br><br>愿你在自己热爱的世界里,<br><br>奔赴山海。<br><br>用心底的赤诚走向更远的路。"},
     {name:"P" ,yin:19, str:"<br><br><br><br<br><br><br>亲爱的朋友<br><br>人生永远柳暗花明"},
     {name:"Q" ,yin:20, str:"<br><br><br><br>在井隅,<br><br>心向星光，<br><br>眼里有诗,<br><br>自在远方。"},
     {name:"R" ,yin:10, str:"<br><br>所有的不远万里,<br><br>皆为你所赴约。<br><br>为我的星星，<br><br>千千万万遍<br><br>甘之如饴。"},
     {name:"S" ,yin:5, str:"<br><br><br><br>你有多遥远，<br><br>但这并不妨碍，<br><br>你成为我的星星。"},
     {name:"T" ,yin:8, str:"<br><br><br><br>成为独独照耀我的那颗星，<br><br>环遍了整个星系，<br><br>找不到比你更亮的星星。"},
     {name:"U" ,yin:21, str:"<br><br><br><br><br>让玫瑰成为玫瑰<br><br>让松柏成为松柏。"},
     {name:"V" ,yin:22, str:"<br><br><br><br<br><br><br><br>熬过的夜会变成光"},
     {name:"W" ,yin:23, str:"<br><br><br><br>人生不可能总是顺心如意，<br><br>但持续朝着阳光走，影子就会躲在后面。<br><br>刺眼，却是对的方向。"},
     {name:"X" ,yin:24, str:"<br><br><br><br><br><br>祝，年年有今日<br><br>岁岁有今朝。"},
     {name:"Y" ,yin:25, str:"<br><br><br><br><br><br>少年不惧岁月长，<br><br>彼方尚有荣光在。"},
     {name:"Z" ,yin:26, str:"<br><br><br><br><br>那就拂去旧诗满身的风雪<br><br>冬去后你我再来共祝春天"}
 ];
 let b=["url(./img/63.jpg)",
 "url(img/67.jpg)",
 "url(./img/39.jpg)",
 "url(./img/36.jpg)",
 "url(./img/22.jpg)",
 "url(./img/68.jpg)",
 "url(./img/53.jpg)",
 "url(./img/69.jpg)",
 "url(./img/62.jpg)",
 "url(./img/81.jpg)",
 "url(./img/71.jpg)",
 "url(./img/21.jpg)",
 "url(./img/30.jpg)",
 "url(./img/42.jpg)",
 "url(./img/82.jpg)",
 "url(./img/77.jpg)",
 "url(./img/74.jpg)",
 "url(./img/66.jpg)",
 "url(./img/20.jpg)",
 "url(./img/58.jpg)",
 "url(./img/33.jpg)",
 "url(./img/76.jpg)",
 "url(./img/75.jpg)",
 "url(./img/78.jpg)",
 "url(./img/79.jpg)",
 "url(./img/40.jpg)"];
 let s='';
 let records=0;
 

 
 function fl(e)
 {
     if(clickb==true)
     {
        let key =e.key;
     if((key<='z'&&key>='a')||(key<='Z'&&key>='A'))
     {
         let p=a[k[key]];
         s=s+p.name;
         let x = document.createElement("audio");
         x.setAttribute("src", `./video/${p.yin}.mp3`);
         x.setAttribute("autoplay","autoplay");
         let box=document.getElementById("box");
         let boxl=document.getElementById("boxl");
         let boxr=document.getElementById("boxr");
         let boxup=document.getElementById("boxup");
         let bac=document.getElementById("bac");
         bac.style.opacity=0;
         box.style.transition="0.5s";
         box.style.opacity=0;
         boxup.style.opacity=0;
         setTimeout(function()
         {
         boxl.innerHTML=`${p.name}`;
         boxr.innerHTML=`${p.str}`;
         console.log(b[k[key]]);
         bac.style.background=`${b[k[key]]}`;
       
        bac.style.backgroundSize = "cover"; 
        bac.style.backgroundPosition = "center center"; 
        bac.style.backgroundRepeat = "no-repeat"; 
         box.style.opacity=1;
         boxup.style.opacity=1;  
         bac.style.opacity=1;
         },500);
         if((CryptoJS.MD5(s).toString()=="5c50152daeee511f32db7bf8a5502c69")&&records==0)
         {
             setTimeout(function()
             {
                 records=1;
                 bac.style.opacity=0;
                 box.style.opacity=0;
                 boxup.style.opacity=0;  
                 bac.style.opacity=0;
                 let box1=document.getElementById("box1");
                 box1.style.zIndex=7;
                 box1.style.opacity=1;
                 let music=document.createElement("audio");
                 x.setAttribute("src", `./video/star.mp4`);
                 x.setAttribute("autoplay","autoplay");
                 x.setAttribute("loop","loop");
             },750);
             setTimeout(typewrite,3000);
         }
     }
     }  
 }
 
 
 window.onkeyup=fl;

 function startPrint() {
    console.log("==============================================================================================");
    console.log("          _____________                                                  ___");
    console.log("        ___         _______                                              ___");
    console.log("      ____                                                               ___      ___");
    console.log("     ____                                                                ___    ___");
    console.log("     ____                           _________           _________        ___  ___");
    console.log("     ____                         __        ___       __        ___      ______");
    console.log("     ____          ________      ___         __      ___         __      ___  ___");
    console.log("     ____             _____      _______________     _______________     ___   ___");
    console.log("      _____            ____      ___                 ___                 ___     ___");
    console.log("        _____          ____       ____      ____      ____      ____      ___      ___");
    console.log("           ________________         __ ________          _________        ___       ___");
    console.log("==============================================================================================");
    console.log("==============================================================================================");
    console.log("=======Welcome to GEEK Challenge ^_^ ");
}







let data = [
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'
];

let coordinates = [
    [1, 11], [1, 12], [1, 13], [1, 14],
    [2, 1], [2, 4], [2, 11], [2, 12], [2, 14],
    [3, 4], [3, 14],
    [5, 7], [5, 8], [5, 12], [5, 14], [5, 15], [5, 18],
    [6, 1], [6, 2], [6, 4], [6, 5], [6, 7], [6, 8], [6, 11], [6, 15],
    [7, 1], [7, 5], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [7, 16],
    [8, 1], [8, 12], [8, 13], [8, 15], [8, 18],
    [9, 3], [9, 4], [9, 6], [9, 7], [9, 8]
];

let cols = 20;
let rows = 10;

coordinates.forEach(([row, col]) => {
   
    const index = row * cols + col;
    
    if (index >= 0 && index < data.length) {
        data[index] = '*';
    }
});

let map = data.slice();


let a1, a2,a3, a4, a5, a6, a7, a8;

43654*a1 - 57003*a2 -3158*a3 + 30120*a4 -58621*a5 -41947*a6 +122237*a7 +129534*a8 == 2594143;
-48022*a1 + 18308*a2 + 52478*a3 + 69397*a4  +49696*a5 + 12288*a6 -40437*a7 -23154*a8 ==  651137;
124109*a1  +58952*a2 + 16645*a3 -17531*a4 + 53139*a5  +49937*a6  + 3282*a7   +7656*a8 == 2071815;
108286*a1 + 118886*a2 +116876*a3   +2281*a4 -64590*a5  -3021*a6 + 13386*a7 -56070*a8 ==  703;
105983*a1 + 8794*a2 + 31851*a3 -35052*a4  -7880*a5  + 2183*a6 + 47575*a7 +107236*a8 == 2511919;
-38005*a1 -6833*a2 +107897*a3 +119771*a4 +124322*a5 + 13335*a6+ 121590*a7 -17434*a8 == 4816084;
60696*a1 +95253*a2 +101581*a3 + 93822*a4 +112989*a5  +65643*a6  +45639*a7 + 26705*a8 == 5330538;
49019*a1 +72343*a2 -21814*a3  +85020*a4 -62332*a5  +99828*a6  +  587*a7 -65119*a8 ==  505173;

console.log("好像差了点什么……");
console.log("为什么不试试将a1~a8从小到大排列呢？");

console.log("S:(a1,a6) (a4,a5) Y:(a2,a8) (a3,a7)");
console.log("请以第x行第y列排列");


let chance = 0;
let x = 0;
let y = 0;

function locate1() {
    for (let i = 0; i <= 9; i++) {
        for (let j = 0; j <= 9; j++) {
            if (map[100 * chance + 10 * i + j] === 'S') {
                x = i;
                y = j;
                return;
            }
        }
    }
}

function left() {
    if (y > 0) {
        if (map[100 * chance + 10 * x + y - 1] === '*') {
            map[100 * chance + 10 * x + y - 1] = 'S';
            map[100 * chance + 10 * x + y] = '*';
        } else if (map[100 * chance + 10 * x + y - 1] === 'Y') {
            return 1;
        }
    }
    return 0;
}

function right() {
    if (y < 9) {
        if (map[100 * chance + 10 * x + y + 1] === '*') {
            map[100 * chance + 10 * x + y + 1] = 'S';
            map[100 * chance + 10 * x + y] = '*';
        } else if (map[100 * chance + 10 * x + y + 1] === 'Y') {
            return 1;
        }
    }
    return 0;
}

function down() {
    if (x < 9) {
        if (map[100 * chance + 10 * (x + 1) + y] === '*') {
            map[100 * chance + 10 * (x + 1) + y] = 'S';
            map[100 * chance + 10 * x + y] = '*';
        } else if (map[100 * chance + 10 * (x + 1) + y] === 'Y') {
            return 1;
        }
    }
    return 0;
}

function up() {
    if (x > 0) {
        if (map[100 * chance + 10 * (x - 1) + y] === '*') {
            map[100 * chance + 10 * (x - 1) + y] = 'S';
            map[100 * chance + 10 * x + y] = '*';
        } else if (map[100 * chance + 10 * (x - 1) + y] === 'Y') {
            return 1;
        }
    }
    return 0;
}

const input = prompt("You need to find the best wayyyyyyyy to the exit :D");
let v3 = 0;

function findtheway(){
    while (true) {
        let v0 = input[v3];
        if (!v0) break;


        let a2 = 0;
        locate1();
        while (a2 !== 1) {
            switch (v0) {
                case 'S':
                    a2 = left();
                    break;
                case 'T':
                    a2 = up();
                    break;
                case 'A':
                    a2 = right();
                    break;
                case 'R':
                    a2 = down();
                    break;
                default:
                    if (v0 === String.fromCharCode(27)) 
                        return; 
            }
            v3++;
        }

        if (chance === 1) break;
        chance++;



    }

    console.log("success!");
}