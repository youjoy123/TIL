*22.7.5 TIL(TODAY I LEARN)* 

## MARKDOWN 문법

### Heading

• Heading은 문서의 제목이나 소제목으로 사용 

• #의 개수에 따라 대응되는 수준(Heading level)이 있으며, h1 ~ h6까지 표현 가능 ::  `#` ~`######`  

• 문서의 구조를 위해 작성되며 글자 크기를 조절하기 위해 사용되어서는 안됨



### list

• List는 순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성

- 딸기
  - 당근수박
    - 참외메론



### Fenced Code block

 • 코드 블록은 backtick 기호 3개를 활용하여 작성(` ``` `) 

• 코드 블록에 특정 언어를 명시하면 Syntax Highlighting 적용 가능 

• 일부 환경에서는 적용이 되지 않을 수 있음

```python
print('hello')
# 주석
```

코드 블록에 특정 언어를 명시하면 Syntax highlighting 적용이 가능하다

```python
```python
```



### Inline code block

• 코드 블록은 backtick 기호 1개를 인라인에 활용하여 작성(``) 



### Link 

• `[문자열](URL)`을 통해 링크를 작성 가능, 특정 파일들 포함하여 연결 시킬 수도 있음



### image

`![문자열](URL)`

> - [마크다운 예시](./마크다운.md) `[마크다운 예시](./마크다운.md) `
> - [이미지폴더](./images) `[이미지폴더](./images)`



### 인용문 

> life is short, you need confidence. 인용문 무언가를 정의 할때 사용
>
> 꺽쇠를 사용 '>' 하여 인용문 구문을 작성한다.





### 표 Table

타이포라 기능을 적극활용하자.

본문 > 표 > 표삽입 (ctrl+t)

| 이름  | 컬러 |
| ----- | ---- |
| 이*훈 | 빨강 |
|       |      |
|       |      |



### TEXT 강조

**굵게** `**`

*기울게* `*`

***굵게기울게*** `***`



### 수평선

3개 이상의 `***`, `---`,`___`  

***

___

___



> ### 마크다운 관련 자료
>
> • GitHub Flavored Markdown (https://github.github.com/gfm/) 
> • Mastering Markdown (https://guides.github.com/features/mastering-markdown/) 
> • Markdown Guide (https://www.markdownguide.org/)
