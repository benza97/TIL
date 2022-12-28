 # 마크다운 문법 정리
 
 ## 제목 2
 ### 제목 3

 
 **글씨체 강조**
 
 *글씨체 강조*

 > 인용문

 1. 분류
 2. 분류
 3. 분류

 - 분류
 - 분류
 - 분류

 `python` 

 - 밑줄
 ---
 - 링크  [구글](https://www.google.com/)
 
![보노보노](bn14.jpg)
- 이미지


 ```
  "firstName":"jun young"
  "lastName": "kim"
  "age": 26
```

``` python
print(hello world)
```


# CLI 문법

`ls` : 목록 list

`mkdir` : 디렉토리 생성 make directory

`cd`: 디렉토리 이동 `change directory`

`.` : 현재 디렉토리 ..: 상위 디렉토리

`touch` : 새로운 파일을 생성

`rm` : 삭제 `remove` 폴더 삭제 시 `rm -r`

## *ctrl+s (저장) 습관적으로 사용하기*

---

# git bash 개념이해

 working tree (1통)
 -> `git add` 입력


 staging area  (2통)
 -> `git commit -m` 입력 (3통)
 

 working tree, staging area (1,2통) -> `git status`
 commit -m (3통) -> `git log`

 ---



# 원격저장소 정리
##  저장소 처음 만들때 
- `git init`

## 버전 기록할 때
- `git add`
- `git commit -m`

## 상태 확인할 때
- `git status` 1통,2통
- `git log`  커밋 확인
---

# 원격 저장소 활용하기
## 처음 연결할 때
- `git remote add origin URL`

## 보내기/받기
- `git push origin master` 보내기
- `git pull origin master` 받기

## 원격 프로젝트 참여할 때
- `git clone url`

## 원격 저장소 삭제
- `git remote rm`

## 원격 저장소 정보확인
- `git remote -v`

---

# 용어 
## 브랜치 `master,main`
## 원격저장소 `origin`

---

# 협업과정 그림 자료


![협업과정](%ED%98%91%EC%97%85%EA%B3%BC%EC%A0%95.png)


---

# 유용한 홈페이지

# [gitignore](https://www.toptal.com/developers/gitignore) 
# [git 입문](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)
# [git 완벽정리](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-%EB%B2%84%EC%A0%84-%EA%B4%80%EB%A6%AC%EB%9E%80%3F)






