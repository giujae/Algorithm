function solution(array, commands) {
    let answer = [];
    for(let i=0; i<commands.length; i++){
        const[start, end, target] = commands[i];
        const calcArray = array.slice(start-1, end).sort((a,b) => (a-b));
        const result = calcArray[target-1];
        answer.push(result);
    }
    return answer;
}