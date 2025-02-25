Java.perform(function() {
    var Skip32 = Java.use('com.ex.skip.Skip32');

    // 保存原始FTABLE的引用
    var originalFTABLE = Skip32.FTABLE.value;

    console.log(originalFTABLE);
    // Hook g函数
    var gFunc = Skip32.g;
    gFunc.implementation = function(arg3, arg4, arg5) {

        // 执行原始函数
        var result = this.call(arg3, arg4, arg5);

        // 调用后的FTABLE值
        console.log(originalFTABLE);

        console.log("g函数返回值: " + result);
        return result;
    };
});
