
function checkFlag(){
    let flag = document.getElementById("flag").value;
    let flag_len = flag.length+1;

    let flag_arr = Array(flag_len).fill(0);
    for(let i = 0; i < flag_len-1; i++){
        flag_arr[i] = flag.charCodeAt(i);
    }

    let flag_ptr = Module._malloc(flag_len);
    Module.HEAPU8.set(new Uint8Array(flag_arr), flag_ptr);
    let res = Module.cwrap("check_flag", "number", ["number"])(flag_ptr);
    Module._free(flag_ptr);

    if(res == 1){
        document.getElementById("right").innerHTML = "ur right :)";
        document.getElementById("wrong").innerHTML = "";
    }else{
        document.getElementById("right").innerHTML = "";
        document.getElementById("wrong").innerHTML = "ur wrong :(";
    }
}
