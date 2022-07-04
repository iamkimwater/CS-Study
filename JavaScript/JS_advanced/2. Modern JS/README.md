# Topic2. Modern JS

## 01. Modern JS란?
### 현시점에 사용하기 적합한 범위 내에서 최신 버전의 표준을 준수하는 JS

> ECMA Script 2015 = ES6
> * JS 발전에 매우 큰 영향을 준 버전
> * 이후 1년에 1번 씩 새로운 버전 출시
> 

## 00. 함수 선언식 VS 함수 표현식

### 함수 선언식 (Function Declaration)

> **예시**
> 
> ```javascript
> function myFunc() {
> 	return 'Who are you?';
> }
> ```

### 함수 표현식 (Function Expression)

> **예시**
> 
> ```javascript
> var myFunc = function() {
> 	return 'Who are you?';
> }
> myFunc();
> ```

### cf ) 기명 함수 표현식 (Named Function Expression)

> **예시**
> 
> ```javascript
> // 함수 표현식 //
> const sayHi = function () {
>   console.log('Hi');
> };
> 
> console.log(sayHi.name); // sayHi
> 
> 
> // 기명 함수 표현식 //
> const sayHi = function printHiInConsole() {
>   console.log('Hi');
> };
> 
> console.log(sayHi.name); // printHiInConsole
> ```

### 호이스팅에 의한 영향

> * 함수 선언식: 호이스팅에 영향을 받음
> * 함수 표현식: 호이스팅에 영향을 받지 않음
> 
> **예시**
> 
> ```javascript
> logMessage();
> sumNumbers();
> 
> function logMessage() {              // 함수 선언식
> 	return 'worked';
> }
> 
> var sunNumbers = function() {     // 함수 표현식
> 	return 10 + 20;
> }
> ```
> 
> 위의 코드를 호이스팅에 의해 아래와 같이 인식함
> 
> ```javascript
> function logMessage() {
> 	return 'worked';
> }
> 
> var sunNumber;
> 
> logMessage();     // 'worked'
> sumNumbers();    // Uncaught TypeError: sumNumber is not a funtion
> 
> sunNumbers = function() {
> 	return 10 + 20;
> }
> ```

---

> 프로퍼티가 함수일 경우 메소드라 함

---

### Arrow Function
 
>  **예시**
> 
>  ```javascript
>  // 일반적인 함수 1 //
> const getTwice = function(number) {
> 	return number * 2;
> }
> 
> console.log(getTwice(6));
> 
> // 일반적인 함수 2 //
> function getTwice(number) {
> 	return number * 2;
> }
> 
> console.log(getTwice(6));
> 
> // Arrow 함수 //
> const getTwice = number => number * 2;
> 
> console.log(getTwice(6));
>  ```

 ---

 ## 00. 에러 객체

### `try` `catch` 문
> **예시**
>
> ```javascript
> try {
> 	console.log('에러 전');
> 
> 	const codeit = '코드잇';
> 	console.log(codeit)
> 
> 	codeit = 'codeit';
> 
> 	const language = 'JavaScript';
> 	console.log(language);
> } catch (error) {
> 	console.log('에러 후');
> }
> ```
>
> * `try` 부분에서 에러가 발생한 부분 이후의 코드는 실행되지 않음



### 콜백 함수

어떤 이벤트가 발생했거나 특정 시점에 도달했을 때 시스템에서 호출하는 함수
* 대표적으로 이벤트 핸들러 처리 (이벤트 발생했을 떄 이벤트 핸들러가 콜백함수 호출)
* 

### for each 문

* Array 객체에서만 사용가능한 메소드
* 배열을 처음부터 마지막까지 반복하며 item 추출 가능
* 인자(argument)로 Callback 함수 등록 가능
* 배열의 각 요소들이 파라미터로 전달되어 반복될 때 Callback 함수 호출
* Callback함수의 첫 번째 파라미터로 배열의 요소를 전달하면서 함수 반복 실행
* Callback함수에 파라미터 한 개 반드시 작성해야 함
* 파라미터로 index
* 비슷하게 `map` 메소드가 있는데 이는 새로운 배열을 출력하고자 할 때 사용

### for in 문

* 객체에서 사용 가능
* 객체의 `key`, `value`값 추출에 유용
* `key`값의 개수만큼 반복





---





## 00. 모듈

### 모듈이란?
> * 자바스크립트 파일의 하나
> * 복잡하고 많은 양의 코드를 기능에 따라 각각의 파일로 나눠 관리하면
>> 
>> **장점**
>> * 코드의 효율적 관리 가능
>> * 비슷한 기능이 필요할 때 다른 프로그램에서 재사용 가능

### 모듈 스코프

> * 모듈 파일 안에서 선언한 변수는 외부에서 자유롭게 접근할 수 없도록 해야 함
> * 모듈은 파일 안에서 모듈 파일만의 독립적인 스코프를 가지고 있어야 함
> * HTML파일에서 자바스크립트 파일을 불러올 때 모듈 스코프를 갖게 하려면 `script`태그에 `type`속성을 `module`이라는 값으로 지정해 주어야 함
> 
> ```javascript
> <body>
>   <script type="module" src="index.js"></script>
> </body>
> ```

### 모듈 문법

> * 기본적으로 `export`와 `import` 가 있음
> * 모듈 스코프를 가진 파일에서 외부로 내보내고자 하는 변수나 함수를 `export` 를 통해 내보냄
> * 모듈 파일에서 내보낸 변수나 함수들을 다른 파일에서 `import` 를 통해 가져옴
> 
> ```javascript
> // printer.js //
> export const title = 'CodeitPrinter';
> 
> export function print(value) {
>   console.log(value);
> };
> 
> // index.js //
> import { title, print } from './printer.js';
> print(title);
> ```
> 
> #### 1. 이름 바꿔 import
> 
> * `as` 를 활용하면 `import`하는 대상들의 이름을 변경할 수 있음
> * 여러 파일에서 불러오는 대상들의 이름이 중복되는 문제를 해결할 수 있음
> 
> ```javascript
> import { title as printerTitle, print, printArr } from './printer.js';
> import { title, data as members } from './members.js';
> 
> printer(title);
> arrPrinter(members);
> ```
> 
> #### 2. 한꺼번에 import
> 
> * `*`와 `as`를 활용하면 모듈 파일에서 `export`하는 모든 대상을 하나의 객체로 불러올 수 있음
> 
> ```javascript
> import * as printerJS from './printer.js';
> 
> console.log(printerJS.title);      // CodeitPrinter
> console.log(printerJS.print);     // ƒ print(value) { console.log(value); }
> ```
> 
> #### 3. 한꺼번에 export
> 
> * 선언된 변수나 함수를 하나의 객체로 모아 한꺼번에 내보낼 수 있음
> * `as` 를 활용하면 이름을 변경 가능
> 
> ```javascript
> const title = 'CodeitPrinter';
> 
> function print(value) {
>   console.log(value);
> }
> 
> function printArr(arr) {
>   arr.forEach((el, i) => {
>     console.log(`${i + 1}. ${el}`);
>   });
> }
> 
> export { title as printerTitle, print, printArr };
> ```
> 
> #### 4. default export
> 
> * `export`를 할 때 `default` 를 함께 사용하면 모듈 파일에서 기본적으로 `export`할 대상을 정할 수 있음
> * 일반적으로 모듈 파일에서 `export` 대상이 하나라면 `default` 를 활용하는 것이 조금 더 간결
> 
> ```javascript
> const title = 'CodeitPrinter';
> 
> function print(value) {
>   console.log(value);
> }
> 
> export default print;
> ```
> 
> * `default export`는 `import`할 때 기본적으로 아래와 같이 불러올 수 있지만,
> 
> ```javascript
> import { default as printerJS } from './printer.js';
> 
> console.log(printerJS.title);      // CodeitPrinter
> console.log(printerJS.print);     // ƒ print(value) { console.log(value); }
> ```
> 
> * 아래와 같이 축약형 문법으로 `import` 할 수도 있음
> 
> ```javascript
> import printerJS from './printer.js';
> 
> console.log(printerJS.title);      // CodeitPrinter
> console.log(printerJS.print);     // ƒ print(value) { console.log(value); }
> ```
>
> #### 5. 정리
> 
> * `export`를 할 때도 선언문을 `export`하거나
> 
> ```javascript
> export const title = 'Module';
> ```
> 
> * 선언된 변수나 함수를 코드 블록으로 묶어서 `export`할 수도 있고,
> 
> ```javascript
> const printer = (value) => {
>   console.log(value);
> };
> 
> const arrPrinter = (arr) => {
>   arr.forEach((el, i) => {
>     console.log(`${i + 1}. ${el}`);
>   })
> };
> 
> export { printer, arrPrinter };
> ```
> 
> * `as` 를 통해 이름을 변경해서 `export`를 할 수도 있음
>
> ```javascript
> const printer = (value) => {
>   console.log(value);
> };
> 
> const arrPrinter = (arr) => {
>   arr.forEach((el, i) => {
>     console.log(`${i + 1}. ${el}`);
>   })
> };
> 
> export { printer as namedPrinter, arrPrinter };
> ```
> 
> * 그리고 `default` 를 통해 표현식을 `export`하는 방법도 배우면서,
> 
> ```javascript
> const title = 'Module';
> 
> export default title;
> ```
> 
> * 여러 대상을 객체 값으로 모아 내보내는 방식도 가능함
> 
> ```javascript
> const title = 'Module';
> 
> const printer = (value) => {
>   console.log(value);
> };
> 
> const arrPrinter = (arr) => {
>   arr.forEach((el, i) => {
>     console.log(`${i + 1}. ${el}`);
>   })
> };
> 
> export default { title, printer, arrPrinter };
> ```
> 
> * `import` 이후에 중괄호를 감싸면 모듈 파일에서 `export`하는 항목들을 선택적으로 불러올 수 있고
> 
> ```javascript
> import { title, data } from './modules.js';
> ```
> 
> * `as` 를 통해서 이름을 바꿀 수도 있음
> 
> ```javascript
> import { title as moduleTitle, data } from './modules.js';
> ```
> 
> * `*`를 통해서 `export`된 항목들을 모두 불러올 수도 있음
> 
> ```javascript
> import * as modules from './modules.js';
> ```
> 
> * `default export`된 대상을 `import`할 때는
> 
> ```javascript
> import { defult as modules } from './modules.js';
> ```
> 
> * 아래 코드처럼 축약형으로 불러올 수 있음
> 
> ```javascript
> import modules from './modules.js';
> ```
> 
> * 심지어 이러한 방식들을 잘 응용하면,
> 
> ```javascript
> // modules.js //
> import module1 from './sub-module1.js';
> import module2 from './sub-module2.js';
> import module3 from './sub-module3.js';
> 
> export { module1, module2, module3 };
> 
> // index.js //
> import { module1, module2, module3 } from 'modules.js';
> ```