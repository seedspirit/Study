[원문](https://www.youtube.com/watch?v=sLJ8ypeHGlM)

#### Transaction이란?
- 단일한 논리적인 작업 단위 (a single logical unit of work)
- 논리적인 이유로 여러 SQL문들을 단일 작업으로 묶어서 나눠질 수 없게 만든 것
	- 계좌 이체를 구현한다고 했을 때 
		- 송금과 입금이 모두 성공해야 의미가 있음
		- 둘 중 하나만 성공하는 경우는 아예 없게 해야 함
- transaction의 SQL문들 중에 일부만 성공해서 DB에 반영되는 일은 일어나지 않음


#### Transaction 사용 패턴
1. Transaction을 시작(begin)한다.
2. 데이터를 읽거나 쓰는 등의 SQL문들을 포함해서 로직을 수행한다.
3. 일련의 과정들이 문제없이 동작했다면 transaction을 commit한다.
4. 중간에 문제가 발생했다면 transction을 rollback한다.


#### ACID
##### Atomicity (원자성)
- 모두 성공하거나 모두 실패하는 속성 (ALLor NOTHING)
- Transaction은 논리적으로 쪼개질 수 없는 작업 단위이기 때문에 내부의 SQL문들이 모두 성공해야 함
- 중간에 SQL문이 실패하면 지금까지의 작업을 모두 취소하여 아무 일도 없었던 것처럼 rollback한다

##### Consistency (일관성)
- Transaction은 DB 상태를 consistent 상태에서 또 다른 consistent 상태로 바꿔줘야 한다
- constraint, trigger 등을 통해 DB에 정의된 rules을 transaction이 위반했다면 rollback해야 한다
- transaction이 DB에 정의된 rule을 위반했는지는 DBMS가 commit하기 전에 확인하고 알려준다
- 그 외에 application 관점에서 transaction이 consistent하게 동작하는지는 개발자가 챙겨야 한다

##### Isolation (고립성)
- 여러 transaction들이 동시에 실행될 때도 혼자 실행되는 것처럼 동작하게 만든다
- DBMS는 여러 종류의 isolation level을 제공함
	- 엄격하면 결과물이 안정적인 대신에 DB Server 퍼포먼스가 낮음
	- 관대하면 DB Server의 퍼포먼스가 높지만 이상한 결과물이 나올 수 있음
- 개발자는 isolation level 중에 어떤 level로 transaction을 동작시킬지 설정할 수 있다
- concurrency control의 주된 목표가 isolation임

##### Durability (영존성)
- commit된 transaction은 DB에 영구적으로 저장한다
- 즉, DB system 문제 (power fail or DB crash)가 생겨도 commit된 transaction은 DB에 남아 있는다
	- '영구적으로 저장한다'라고 할 때는 일반적으로 '비휘발성 메모리(HDD, SSD, ...)에 저장함'을 의미한다
- 기본적으로 tansaction의 durability는 DBMS가 보장한다
