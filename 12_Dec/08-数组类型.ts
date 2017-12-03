var arr = [1, 2, 4, 'abc']
// 这里 也有 隐式类型声明
// arr[2] = {};
// error TS2322: Type '{}' is not assignable to type 'string | number'.
console.log(arr);

// 升级版
var arr2 = Math.random() > 0.5 ? [1, 'ab', {}] : [1, 2, 3]
arr2[0] = false;
// 此时 arr2 是 any 数组
console.log(arr2);

var arr3:any[] = [1, 2, 3]
arr3[0] = false;
console.log(arr3);

