function solution(numbers) {
    let answer = '';
    const compareFn = (a, b) => {
        return Number(String(b)+String(a)) - Number(String(a)+String(b));
    }
    if(numbers.reduce((acc, curr) => (acc + curr), 0) === 0){
        return '0'
    }
    answer = numbers.sort(compareFn).join('');
    return answer;
}