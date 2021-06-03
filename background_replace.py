import cv2 as cv #cv2 모듈 불러오기
import numpy as np #numpy 모듈 불러오기

## [create]
#배경 제거 객체 생성 함수
#history:히스토리 개수, varThreshold:분산 임계 값/detectShadows:그림자 표시
backSub = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=500, detectShadows=0)

## [video] 
## 불러오기
video = cv.VideoCapture(0)
oceanVideo = cv.VideoCapture("city.mp4")

takeBgImage = 0
ret, bgReference = video.read()

if not video.isOpened():
    print('Unable to open!')
    exit(0)

while True:
    ret, frame = video.read()
    ret2, bg = oceanVideo.read()

    if frame is None:
        break

    ## [apply]
    #background model 업데이트
    fgMask = backSub.apply(frame)

    ## [show]
    #webcam 영상과, mask 영상 보여주기
    cv.imshow('WebCam', frame)
    cv.imshow('FG Mask', fgMask)

    # Inverting the mask
    fgMask_inv = cv.bitwise_not(fgMask)

    #mask를 사용하여 foreground와 background 정보 가져오기
    #bitwise_and(비트연산)=> 두 값 중 하나라도 false이면 false
    fgImage = cv.bitwise_and(frame, frame, mask=fgMask)
    fgImage=np.array(fgImage)
    
    #bg를 frame의 array와 맞춰줘야하므로 (int(frame.shape[1]),int(frame.shape[0])) 사용
    bg = cv.resize(bg,(int(frame.shape[1]),int(frame.shape[0])),interpolation = cv.INTER_AREA)
    #bitwise_and(비트연산)=> 두 값 중 하나라도 false이면 false
    bgImage = cv.bitwise_and(bg, bg, mask=fgMask_inv)
    bgImage=np.array(bgImage)

    #bgImage와 fgImage를 더해 새로운 이미지 생성
    bgSub = cv.add(bgImage,fgImage)
    #배경합성 영상 보여주기
    cv.imshow('Background Removed', bgSub)

    #키보드 'q'를 누르면 종료
    keyboard = cv.waitKey(5) & 0xFF
    if ord('q') == keyboard:
        break

cv.destroyAllWindows()
video.release()