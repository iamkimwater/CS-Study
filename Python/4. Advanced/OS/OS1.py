# 7. 효율적이고 빠른 프로그램 - 논블로킹, 동시성
# 어떨게 하면 프로그램이 더 효율적으로 동작할까?
# 어떻게 하면 프로그램이 더 빠르게 동작할까?
# 어떻게 하면 파이썬이 더 빠르고 효율적으로 동작할까?


####################################################################################################
# 어떻게 하면 프로그램이 더 효율적으로 동작할까?
####################################################################################################
# 1. 블로킹 방식의 코드 흐름
# os가 io 집약적인 작업이 완료되었다고 알려줄 때까지
# cpu는 계산을 미루는 방식
# 단점: 효율은 없지만
# 장점: 코드가 진행되는데 아무런 문제가 없다

# 2. 논블로킹 방식의 코드 흐름
# os가 io 집약적인 작업이 완료되었다고 알려주는 것과 무관하게 (엽떡 도착했다고 알려주든 말든)
# cpu는 자신의 계산을 계속 진행하는 방식 (과제 진행)
# 장점: 효율적이지만
# 단점: 코드가 진행되는데 문제가 발생할 수 있다
# 해결법
# : 논블로킹 방식의 코드 흐름은 코드 실행 중 필요한 코드가 아직 없을 때 진행될 수 없다는 문제가 있다 (과제 중간에 엽떡이 필요한 경우 과제 진행 불가)
# : 제어권의 흐름을 제어해야 프로그램이 정상적으로 작동한다
# : 이 흐름을 제어하기 위해서 코루틴을 사용한다

# 3. sync 방식의 코드 흐름
# cpu쪽에서 os에게 io 작업 완료 여부를 주기적으로 질문하는 방식
# 주기적으로 확인해야 해서 비효율적이다

# 4. async 방식의 코드
# io 작업쪽에서 작업 완료 여부를 이벤트를 통해 os에게 알려주면 os가 cpu에게 인터럽트를 걸어서 작업 완료 여부를 알려주는 방식
# 작업이 완료된 후에 알려주기 때문에 효율적이다

# 결론
# 1. 블로킹 sync
# 하라는 과제는 안하고 엽떡이 오기를 기다리는데 + 계속 os에게 io 친구 어디쯤 왔는지 확인하는 방식

# 2. 논블로킹 sync + 코루틴을 통한 제어권 제어
# 과제를 계속 진행하면서 + 계속 os에게 io 친구 어디쯤 왔는지 확인하는 방식
# 엽떡이 필요한 과제가 존재하는 경우 엽떡을 사 오면 그 부분만 나중에 따로 진행할 수 있도록 코루틴으로 제어

# 3. 블로킹 async
# 하라는 과제는 안하고 엽떡이 오기를 기다리는데 + io 친구가 엽떡을 사오면 os가 알려준다

# 4. 논블로킹 async + 코루틴을 통한 제어권 제어(베스트 옵션 but 코드 복잡)
# 과제를 계속 진행하면서 + io 친구가 엽떡을 사오면 os가 알려준다
# 엽떡이 필요한 과제가 존재하는 경우 엽떡을 사 오면 그 부분만 나중에 따로 진행할 수 있도록 코루틴으로 제어
####################################################################################################


####################################################################################################
# 어떻게 하면 프로그램이 더 빠르게 동작할까?
####################################################################################################
# 1. 병렬 프로그래밍
# 서로 다른 cpu에서 독립적으로 작업하고 그 결과를 병합하는 패턴의 프로그래밍
# 서로 독립적이기 때문에 진정한 동시적 프로그래밍이다
# 서로 다른 컴퓨터에서 이루어 지기도 하는데, 이 경우를 특별히 분산 처리 시스템이라고 부른다
# 분산 처리 시스템을 활용하는 대표적인 분야가 슈퍼컴퓨터, 빅데이터이며, 이것을 다루기 위해 spark를 주로 사용한다
# spark는 map, filter, reduce, take 계열의 함수를 기본으로 사용한다

# 2. 동시성 프로그래밍
# 병렬 프로그래밍의 효과를 하나의 cpu에서 소프트웨어적으로 구현한 것
# 어떻게 하나의 cpu에서 일을 나누어 처리할 수 있을까?

# 일꾼의 원리(여러 명의 일꾼)
# 하나의 프로그램을 실행하는 여러명의 일꾼을 만들어서
# 일꾼들의 요청을 cpu가 매우 빠른 속도로 순차적으로 처리한다(어떤 순서로 일꾼들의 부탁을 cpu가 처리해 줄지 전략은 os가 결정)
# 일꾼 1의 요청을 처리하다가 > 일꾼 2의 요청을 처리하고 > ... = 컨텍스트 스위칭
# cpu의 계산 속도가 메모리의 처리 속도보다 훠얼씬 더 빠르기 때문에 그 어떤 프로세스도 중지되지 않는 것처럼 보인다
# 따라서 여러 프로세스가 동시에 일하는 것처럼 느껴진다

# 일꾼 종류1 = 프로세스
# 정의: 메모리 위에서 실행중인 프로그램
# 구조: 프로세스 상태(pc, register) + 스택 영역 + 힙 영역 + 데이터 영역 + 코드 영역
# 최소 1개의 메인 스레드를 보유
# 통신 방법: 파이프(같은 컴퓨터 내부에서), 소켓(다른 컴퓨터끼리)등을 활용
# 멀티 프로세스 프로그래밍의 문제점
# : 코딩이 쉽지만 컨텍스트 스위칭 비용이 크다 => 그래서 느리다
# : 데이터를 공유하지 않고 통신으로 해결할 수 있다 => 그러나 통신에 드는 비용이 크다
# : 만약에 공유 데이터 또는 공유 자원이 존재한다면 문제가 발생할 수 있다 => 락을 사용한 동기화로 문제를 해결하게 된다

# 일꾼 종류2 = 쓰레드
# 정의: 프로세스 내부의 프로그램 실행 흐름 단위, 하나의 프로세스에 여러 쓰레드가 존재할 수 있음
# 구조: 프로세스 상태(pc, register) + 스택 영역 + 힙 영역 + 데이터 영역 + 코드 영역 => 단, 스택 영역만 독립적
# 통신: 데이터를 공유하므로 통신할 일이 없음 but 공유데이터 문제 발생 -> 코딩 매우 어려움
# 컨텍스트 스위칭 비용이 적다 => 그래서 빠름
# 멀티 쓰레드 프로그래밍의 문제점
# : 만약에 공유 데이터 또는 공유 자원이 존재한다면 문제가 발생할 수 있다 => 락을 사용한 동기화로 문제를 해결하게 된다

# 결국 멀티 프로세스와 멀티 쓰레드에서 발생하는 문제
# 문제점: 공유 변수, 공유 자원 문제, 데드락
# 공유 변수, 공유 자원 문제 해결 방법: 락을 활용해서 쓰레드(프로세스)간의 경쟁 문제를 해결
# : 뮤텍스: 하나의 공유 변수, 혹은 컴퓨터 자원에 하나의 쓰레드(프로세스)만 접근할 수 있게 한다
# : 세마포어: 하나의 공유 변수, 혹은 컴퓨터 자원에 하나의 쓰레드(프로세스)만 접근할 수 있게 한다
# : 뮤텍스와 세마포어의 차이: 세마포어는 여러개의 뮤텍스로 생각할 수 있다
# 문제점: 데드락 = 여러 쓰레드(프로세스)가 서로에 의해 서로가 자원을 획득하지 못해 무한하게 대기하는 상태
# : 코드를 잘 짜거나 / 그냥 받아들인다

# 위의 문제들을 모두 해결했다고 가정하자
# 멀티 쓰레드 프로그래밍은 어떤 식으로 작동할까?(멀티 프로세스도 마찬가지)

# 1.
# 메인 쓰레드가 하나 있고, 필요한 경우 자식 쓰레드를 추가로 생성하고, 다 쓰면 삭제하는 방식
# 자식 쓰레드를 만들고 지우는데 시간이 걸림
# 자식 쓰레드를 유지할 필요가 없음

# 2.
# 처음부터 메인 쓰레드로부터 몇 명의 자식 쓰레드를 만들어 놓고 쓰레드 풀에 넣어둔 후 필요하면 가져다 쓰는 방식
# 자식을 만들고 지우는 시간이 안걸려서 속도가 빠름
# 자식 쓰레드를 계속 유지해야 함

# 3.
# 위의 2가지 방법 중 어떤 방법을 쓰더라도, 가게의 일을 여러 쓰레드가 분업해서 처리하는 것은 동일한데
# 이 분업을 어떻게 시키는지 2가지 방법이 있다
# 첫째, 개발자가 직접 각각의 쓰레드에게 해야할 작업을 나누어서 할당할 수도 있고(주인이 알바생들에게 작업을 가게 오픈 전부터 분업해 주는 경우)
# 둘쨰, 프로그램이 추가 쓰레드가 필요한 경우 알아서 작업을 맡길 수 있다(가게 운영 도중에 일손이 부족하면 알바생들이 알아서 분업하는 경우)

# 결론
# 선택 가능한 동시성 프로그래밍 옵션
# 멀티 프로세스 프로그래밍(속도가 크리티컬하지 않은 경우, 즉 앱 또는 웹 개발에 필요한 서버)
# 멀티 쓰레드 프로그래밍(속도가 중요한 경우, 즉 온라인 실시간 게임 서버, 다양한 클라이언트 프로그램)
####################################################################################################


####################################################################################################
# 지금까지의 효율과 속도 이야기를 실졔 예시로 이해해보자
####################################################################################################


####################################################################################################
# 예시1: n명의 사용자가 동시에 cpu 집약적인 연산(파스타 조리)을 많이 요청하는 하는 경우
# (c# 실시간 온라인 게임 서버 => 프레임 워크로 닷넷을 주로 쓴다)
# (자바 실시간 서비스 서버(배민) => 프레임 워크로 스프링을 주로 쓴다)
####################################################################################################
# 멀티 쓰레드를 잘못 활용하는 예: 일을 분업하지 않고 멀티 쓰레드를 하는 경우

# 예를 들어 서버가 해야 하는 모든 일(손님에게 주문을 받고, 요리를 만든 후, 완성된 요리를 손님에게 서빙)을 1번 쓰레드에게 시겼다고 가정하자
# 첫 손님의 일이 다 처리되지 않았는데 추가로 100명의 손님이 요리를 요청하게 된다면 어떻게 될까?
# 손님의 요청을 무시할 수 없으므로 가게의 사장님인 os는 다음 손님의 요청을 처리할 수 있도록
# 1번 쓰레드, 즉 메인 쓰레드에게 자식 쓰레드 100명을 추가적으로 생성하도록 요구하게 된다

# 문제는 쓰레드와 함께 요리를 하고 있는 cpu다
# cpu라는 주방은, 손님의 주문을 처리하려는 쓰레드와 함께 식당을 운영하고 있는데
# 문제는 현재 손님 101명을 위해 일하는 101명의 쓰레드의 모든 작업은
# cpu가 컨텍스트 스위칭을 하면서 동시에 처리하고 있다는 점이다
# 따라서 1명에서 101명으로 늘어난 파스타 조리 요청때문에, 파스타 하나를 조리하는 시간이 매우 느려지게 된다
# 결론적으로 파스타를 서빙하려는 쓰레드는 cpu와의 작업이 계속 느려져서 무한하게 대기해야 하는 상황이 되고
# 결국 그 어떤 손님의 요청도 처리되지 못하는 상황이 된다
# 이 때, 추가로 100명의 손님이 더 입장한다면...?
# 추가로 들어온 손님의 요청을 돌아볼 쓰레드가 아무도 없으므로(아직 101명의 쓰레드 모두 자신이 전담마크하는 손님의 파스타를 조리하는 중이다)
# 손님의 요청을 무시할 수 없는 가게의 사장 OS가 100명의 쓰레드를 추가로 고용하게 된다...
# 손님이 201명인데 손님을 일대일 마크하는 알바생도 201명...주방은 이제 동시에 201개를 조리중...
# 과연 이 식당이 운영이 될까? 더 이상의 자세한 설명은 생략한다...
# 이것을 서버가 다운됬다고 말한다

# 위의 문제 상황을 직관적으로 정리하자면
# 101명의 손님을 모두 전담마크하는 101명의 쓰레드를 고용하는 식으로 식당을 운영했는데
# 그 101명의 쓰레드가 사용하는 공용 주방은 1개 뿐이어서 모두의 요리가 늦춰지는 문제가 발생한 것이다
# 알바생은 끝없이 늘어나고, 조리시간은 계속 늘어나고, 손님은 모두가 기다리기만 하는 상황

# 이제 어떻게 이 문제를 해결하고 정상적으로 식당을 운영할 수 있을까?
# 정답은, 해야 할 일을 분업해서 여러 쓰레드에게 맡기는 것이다
# 위의 식당 운영에 문제가 발생한 이유는
# 하나의 쓰레드가 손님의 요청을 받고, 요리를 한 후, 서빙까지 모두 해야 하는 일대일 손님 전담마크 방식으로 가게를 운영했기 때문이다

# 우선 작업을 대략 4가지로 분업해보자
# 첫째, 손님의 요청을 받아서 큐에 담아두기만 하는 쓰레드
# 둘째, 큐에 쌓여있는 손님의 요청을 하나씩 꺼내서 확인하는 쓰레드
# 셋째, 꺼내서 확인한 손님의 요청을 보고 실제로 요리를 하는 쓰레드
# 넷째, 완성된 요리를 손님에게 서빙하는 쓰레드

# 위의 분업은 아래와 같은 효과를 만들어 낸다

# 첫째, 손님의 요청은 아무리 많아도 즉각적으로 처리된다
# => os가 손님의 요청을 처리하기 위해 추가적으로 쓰레드를 고용하지 않게 된다
# => 그런데 만약에 너무 너무 너무 너무 너무 많은 손님이 와서 주문을 하는 경우에는 쓰레드를 조금 더 고용할 수 있으나
# => 그럼에도 불구하고 제한은 둬야 식당이 정상적으로 운영되기 때문에, 쓰레드 풀의 쓰레드(워커) 개수를 제한해야 한다

# 둘째, 큐에 쌓여있는 손님의 요청을 하나씩 꺼내서 처리하므로 주방에서 101개의 파스타를 동시에 조리하지 않는다
# => 최소 1개, 최대로 큐에 쌓인 개수만큼의 파스타만 동시에 조리한다 => 파스타 1개의 조리시간이 극단적으로 낮아지지 않게 된다
# => 여러 쓰레드가 이 큐에 접근해서 일을 처리하려는 경우 공유 데이터 문제가 발생하니까 이 큐는 락을 걸어두고 처리한다
# => 이렇게 큐를 관리하는 쓰레드는 식당에서 총괄 셰프와 같다고 이해할 수 있다
# => 손님이 요청한 요리가 파스타인지, 물 한컵인지에 따라 작업 순서가 달라져야 하므로 우선순위 큐를 쓴다

# 셋째, 손님의 요청을 1개만 꺼내어 처리한다면 1명의 쓰레드가 조리하면 되고
# => 인기가 많아 짧은 시간 안에 큐에 10개 정도의 주문이 쌓였다면 10개의 쓰레드가 동시에 조리하면 된다
# => 즉 101개를 동시에 조리하지는 않지만, 1 ~ 10개정도의 파스타는 동시에 조리해서 cpu의 능력에 어울리는 최적의 속도감을 유지한다

# 넷째, 조리가 완성된 즉시 손님에게 요리를 서비스해서 다른 일을 하는 쓰레드들이 자신의 일에 끊기지 않고 집중할 수 있도록 한다

# 따라서 101명의 유저가 요청을 해도
# 모든 유저의 주문을 거의 동시에 빠르게 받고
# 모든 유저들의 요청을 거의 동시에 빠르게 처리해서 서빙하므로
# 101명은 마치 거의 동시에 서비스를 받는 것 처럼 느낀다
####################################################################################################


####################################################################################################
# 예시2: n명의 사용자가 동시에 io 집약적인 작업(이마트에서 초밥 사와서 내놓기)을 많이 요청하는 경우
# (자바스크립트 웹 서버 => 프레임워크로 주로 node.js를 사용한다)
# (파이썬 웹 서버 => 프레임워크로 주로 Django를 사용한다)
####################################################################################################
# 우선 멀티 프로세스는 싱글 쓰레드로 생각한다

# 우리 가게의 알바생인 쓰레드가 한 명 뿐이라는 사실을 생각해보자
# 101명의 유저가 와서 이마트 초밥을 주문하는 경우
# 1번 유저의 초밥이 도착한 후에서야 2번 유저의 주문을 받게 된다면 식당은 망할 것이다
# 따라서 쓰레드가 한 명인 경우 반드시 논블로킹 방식으로 일을 처리해야 한다

# 논블로킹 방식의 일의 흐름을 생각하면 아래와 같다
# 1. 1번 손님의 요청을 받는다
# => 쓰레드는 메인 홀을 제어한다

# 2. 1번 손님의 초밥을 사기 위해 os가 io 친구에게 초밥을 구매하라고 부탁한다
# => 쓰레드는 초밥 사오기 함수를 실행한다

# 3. 1번 손님의 초밥이 돌아오면 추가로 진행할 일을 콜백으로 등록해두고 다시 메인 홀로 돌아간다
# => 초밥이 도착하면 수행할 콜백 함수를 등록하고, 쓰레드는 다시 메인 홀을 제어하기 시작

# 4. 2번 손님의 주문을 받는다
# => 쓰레드는 메인 홀을 제어하고 있다

# 5. 2번 손님의 초밥을 사기 위해 os가 io 친구에게 초밥을 구매하라고 부탁한다
# => 이 때, io 작업은 내부적으로 멀티 쓰레드로 동작해서 여러명의 부탁도 매우 빠르게 처리된다
# => 초밥이 도착하면 수행할 콜백 함수를 등록하고, 쓰레드는 다시 메인 홀을 제어하기 시작

# 6. 이제 창고(이벤트 큐)에 가서 혹시 1번 손님의 초밥이 도착했는지 확인한다
# => 쓰레드가 메인 홀로 돌아가기 전에 주기적으로 창고(이벤트 큐)를 확인해서 io가 초밥을 사다놓았는지 확인한다
# => 이벤트 큐에 초밥이 도착했는지 주기적으로 체크하므로, sync 방식이다

# 7. 만약 초밥이 도착했다면 홀에 있다가 다시 1번 손님에게 돌아가서 이마트에서 사온 초밥을 서빙한다
# => 만약 초밥이 창고에 있었다면 쓰레드는 메인 홀 제어를 잠시 멈추고 1번 손님의 요청을 처리하는 함수 안에 들어가서 제어를 시작한다
# => 알고보니, 초밥 창고에는 io 친구가 사온 초밥 + 그 초밥 사오면 하려고 했던 콜백 함수가 모두 들어있었다
# => 이 때 아까 3단계에서 등록해 두었던 콜백 함수를 실행한다

# 8. 1번 손님에 대한 일이 끝나면 다시 홀로 돌아가 3번 손님의 주문을 처리한다
# => 콜백 함수를 다 실행하면 쓰레드는 다시 메인 홀을 제어하기 시작

# 9. 위의 과정을 반복

# 따라서 101명의 유저가 요청을 해도
# 모든 유저의 주문을 거의 동시에 빠르게 받고
# 모든 유저들의 요청을 거의 동시에 빠르게 처리해서 서빙하므로
# 101명은 마치 거의 동시에 서비스를 받는 것 처럼 느낀다
####################################################################################################


####################################################################################################
# 위의 두 식당이 운영 방식은 유지한 채로 손님이 바뀐다면 어떻게 될까?
####################################################################################################
# 파스타 식당이 이마트 초밥을 사와서 서빙해야 하는 요청을 주로 받게 될 경우
# => 5인분의 요리를 동시에 할 수 있게 유능한 조리사 쓰레드를 5명 고용했는데
# => 실제로 해야하는 일은 이마트에 가서 초밥을 사오는 일이어서
# => 결론1: 쓰레드를 낭비하게 된다

# => 그러나 유능한 조리사 쓰레드를 여러명 고용하지 않은 경우라면?
# => 제어권을 교환하지 않고도 한 명의 쓰레드가 블로킹 방식으로 초밥이 도착하기를 기다리는 동안
# => 다른 쓰레드가 다른 손님의 주문을 받을 수도 있다
# => 다만 이 방식을 쓰려면 손님의 수가 101명이어도 주문은 제한된 쓰레드가 받아야 되기 떄문에 쓰레드 풀을 써서 쓰레드 생성 개수를 제한해야 한다
# => 결론2: 이렇게 식당을 운영하면 멀티 쓰레드로도 좋은 효율을 낼 수 있다

# 이마트 초밥을 사와서 내던 식당(자바스크립트 웹 서버)이 파스타 요청(동영상 인코딩)을 주로 받게 될 경우
# => 쓰레드가 1명 뿐이므로 1번 손님의 파스타 조리가 끝나야만 2번 손님의 주문을 받을 수 있어서
# => 결론3: 아무리 논블로킹으로 무언가를 하려고 해도 결국 식당이 망한다
####################################################################################################


####################################################################################################
# 프론트엔드 개발자는 동시성 프로그래밍을 배워야 하는가?
####################################################################################################
# 웹: 브라우저 개발자
# 앱: 안드로이드 ios 개발자
# 게임: 유니티 개발자

# 브라우저, 안드로이드, ios, 유니티와 같은 프로그램은 내부적으로 렌더링, 데이터, 네트워크 등의 작업을 멀티 쓰레드로 처리
# 그러나 프론트엔드 개발자는 그 중에서 화면을 그리고 데이터를 관리하는 일을 주로 처리하고, 이는 하나의 메인 쓰레드로 동작한다

# 만약에 유니티, 브라우저, 안드로이드, ios를 만드는 개발자라면: 블로킹 멀티쓰레드
# 만약에 유니티, 브라우저, 안드로이드, ios 위에서 어플리케이션을 만드는 개발자라면: 논블로킹 싱글쓰레드

# 지원하고자 하는 직무에 따라 다르다
# 일반적인 프론트엔드 개발자는 논블로킹 싱글쓰레드 프로그래밍이 중요하다
####################################################################################################
# 백엔드 개발자는 동시성 프로그래밍을 배워야 하는가?
####################################################################################################
# 스타트업의 앱, 웹서버: 논블로킹 멀티 프로세스(싱글 쓰레드)
# 대기업의 앱, 웹서버: 블로킹 멀티 쓰레드
# 실시간 온라인 게임 서버: 블로킹 멀티 쓰레드
# 지원하고자 하는 직무에 따라 다르다
####################################################################################################


####################################################################################################
# 효율적이고 빠른 파이썬 프로그램 개발
####################################################################################################
# 파이썬의 GIL
# GIL이란 Global Interpreter Lock의 약자

# python은 기본적으로 가비지 콜렉터와 reference counting을 통해 할당된 메모리를 관리합니다
# 파이썬은 메모리 관리를 위해 객체의 소멸과 생성을 reference count로 판단
# reference count가 0이 되면 가비지 콜렉터가 메모리를 해제
# 따라서 파이썬의 모든 객체는 refernce count, 즉 해당 변수가 참조된 수를 저장하고 있습니다.
# 여기서 문제가 발생합니다

# 멀티스레드인 경우 여러 스레드가 하나의 객체를 사용한다면 refernce count를 관리하기 위해서 모든 객체에 대한 lock이 필요할 것입니다
# 이러한 비효율을 막기 위해서 python에서 GIL을 사용하게 되었습니다.
# 하나의 Lock을 통해서 모든 객체들에 대한 refernce count의 동기화 문제를 해결한 것이죠

# 그리고 바로 이러한 gil 떄문에 cpu 집약적인 코드를 실행하면
# 멀티 쓰레드 프로그래밍이 동시성 효과를 보지 못하게 되어 오히려 느려지게 된다

# 종합 총정리
# 파이썬으로 프로그램을 만든다면 상황에 맞추어 선택해야 한다
# cpu 연산이 많다면 멀티 쓰레드 => 이게 파이썬에서는 의미가 없어진다(gil 떄문) => 멀티 프로세스를 쓸 수 밖에 없다 => 이것도 무리수... => 동시성 프로그래밍 포기
# io 작업이 많다면 멀티 프로세스(싱글 쓰레드) 논블로킹 또는 제한된 숫자의 멀티 쓰레드

# 기타
# 데몬 쓰레드란?
# 백그라운드에서 실행된다
# 백그라운드에서 무한 대기하다가 이벤트에 따라 일을 하는 작업 담당(가비지 콜렉터)
####################################################################################################