쉘(Shell): 
- 사용자가 문자를 입력해 컴퓨터에 명령할 수 있도록 하는 프로그램
	- 사용자가 명령을 입력하면 쉘이 이 명령을 해석해서 커널이 이해할 수 있는 방법으로 변환해 전달
- 종류
	- sh: 최초의 쉘
	- bash: linux 표준 쉘
	- zsh: Mac 카탈리나 OS 기본 쉘

커널(Kernal):
* 물리적인 기계를 직접적으로 제어하는, 운영체제에서 중심이 되는 것

명령 & 결과 전달(& 해석) 프로세스:
- 명령 내리기: 사용자 -> 쉘 -> 커널 -> 하드웨어
- 결과 전달: 하드웨어 -> 커널 -> 쉘 -> 사용자


### 리눅스와 권한
- 운영체제는 사용자/리소스 권한을 관리
- 리눅스는 사용자/그룹으로 권한을 관리
- 파일마다 소유자, 소유자 그룹, 모든 사용자에 대해
	- 읽고 r, 쓰고 w, 실행 x 하는 권한을 관리함


### 리다이렉션과 파이프
* Unix에서 동작하는 프로그램은 커맨드 실행시 3개의 Stream이 생성됨
	* 표준 입력 스트림 (Standard Input Stream, stdin): 0으로 표현, 입력(비밀번호, 커맨드 등)
	* 표준 출력 스트림 (Strandard Output Stream, stdout): 1로 표현, 출력 값(터미널에 나오는 값)
	* 오류 출력 스트림 (Standard Error Stream, stderr): 2로 표현, 디버깅 정보나 에러 출력 ![[스크린샷 2022-12-23 오후 2.00.59.png]]
*  리다이렉션 (Redirection): 프로그램의 출력(stdout)을 다른 파일이나 스트림으로 전달
	* 주로 명령어 표준 출력이 아닌 파일에 쓸 때
	* >: 덮어쓰기(Overwrite) 파일이 없으면 생성하고 저장
	* >>: 맨 아래에 추가하기 (Append)![[스크린샷 2022-12-23 오후 2.04.18.png]]
* 파이프 (Pipe): 두 프로세스 사이에서 한 프로세스의 출력 스트림을 또다른 프로세스의 입력 스트림으로 사용할 때 사용
	* ![[스크린샷 2022-12-23 오후 2.04.39.png]]
	* `ls | grep files.txt`
		* ls 명령을 통한 출력 내용이 grep 명령의 입력 스트림으로 들어감


### 프로세스

##### 프로세스 vs 바이너리
- 코드 이미지 또는 바이너리: 실행 파일
- 프로세스: 실행 중인 프로그램

##### Foreground process & Background process
- Foreground process: 쉘에서 해당 프로세스 실행을 명령한 후, 해당 프로세스 수행 종료까지 사용자가 다른 입력을 하지 못하게 하는 프로세스
- Background process: 사용자 입력과 상관없이 실행되는 프로세스
	- 쉘에서 해당 프로세스 실행시, 맨 뒤에 &를 붙여줌
	- `find / -name '*.py' > list.txt &`


### bash shell
- sudo : 관리자 권한으로 실행하고 싶은 경우 사용
- pwd: 현재 디렉토리 위치 반환
- ls: 파일 목록 출력
	- ls -al: 숨겨진 파일 목록까지 출력 ![[스크린샷 2022-12-23 오후 1.31.26.png]]
- chmod: 파일 권한 변경
	- 숫자를 사용하는 방법은 ![[스크린샷 2022-12-23 오후 1.30.24.png]]
	* chmod -R: 하부 폴더, 파일 권한 설정을 싹다 바꾸는 옵션
```
chmod 400 mysecurity.pem
chmod 777 myfile.py
```
* cat: 파일 보기 (빠르게 파일 확인하기 위해 사용)

* rm: 파일 삭제하기 (리눅스에는 기본적으로 휴지통이 없어서 매우 주의)
	* -r: 하위 디렉토리를 포함한 모든 파일 삭제
	* -f: 강제로 파일이나 디렉토리 삭제
	- 주로 `rm -rf 디렉토리명` 을 자주 사용

* grep: 검색 명령
	* -i: 영문의 대소문자를 구별하지 않음
	* -v: pattern을 포함하지 않는 라인을 출력
	* -n: 검색 결과의 각 행의 선두에 행 번호를 넣는다
	* -l: 파일명만 출력한다
	* -c: 패턴과 일치하는 라인의 개수만 출력한다
	* -r: 하위 디렉토리까지 검색한다

* ps: 프로세스 상태 확인 (주로 aux 조합을 많이 사용)
	* -a: 시스템을 사용하는 모든 사용자의 프로세스 출력
	* -u: 프로세스 소유자에 대한 상세 정보 출력
	* -l: 프로세스 관련 상세 정보 출력
	* -x: 터미널에 로그인한 후 실행한 프로세스가 아닌 프로세스도 출력
		* 주로 데몬 프로세스(daemon process)까지 확인하기 위해 사용
			* 사용자 모르게 시스템 관리를 위해 실행되는 프로세스로 보통 시스템이 부팅될 때 자동 실행
		* 본래 ps 명령은 현재 shell에서 실행한 프로세스만 보여주기 때문에 이 옵션을 사용하는 경우가 많음
	- -e: 해당 프로세스와 관련된 환경 변수 정보도 함께 출력 
	- -f: 프로세스 간 관계 정보도 출력

- kill: 프로세스를 중지시키는 명령
	- kill % 작업 번호
	- kill 프로세스ID
	- kill -9: 강제 종료 옵션


### 하드링크와 소프트링크
- cp {복사하고자 하는 파일명} {복사결과물의 파일명} : 파일 복사
	- cp -rf * {복사하고자 하는 파일명} {복사결과물의 파일명} : 하위 폴더와 파일까지 통째로 복사
	- cp의 결과물은 완전히 다르기 때문에 A를 수정한다고 B에 반영되지 않음
- ln {A} {B} : 하드링크 - A를 수정하면 그 내용이 자동적으로 B에도 반영됨
	- A와 B는 독립적인 파일은 맞음. A파일을 지운다고 해서 B가 지워지지는 않음
- ln -s {A} {B} : 소프트 링크 (심볼릭 링크)
	- Window OS의 바로가기와 동일
	- ls -al 혹은 ll로 소프트 링크 확인 가능
	- A에서 뭘 수정하면 B로 접속해도 A를 확인하는 것이기 때문에 바뀐 것처럼 보임
	- rm A로 A를 삭제하면 B 파일은 존재하긴 하나, 해당 파일로 접근은 불가함