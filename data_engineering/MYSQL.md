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


#### 3. SQL 명령어 - DML

1. Create (데이터 생성)
- 기본: INSERT INTO
	- INSTERT INTO {테이블명} ({칼럼명}) VALUES (값, 값, 값...); : 특정 칼럼에 특정 데이터 넣기
		- ex. `INSERT INTO mytable (name, model_type) VALUES ('i7', '8800')`

2. Read (데이터 읽기)
- 기본: SELECT FROM
	- SELECT {읽고 싶은 컬럼명} FROM {테이블명} : 테이블의 레코드 읽어오기
		- ex. `SELECT * FROM mytable : mytable 테이블의 전체 레코드 읽어오기`
		- ex. `SELECT name, model_type FROM mytable` 
	- SELECT {읽고 싶은 컬럼명} AS {바꿀컬럼이름} FROM {테이블명} : 테이블의 특정 컬럼을 읽어오되 지정한 이름으로 다르게 가져오기
		- ex. `SELECT name AS myname, type AS mytype FROM mytable`
	- 조건문 WHERE : 조건에 맞는 데이터만 소팅해서 읽어오기
		- 비교연산자인 <, >, = 사용 가능
		- 논리연산자인 AND OR 사용 가능
		- `SELECT name FROM mytable WHERE id <= 5 AND price < 3000;`
	- LIKE: 부분 일치 데이터를 읽음 (= 는 전체가 다 맞아야 하고, LIKE는 부분일치. 약간 정규표현식 느낌)
		- '가%': '가'로 시작하는 데이터
		- '%가': '가'로 끝나는 데이터
		- '%가%': '가'가 들어가 있는 모든 데이터
		- '가__': '가'뒤에 두 텍스트가 있는 경우
			- ex. `SELECT name FROM mytable WHERE name LIKE '%가'`
	- ORDER BY {칼럼이름}: 데이터를 정렬해서 읽어오기
		- DESC: 내림차순으로 / ASC: 오름차순으로
			- ex. `SELECT name FROM mytable WHERE id > 7 AND ID < 9 ORDER BY id ASC`
	- LIMIT: 조건에 맞는 데이터 중 일부만 가져오는 (head랑 비슷)
		- ex. `SELECT name AS myname FROM mytable WHERE name LIKE '%나%' LIMIT 5;`
- 조건문 순서는 WHERE -> LIKE -> ORDER BY -> LIMIT


3. Update (데이터 수정)
- 기본: UPDATE SET
	- Pandas 값 업데이트 명령문 작성이랑 좀 비슷한듯
	- UPDATE {테이블명} SET {수정하고싶은칼럼명} = {수정하고 싶은 값} WHERE {특정 칼럼} = {값}
		- ex. `UPDATE mytable SET name='i7', model_type='4132' WHERE id=3;`

4. DELETE (데이터 삭제)
- 기본: DELETE FROM 
	- DELETE FROM {테이블명} WHERE ~
		- 애초에 RDBMS에서 데이터를 삭제한다는 것은 행 자체를 지운다는 뜻이기 때문에 DELETE 다음에 바로 FROM이 나오는듯
		- ex. `DELETE FROM mytable WHERE id=3;`


#### 4. SQL 명령어 - DCL
- MYSQL 사용자 확인, 추가, 비밀번호 변경, 삭제
	- `create user '{만들고자하는아이디}'@localhost identified by '{비밀번호}'` : 로컬에서만 접속 가능한 userid 생성
	- `create user '{만들고자하는아이디}'@'%' identified by '{비밀번호}'` : 모든 호스트에서 접속 가능한 userid 생성
	- `SET PASSWORD FOR '{유저아이디}'@'%' = '{신규비밀번호}'`
	- `mysql > drop user '{userid}'@'%';` : 사용자 삭제
- MYSQL 접속 허용 관련 설정
	- `mysql > SHOW GRANTS for {아이디}` : 현재 부여된 권한 확인하기
	- `mysql > GRANT ALL ON DATABASES.TABLE to 'root'@localhost`: 로컬에서만 접속 허용
	- `mysql > GRANT SELECT, UPDATE ON DATABASES.TABLE to 'root'@localhost` : 특정권한만 부여 (select, update 만)
