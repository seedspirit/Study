[[RDBMS]]의 한 종류

#### 1. MySQL 터미널에서 접속하기

아래 코드로 터미널에서 mysql 접속
```
cd /usr/local/mysql/bin
./mysql -p
```

아니면 터미널 키자마자 아래 코드 갈기기
```
mysql -u root -p
```



#### 2. SQL 명령어 - DDL

- STEP 1. 데이터베이스 생성
	- CREATE DATABASE {데이터베이스명}; : 데이터베이스 생성
	- SHOW DATABASES; : 생성된 데이터베이스 목록 출력
	- DROP {데이터베이스명} : 데이터베이스 삭제
		- IF EXISTS: 삭제시 조건

- STEP 2. 데이터베이스 사용
	- USE {데이터베이스명}; : 데이터베이스 사용

- STEP 3-1. 테이블 생성
	- CREATE TABLE {테이블명}; : 테이블 생성
		- 숫자형 옵션 사항
			- UNSIGNED : 음수로 입력값을 넣지 못하게
			- NOT NULL: 해당 칼럼의 레코드를 NULL 상태가 되지 못하게 강제
			- AUTO_INCREMENT: 해당 칼럼의 데이터 등록시 숫자가 1씩 증가하여 저장됨 
		```
		CREATE TABLE product (
		key INT AUTO_INCREMENT NOT NULL,
		title VARCHAR(20) NOT NULL,
		price INT NOT NULL,
		PRIMARY KEY (key)
		);
	   ```
	- SHOW TABLES: 생성된 테이블 목록 출력
	- DESC {테이블명}: 테이블 세부정보 조회
	- DROP {테이블명}: 테이블 삭제

- STEP 3-2. 테이블 구조 수정
	- 기본: ALTER TABLE {테이블명} ~ COLUMN 
	- ALTER TABLE {테이블명} ADD COLUMN  {추가할칼럼이름} {자료형} : 테이블에 필드 추가
		- ex. `ALTERT TABLE customer_db ADD COLUMN model_type VARCHAR(10) NOT NULL;`
	- ALTER TABLE {테이블명} MODIFY COLUMN {수정할칼럼이름} {변경할칼럼타입} : 칼럼의 칼럼 타입 수정
		- ex. `ALTERT TABLE customer_db MODIFY COLUMN model_type INT NOT NULL;`
	- ALTER TABLE {테이블명} CHANGE COLUMN {기존칼럼명} {변경할칼럼명} {변경할칼럼타입} : 테이블 칼럼 이름 변경
		- ex. `ALTERT TABLE customer_db CHANGE COLUMN model_type  modle_name VARCHAR(20) NOT NULL;`
	- ALTER TABLE {테이블명} DROP COLUMN {삭제할칼럼명}: 테이블 칼럼 삭제
		- ex. `ALTERT TABLE customer_db DROP COLUMN modle_name;
