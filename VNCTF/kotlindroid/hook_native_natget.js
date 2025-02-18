Java.perform(function () {
    // 获取JNI类的引用
    var JNI = Java.use("com.atri.ezcompose.JNI");

    // Hook `getAt` 方法
    JNI.getAt.implementation = function () {
        // 打印调试信息
        console.log("JNI.getAt() 被调用");

        // 调用原始的 getAt 方法
        var result = this.getAt();

        // 打印返回值
        console.log("getAt() 返回值: " + result);

        return result;  // 返回结果
    };

    // Hook native_natget 方法
    JNI.native_natget.overload('[B').implementation = function (arg1) {
        // 打印调用时传递的参数
        console.log("native_natget() 被调用，参数: " + arg1);

        // 你可以在这里修改参数或者改变返回值
        var result = this.native_natget(arg1);

        // 打印返回值
        console.log("native_natget() 返回值: " + result);

        return result;  // 返回结果
    };

    // 获取 Cipher 类的引用
    var Cipher = Java.use("javax.crypto.Cipher");

    // Hook `updateAAD` 方法
    Cipher.updateAAD.overload('[B').implementation = function(aad) {
        // 打印传入的 AAD（附加认证数据）
        console.log("updateAAD 被调用，传入的 AAD: " + aad);

        // 调用原始的 updateAAD 方法
        this.updateAAD(aad);
    };

    Cipher.doFinal.overload('[B').implementation = function(enc) {
        // 打印传入的 AAD（附加认证数据）
        console.log("doFinal 被调用，传入的 enc: " + enc);
        console.log("doFinal 被调用，传出的 dec: " + this.doFinal(enc));

        return this.doFinal(enc);
    };

    // 获取 SecretKeySpec 类的引用
    var SecretKeySpec = Java.use("javax.crypto.spec.SecretKeySpec");

    // Hook SecretKeySpec 构造方法
    SecretKeySpec.$init.overload('[B', 'java.lang.String').implementation = function(key, algorithm) {
        // 打印密钥字节数组
        console.log("SecretKeySpec 被调用，传入的 key: " + key);
        console.log("使用的算法: " + algorithm);

        // 调用原始构造方法
        return this.$init(key, algorithm);
    };
});
