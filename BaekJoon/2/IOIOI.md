# IOIOI

소요시간: 40분

작성일시: 24.06.23 14:40:16

출처: https://www.acmicpc.net/problem/5525

### 접근 방법
(I)OI의 조합만으로 Pn을 만들 수 있다.

Pn을 통째로 비교하는 방법은 시간 초과를 발생시키므로, Pn을 만드는데 필요한 글자의 수와 S에 포함된 유효한 P 집합의 길이 및 수를 따로 저장하면 쉬이 계산할 수 있다.

### 시간 복잡도 분석
O(n)

### 새로 알게 된 것
~~는 32bit를 벗어나는 데이터를 truncate하는 효과가 있다.

i.e. ~~(32.9) === 32

i.e. ~~(-32.9) === -32

### 주의할 점
.

### 기타 코멘트
.

```python
const fs = require('fs')

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
const M = Number(input[1])
const S = input[2].trim() + 'x'

const PNLength = 2 * N + 1

let flag = false
let chunks = []
let curChunk = 0
for (let char of S) {
    if (!flag && (char === 'I')) {
        flag = true
        curChunk += 1
    } else if (flag && (char === 'O')) {
        flag = false
        curChunk += 1
    } else {
        if (curChunk > 2 && curChunk >= PNLength) {
            chunks.push(curChunk)
        }
        if (char === 'I') {
            curChunk = 1
            flag = true
        } else {
            curChunk = 0
            flag = false
        }
    }
}
let answer = 0
for (let chunk of chunks) {
    answer += ~~((chunk - PNLength) / 2) + 1
}
console.log(answer)
```
