# Topic3. 프로그래밍과 데이터

## 01. 객체 (Object)
### 사용법
#### 형태
> **{ 값 이름(Key): 값(Value), ··· }**
> - `{ }` 안에 Key, 콜론, Value, 쉼표로 구성
> - 위의 한 쌍을 속성(Property)이라고 함
> - Key를 Property Name, Value를 Property Value라고도 함
>
> **예시**
> ```javascript
> {
> 	name: 'Kimwater',       // Property 하나
> 	age: 34,               // Property 둘
> 	gender: female,       // Property 셋
> 	isSolo: true         // Property 넷
> }
> ```

#### 코드 작성 시 주의 사항
> **Key / Property Name / 값 이름**
> - 첫 번째 글자는 반드시 문자, 밑줄(_), 달러 기호($) 중 하나로 시작해야 함
> - 띄어쓰기 금지
> - 하이픈(-) 금지

#### 형태의 확장
> **Value / Property Value / 값**
> - 모든 자료형 가능
> - 또 다른 Property도 넣을 수 있음
>
> **예시**
> ```javascript
> {
> 	name: 'Kimwater',
> 	age: 34,
> 	gender: 'female',
> 	isSolo: true,
> 	favorites: {
> 		color: 'blue',
> 		drink: 'coffee',
> 		movie: 'Notebook'
> 	}
> }
> ```
