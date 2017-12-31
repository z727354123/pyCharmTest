// 参数 类型
function myFun (a: number, b = 1) {
    console.log(a + b);
}
// myFun(); 必须要有 1-2 个参数
// error TS2554: Expected 1-2 arguments, but got 0.

// myFun(1, '1')    默认值，默认类型声明
// error TS2345: Argument of type '"1"' is not
// assignable to parameter of type 'number'.

myFun(1)


// 返回值类型
function myFun2 (a, b):number {
    return a + b
}
// 返回值是 变量，就检测不了
myFun2('2', '2')

function myFun3 (a, b):number {
    // return '123'
    // error TS2322: Type '"123"' is not assignable to type 'number'.

    // return a + b + '1'
    // error TS2322: Type '"123"' is not assignable to type 'number'.

    return
    // 这样就不报错 。。。

    // 什么都不写就报错
    // error TS2355: A function whose declared type is neither
    // 'void' nor 'any' must return a value.
}
// 返回值是 变量，就检测不了
myFun3('2', '2')

// 箭头函数
let myFun4 = ():number => {
    return 123
}

