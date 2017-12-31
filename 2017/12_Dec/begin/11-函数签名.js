function ajax(url, success, error) {
    return 'ok';
}
ajax('1.txt', function (res, code) {
    return '123';
}, function () {
    return;
});
