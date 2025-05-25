function solution(s) {
    const words = s.split(' ');
    
    const result = words.map((word) => ([...word].map((w, idx) => (idx % 2 === 0 ? w.toUpperCase() : w.toLowerCase()))).join('')).join(' ');
    
    return result
    
}