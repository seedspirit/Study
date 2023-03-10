#### 기본 용어
네트워크
- 종단 시스템 (end system): 컴퓨터나 스마트폰과 같은 네트워크 송수신의 주체
- 프로토콜 (protocol): 두 이종 시스템을 연결하기 위한 규약, 약속

인터넷
- 회사 혹은 소규모의 네트워크에서 전세계 네트워크와 연결된 상태 - 연결연결이 모여 인터넷이 되는 것
	- 웹 통신은 주로 HTTP 프로토콜을 사용
- 종단 시스템은 보통 ISP(Internet Service Provider)


TCP/IP
- OSI 7계층이 나오기 전부터 사용되었던 표준 모델

OSI 7 Layer
- 통신을 위한 약속을 상세하게 기술한 모델, 7개의 계층으로 역할을 나눔
- 각 계층별로 역할이 있으며, 이를 통해 프로토콜을 만족
- TCP/IP와 마찬가지로 각 계층별로 역할이 나뉘어져 있음

IP Address
- 통신 자료를 최종적으로 전달하기 위해 필요한 송/수신 위치 정보

Packet Switching
- 인터넷을 위해서 정보를 주고받는 작은 단위가 패킷(Packet)
- 이 패킷을 네트워크 송수신의 주체끼리 주고 받을 때, 일정한 순서없이 보내지며 어떤 경로를 통해 이동되는지는 네트워크의 상황에 따라 다름


#### 통신을 위한 기본 동작
아래의 기본 동작을 바탕으로 프로토콜을 설계함
- 요청 (Request): 서비스 혹은 정보를 요청함
- 인지 (Indicate): 수신하는 주체가 작업 요청을 확인
- 응답 (Response): 수식하는 주체가 요청받은 작업에 대해서 적절히 응답함
- 확인 (Confirm): 요청한 주체가 응답 데이터를 최종적으로 확인함


#### 네트워크의 유형
- LAN (Local Area Network) : 지역 네트워크. 소규모 사이즈로 묶임 (집, 오피스 등)
- WAN (Wide Area Network) : 원거리 통신망으로 넓게 범위를 지님 (국가 등)
- LAN끼리 또 WAN으로 엮고, 이 WAN이 모여 인터넷이 됨
- 네트워크 토폴로지: 이 네트워크의 구성을 어떤 방식으로 할 것인지
	- Star, Mesh, Bus, Ring 등등
