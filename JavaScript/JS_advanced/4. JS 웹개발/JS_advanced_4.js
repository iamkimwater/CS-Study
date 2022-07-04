fetch('http://www.google.com')
	.then((response) => response.text())
	                                                     // fetch 실행될 때 함께 바로 실행되는 함수 아님
	                                                    // 서버에 반응(response)이 오고 나서야 실행됨
	                                                   // Callback 함수임
	                                                  // .then 메소드는 Callback 함수 등록해주는 기능
	                                                 // fetch 함수가 리턴하는 Promise 객체의 메소드
	.then((result) => { console.log(result); });
	                                               // 앞의 함수가 실행되고 나서 실행됨
																							  // 앞의 response.text의 리턴값이 result 파라미터로 넘어옴

