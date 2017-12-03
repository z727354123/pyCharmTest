var b = 12;
console.log(b);
b = 'abc';
console.log(b);
// 编译不报错，
// 一开始没赋值，默认就是 any 类型
var a;
a = 123;
console.log(a);
a = 'abc';
console.log(a);
// 一开始有赋值，默认类型会被确定
var c = 123;
// c = 'abc'
// error TS2322: Type '"abc"' is not assignable to type 'number'.
