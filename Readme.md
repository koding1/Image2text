# Image2Text
### 이미지 OCR을 통한 텍스트 변환 및 Clipboard Copy

## 1. Example    

#### 영상에서 사용한 이미지     
<img src="/images/ex.jpg" width="50%" height="50%">

#### 영상     
<img src="/docs/ex.gif" width="100%" height="100%">    

## 2. Use

### for User
1. main.py 를 실행  
2. capture 버튼 클릭
3. 캡쳐 하고 싶은 영역의 시작점과 끝 점을 각각 클릭  (각 점으로 사격형을 만들어 범위만큼 캡쳐합니다.)
4. 클립보드에 복사된 text를 붙여넣기   

### for developer
캡쳐가 종료된 후 해당 영역에 대한 확인을 위해 1.8 초간 해당 영역을 보여줍니다. 이 시간을 변경하고 싶다면 ocr.py의     
    cv2.waitKey(1800) 
부분을 수정하십시오.      
다중 모니터, 특히 서브 모니터에 대한 기능은 제공하지 않고 있습니다.    
