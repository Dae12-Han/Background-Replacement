# Background-Replacement   

## Implementing one of difference-keying algorithms
PC 카메라 영상의 배경을 임의의 다른 배경으로 교체한다.

### 알고리즘 
OpenCV docs - How to use Background Subtraction Methods
https://docs.opencv.org/master/d1/dc5/tutorial_background_subtraction.html

Background Subtraction(BS) 알고리즘은 고정된 카메라에서 mask 영상을 생성하는 대표적인 알고리즘입니다.   
Background Subtraction(BS)의 기본 원리는 현재 프레임과 객체를 추출하기 위한 배경 모델의 차영상을 구하여 Thresholding을 하여 foreground mask를 구하는 것입니다. 
기본동작은 다음과 같습니다.   
①배경 초기화   
②배경 업데이트 (프레임 간 변화를 적용)   

![image](https://user-images.githubusercontent.com/72742199/120604813-60966f00-c488-11eb-84ca-23ee7b0e4d46.png)

### 코드
OpenCV에서 제공하는 Background Subtraction 알고리즘 중 하나인 BackgroundSubtractorMOG2를 사용하여 구현하였습니다.   
openCV 공식 github https://github.com/opencv/opencv
