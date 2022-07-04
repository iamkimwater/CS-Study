# Topic1. Interactive JS

## 01. id로 태그 선택
### 사용법
#### 형태
> **document.getElementById(' ')**
> - JS에 미리 만들어져 있는 `document`라는 객체의 `getElementById`라는 메소드를 사용
> - id속성을 통해 HTML 문서에서 해당 요소를 가져옴
>
> **예시**
> ```html
> // HTML 파일 //
> 
> <!DOCTYPE html>
> <html lang="ko">
> <head>
>   <meta charset="UTF-8">
>   <title>Kimwater</title>
> </head>
> <body>
>   <h1 id="title">I Am Kimwater</h1>
>   <script src="index.js"></script>
> </body>
> </html>
> ```
>
> ```javascript
> // index.js 파일 //
> 
> document.getElementById('title');
> ```

#### 코드 작성 시 주의 사항
> **getElementById 메소드**
> - Element에 -s 가 붙지 않음 (id값은 고유값이므로)
> - 대소문자 구분에 유의할 것
> - id명 작성 시 따옴표 빼먹지 않기
>
> **잘못된 예시**
> ```javascript
> document.getElementsById('title');   // -s
> document.getelementbyid('title');   // 대소문자
> document.getElementById(title);    // 따옴표
> ```

#### 기타 사항
> * HTML 문서에 존재하지 않는 id값을 선택하면 undefined가 아닌 null값이 출력됨



## 02. class로 태그 선택
### 사용법
#### 형태
> **document.getElementsByClassName(' ')**
> - JS에 미리 만들어져 있는 `document`라는 객체의 `getElementsByClassName`라는 메소드를 사용
> - class속성을 통해 HTML 문서에서 해당 요소를 가져옴
>
> **예시**
> ```html
> // HTML 파일 //
> 
> <!DOCTYPE html>
> <html lang="ko">
> <head>
>   <meta charset="UTF-8">
>   <title>Kimwater</title>
> </head>
> <body>
>   <h2 id="title">What is my REAL name?</h2>
>   <ul id="names">
>     <li class="name">김워터</li>
>     <li class="name">박워터</li>
>     <li class="name">임워터</li>
>     <li class="name">류워터</li>
>   </ul>
>   <script src="index.js"></script>
> </body>
> </html>
> ```
>
> ```javascript
> // index.js 파일 // 
> 
> document.getElementsByClassName('name');
> ```

#### 코드 작성 시 주의 사항
> **getElementsByClassName 메소드**
> - Element에 -s 가 붙음 (여러 class를 선택하는 것이므로)
> - 대소문자 구분에 유의할 것
> - class명 작성 시 따옴표 빼먹지 않기
>
> **잘못된 예시**
> ```javascript
> document.getElementByClassName('name');   // -s
> document.getelementsbyclassname('name');   // 대소문자
> document.getElementsByClassName(name);    // 따옴표
> ```

#### 기타 사항
> * 콘솔에 출력하면 배열의 형태로 출력되지만 배열은 아닌 유사배열(Array-Like Object)임
> * HTML 문서에 존재하지 않는 class값을 선택하면 빈 HTML Collection이 출력됨



## 03. tag로 태그 선택
### 사용법
#### 형태
> **document.getElementsByTagName(' ')**
> - JS에 미리 만들어져 있는 `document`라는 객체의 `getElementsByTagName`라는 메소드를 사용
> - tag속성을 통해 HTML 문서에서 해당 요소를 가져옴
>
> ```javascript
> // index.js 파일 // 
> 
> document.getElementsByTagName('button');
> ```

#### 코드 작성 시 주의 사항
> **getElementsByTagName 메소드**
> - Element에 -s 가 붙음 (여러 tag를 선택하는 것이므로)
> - 대소문자 구분에 유의할 것
> - tag명 작성 시 따옴표 빼먹지 않기
>
> **잘못된 예시**
> ```javascript
> document.getElementByTagName('button');   // -s
> document.getelementsbyTagname('button');   // 대소문자
> document.getElementsByTagName(button);    // 따옴표
> ```

#### 기타 사항
> * 콘솔에 출력하면 배열의 형태로 출력되지만 배열은 아닌 유사배열(Array-Like Object)임
> * HTML 문서에 존재하지 않는 tag값을 선택하면 빈 HTML Collection이 출력됨
> * HTML 문서에 존재하는 모든 tag값을 선택하게 되면 예기치 않은 오류가 발생할 수 있으므로 잘 사용되지 않음



## 04. css 선택자로 태그 선택
### 사용법
#### 형태
> **document.querySelector(' ')**
> - JS에 미리 만들어져 있는 `document`라는 객체의 `querySelector`라는 메소드를 사용
>
> **예시**
> ```html
> // HTML 파일 //
> 

> ```
>
> ```javascript
> // index.js 파일 // 
> 
> document.querySelector('');
> ```

#### 코드 작성 시 주의 사항
> **querySelector 메소드**
> - 대소문자 구분에 유의할 것
> - 태그명 작성 시 따옴표 빼먹지 않기
>
> **잘못된 예시**
> ```javascript
> document.queryselector('#name');   // 대소문자
> document.querySelector(#name);    // 따옴표
> ```

#### 기타 사항
> * 