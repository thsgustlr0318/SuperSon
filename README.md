# SuperSon
산학연계SW프로젝트 슈퍼손팀 Openpose를 이용한 체력측정 자동화

## Prerequisites

Openpose
https://github.com/CMU-Perceptual-Computing-Lab/openpose

mjpg-streamer
https://github.com/jacksonliam/mjpg-streamer

## 사용법

Openpose가 설치, 운용이 가능한 PC에 openpose를 설치하고, openpose 디렉토리에 server의 내용물인 superson.py와 png 파일들을 배치

client로 라즈베리파이를 사용하여, 라즈베리파이에 카메라 모듈을 연결하고, mjpg-streamer를 설치하고, sh mjpg.sh를 통해 mjpg-streamer를 실행할 수 있도록 mjpg.sh파일 생성 후 client의 내용물인 client.py와 voice 디렉토리를 배치

superson.py의 43번 줄에 해당 PC의 IP를 입력하고 python3 superson.py 실행

argument로 

source : 영상의 source

w : width( default : 720)

h : height( default : 480)

timer : 운동 타이머( default : 60)

를 부여할 수 있으며 영상의 source 인자는 필수로 입력

ex) python3 superson.py --source ./test_video, python3 superson.py --source http://192.168.10.20:8091/?action=stream

client.py의 33번 줄에도 server의 IP를 입력하고 python3 client.py 실행

프로그램 실행 후 키보드 1,2 입력을 통해 팔굽혀펴기와 윗몸 일으키기 종목 선택

출력되는 문구를 통해 카메라 각도 조절 후 Ready가 되면 s 입력을 통해 시작, q를 통해 종료
