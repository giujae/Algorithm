function solution(numbers) {
    const compareFn = (a, b) => {
        return +(b +''+ a) - (a+''+b)
    }
    let answer = '';
    answer = numbers.reduce((a, b) => (a + b)) === 0 ? '0' : numbers.sort(compareFn).join('')
    return answer;
}