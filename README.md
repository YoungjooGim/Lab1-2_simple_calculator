# Smart_Textbook_(by-using-tkinter)
## SSU_AI융합학부_오픈소스기초설계_LAB1

***
### "윤성우의 열혈파이썬 기초편"책을 바탕으로 만든 스마트 교과서 GUI 소프트웨어 betaversion입니다.
***
>  <img width="364" alt="smart교과서_열혈파이썬기초편" src="https://user-images.githubusercontent.com/89295180/139580830-34ed64d5-fac1-48bf-a993-a6ad9fdf7ed8.PNG">
>  >tkinter를 이용하여 만들었습니다.

#### Frame 단위로 영역을 나누어 설계하였습니다.
***
* 타이틀 FRAME 
  + 교재이미지 라벨
 
* 교재 챕터 및 연습문제 이동 FRAME
  + 챕터와 연습문제 리스트는 각각 콤보 박스로 구현
  + 다음 버튼: command = 해당 챕터 연습문제만 다음 콤보 박스에 표시
  + 문제풀이시작 버튼: command = 해당 연습문제 notebook로 연습문제 frame 변경
 
 
* 연습문제 FRAME
  + tkinter.ttk에서 제공하는 “notebook class”로 구현함으로써 이용자가 원하는 문제와 해설에 쉽게 접근할 수 있도록 설계
  + 정답보기 버튼: command = 정답 라벨에 표시 + 터미널창에 출력

