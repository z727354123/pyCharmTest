function ajax (
    url: string,
    success: (res:string, code:number) => void,
    error: (code:number) => void
) {
    return 'ok'
}

ajax(
    '1.txt',
    (res, code) => {
        return '123'
    },
    () => {
        return
    }
);
