웹에서 사용하는 HTTP request는 기본적으로 다른 도메인의 데이터를 요청할 수 있음
	- 예:
		- 내가 접속한 웹페이지: www.fun-coding.org/index.html
		- 해당 웹페이지 안에서 <img 태그로 www.kkk.co.kr/google.jpg 파일을 가져와서 이미지로 보여줄 수 있음
		- 해당 웹페이지 안에서 <link> 태그로 www.kkk.co.kr/style.css 파일을 가져와서 CSS 스타일을 적용할 수도 있음
		- 하지만! **<scripit> </script>  태그로 둘러쌓인 스크립트 코드에서 실행되는 HTTP request는 www.fun-coding.org 에만 요청할 수 있음**
		* 정확하게는 **프로토콜, 호스트명, 포트가 동일**해야 함
		* 이를 **Same Origin Policy**라고 함

>  ajax, axios와 같이 <scripit> </script>  안에서 HTTP Request를 보낼 수 있는 기능이 생김에 따라, 해당 태그 내에서도 다른 사이트의 데이터 요청을 지원해야 한다는 요구가 생겨 CORS라는 가이드가 마련됨 (각 언어별 구현)

Request를 하는 쪽에서 (ajax, axios)에서만 설정을 하는 것이 아니라, Response 하는 곳에서 특정한 설정을 함께 전달해야 SOP 정책을 피할 수 있음. 즉, 만약 웹서버를 flask로 구현했다면 request를 받는 flask에 해당 설정을 해줘야 하는 것.  

```
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

> CORS 설정을 해주면 모든 요청/응답 헤더에 CORS 지원 헤더 정보를 넣어서, CORS를 지원해줌
