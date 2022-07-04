/*
// Arguments: 유사배열이므로 배열 메소드 사용 제한

function firstWords() {
  let word = '';

  for(const arg of arguments) {           // for of문: 반복 가능한 객체를 반복
    word += arg[0];
  }

  console.log(word);
}

firstWords('너는', '나의', '운명');                   // 너나운
firstWords('사랑스런', '나의', '코딩', '공부');       // 사나코공
firstWords('너를', '정복해', '버릴거야');            // 너정버
*/

/*
// Rest Parameter: 배열이므로 배열 메소드 자유롭게 사용

function firstWords(...args) {
  let word = '';

  for(const arg of args) {
    word += arg[0];
  }
	console.log(word);
}

firstWords('너는', '나의', '운명');                   // 너나운
firstWords('사랑스런', '나의', '코딩', '공부');       // 사나코공
firstWords('너를', '정복해', '버릴거야');            // 너정버
*/


/*
const getTwice = function(number) {
	return number * 2;
}
console.log(getTwice(6));


function getTwice(number) {
	return number * 2;
}
console.log(getTwice(6));

const getTwice = number => number * 2;
console.log(getTwice(6));
*/


