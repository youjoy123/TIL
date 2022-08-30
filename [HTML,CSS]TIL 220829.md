# HTML 기본 구조

```html
<!-- HTML 기본 골격 -->
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Document</title>
  </head>
  <body>
  </body>
</html>
```

1. `<html></html>`
   
   - 페이지 전체의 컨텐츠를 감싸는 요소
   - 문서의 최상위(root) 요소

2. `<head></head>`
   
   - 문서 메타데이터 요소
   - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
   - 일반적으로 브라우저에 나타나지 않는 내용

3. `<body></body>`
   
   - 실제 화면 구성과 관련된 내용

# 요소와 속성

> 요소 (element)

- HTML의 요소는 시작 태그, 종료 태크, 내용(content)으로 구성
  - 요소는 태그로 내용을 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음)
    - br, hr, img, input, link, meta 등
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야 함
    - 이유: 오류를 반환하는 것이 아닌 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음
- 인라인 레벨 요소 vs 블록 레벨 요소
- 텍스트 요소: a, b, i, br, img, span 등
- 그룹 요소: p, hr, ol, ul, pre, div, blockquote 등

> 속성 (attribute)

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 속성 지정 스타일 가이드
  - 등호 좌우에 공백은 없어야 함
  - 속성값 작성 시 쌍따옴표 사용
- 태그별로 사용할 수 있는 속성은 다름
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

> HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (일부 요소에는 아무 효과가 없을 수 있음)
1. `id`: 문서 전체에서 유일한 고유 식별자 지정

2. `class`: 공백으로 구분된 해당 요소의 클래스 목록
   
   - CSS, JS에서 요소를 선택하거나 접근하기 위해 사용됨

3. `style`: inline 스타일 지정

4. `data-*`: 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용

5. `title`: 요소에 대한 추가 정보 지정

6. `tabindex`: 요소의 탭 순서

# DOM(Document Object Model) 트리

> 렌더링 (Rendering)

- 텍스트로 작성된 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

> DOM 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
- HTML 문서에 대한 모델을 구성함
- HTML 문서 내의 각 요소에 접근/수정하는데 필요한 프로퍼티와 메서드를 제공함

# 



# body 태그

> `<body></body>` 태그 기본 구조

```html
<!-- body 태그 구조-->
<body>
  <h1>나의 첫번째 HTML</h1>
  <p>이것은 본문입니다.</p>
  <span>이것은 인라인요소</span>
  <a href="https://www.naver.com">네이버로 이동!!</a>
</body>
```

> 블록 레벨 요소 vs 인라인 레벨 요소

1. 블록 레벨 요소
   - h, p, hr, ul, ol, dl, blockquote, pre, div 등
2. 인라인 레벨 요소
   - br, b, strong, i, em, a, img, span 등

> body 태그 내 태그들 종류

- [텍스트 관련 태그](#-텍스트-관련-태그): h, p, hr, br, b, strong, i, em, blockquote, pre
- [목록 관련 태그](#-목록-관련-태그): ul, ol, dl
- [이미지 관련 태그](#-이미지-관련-태그): img
- [하이퍼링크 관련 태그](#-하이퍼링크-관련-태그): a
- [컨테이너 관련 태그](#-컨테이너-관련-태그): div, span

# 텍스트 관련 태그

> `<h></h>` 태그

- 제목 요소

- h1부터 h6까지 존재해 구조화된 계층 표현 가능
  
  ```html
  <body>
    <h1>The Crushing Bore</h1>
    <h2>Chapter 1: The dark night</h2>
    <h2>Chapter 2: The eternal silence</h2>
    <h3>The specter speaks</h3>
  </body>
  ```

> `<p></p>` 태그

- 텍스트 단락 요소 (paragraph)
  
  ```html
  <body>
    <p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>
  </body>
  ```

> `<hr>` 태그

- 문단 레벨 요소에서의 주제의 분리를 의미하며, 수평선으로 표현됨 (A Horizontal Rule)

```html
<body>
  <p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>
  <hr>
  <p>Our protagonist could not so much as a whisper out of the shadowy figure ...</p>
</body>
```

> `<br>` 태그

- 텍스트 내에 줄 바꿈 생성
  
  ```html
  <body>
    <p>It was a dark night. Somewhere, an owl hooted.<br>The rain lashed down on the ...</p>
  </body>
  ```

> `<b></b>` & `<strong></strong>` 태그

1. `<b></b>`
   
   - 굵은 글씨 요소
   - 의미가 있는 것이 아닌 표현에만 영향을 주는 요소

2. `<strong></strong>`
   
   - 중요한 텍스트를 **강조**하고자 하는 요소 
   - 브라우저에서는 기본적으로 굵은 텍스트로 스타일을 지정
   - 화면판독기에 인식되면 다른 톤의 목소리로 표현
   
   ```html
   <body>
     <p><b>Insert</b> a tomato slice and a leaf of lettuce between the slices of bread.</b>
     <p>I am counting on you. <strong>Do not</strong> be late!</p>
   </body>
   ```

> `<i></i>` & `<em></em>` 태그

1. `<i></i>`
   
   - 기울임 글씨 요소
   - 의미가 있는 것이 아닌 표현에만 영향을 주는 요소

2. `<em></em>`
   
   - 중요한 텍스트를 **강조**하고자 하는 요소
   - 브라우저에서는 기본적으로 이탤릭체로 스타일을 지정
   - 화면판독기에 인식되면 다른 톤의 목소리로 표현
   
   ```html
   <body>
     <p>The menu was a sea of exotic words like 
       <i lang="uk-latn">vatrushka</i> and <i lang="fr">soupe à l'oignon</i>.
     </p>
     <p>I am <em>glad</em> you weren't <em>late</em>.</p>
   </body>
   ```

> `<blockquote></blockquote>` 태그

- 인용구 표시 요소

- 브라우저 기본 스타일은 인용구를 표현할 때, 들여쓰기 된 단락으로 나타냄

- 속성
  
  - `cite`: 출처를 표기
    
    ```html
    <body>
      <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
        <p>The HTML Element indicates that the enclosed text is an extended quotation.</p>
      </blockquote>
    </body>
    ```

> `<pre></pre>` 태그

- 코드 블록 요소

- HTML에 작성한 내용을 그대로 표현해줌
  
  - 보통 고정폭 글꼴이 사용되고 공백문자를 유지해줌

- `<code></code>`: 일반적인 컴퓨터 코드를 표시
  
  ```html
  <body>
    <pre>
       택스트 내에서 들여 쓰기 또는 초과 공백을 사용하면 브라우저가 이를 무시하고 렌더링 된 페이지에 공백을 표시하지 않습니다.
       하지만 pre 태그로 텍스트를 감싸면 공백이 텍스트 편집기에서 보는 것과 동일하게 렌더링 됩니다.
       <code>
         var para = document.querySelector('p');
  
         para.onclick = function() {
           alert('Owww, stop poking me!');
         }
       </code>
    </pre>
  </body>
  ```

# 목록 관련 태그

> `<ul></ul>` 태그

- 순서가 없는 리스트 (unordered list)
  
  ```html
  <body>
    <ul>
      <li>milk</li>
      <li>eggs</li>
    </ul>
  </body>
  ```

> `<ol></ol>` 태그

- 순서가 있는 리스트 (ordered list)
  
  ```html
  <body>
    <ol>
      <li>milk</li>
      <li>eggs</li>
    </ol>
  </body>
  ```

> `<dl></dl>` 태그

- Description lists로서 용어 및 정의, 질문 및 답변과 같은 일련의 항목 및 관련 설명을 표시할 때 사용

- `<dt></dt>`: 용어, 질문과 같은 상위 항목을 나타내는 요소 (description term)

- `<dd></dd>`: 정의, 답변과 같은 하위 항목을 나타내는 요소 (description definition)
  
  ```html
  <body>
    <dl>
       <dt>HTML</dt>
       <dd>HTML은 웹 페이지 표시를 위해 개발된 지배적인 마크업 언어다.</dd>
       <dt>CSS</dt>
       <dd>CSS는 마크업 언어가 실제 표시되는 방법을 기술하는 style sheet language다.</dd>
    </dl>
  </body>
  ```

# 이미지 관련 태그

> `<img>` 태그

- 이미지 삽입 요소

- 속성
  
  - `src`: 이미지 경로 지정 (필수)
  
  - `alt`: 대체 텍스트
    
    - 스크린 리더가 텍스트를 읽어 사용자에게 이미지 설명
    - 네트워크 오류, 콘텐츠 차단, 죽은 링크 등 이미지를 표시할 수 없는 경우 텍스트로 표시
    
    ```html
    <body>
      <img src="favicon144.png" alt="MDN logo">
    </body>
    ```

# 하이퍼링크 관련 태그

> `<a></a>` 태그

- href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성

- 속성
  
  - `href`: 사이트의 주소가 포함된 링크
  
  - `title`: 링크에 대한 보충 정보로서, 링크에 마우스를 올렸을 때 정보가 나타남
  
  ```html
  <body>
    <a href="https://www.mozilla.org/en-US/"
      title="The best place to find more information about Mozilla's
        mission and how to contribute">the Mozilla homepage</a>
  </body>
  ```

- 문서 상단이 아닌 HTML 문서 내부의 특정 부분(Document fragments)에 링크 가능
  
  - 이를 위해, 우선 링크를 시키고 싶은 태그에 id 속성을 넣어 주어야함
  
  - 특정 id를 가진 태그에 연결하려면 URL 끝에 해시/파운드 기호를 포함하면 됨
    
    ```html
    <!-- contacts.html 파일 -->
    <body>
      <h2 id="Mailing_address">Mailing address</h2>
    </body>
    
    <!-- main.html 파일 -->
    <body>
      <p>Want to write us a letter? Use our <a href="contacts.html#Mailing_address">mailing address</a>.</p>
    </body>
    ```

# 



# 컨테이너 관련 태그

> `<div></div>` 태그

- 의미 없는 블록 레벨 컨테이너

- CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음

- 요소 여럿을 묶어 class나 id 속성으로 꾸미기 쉽도록 도움

- 문서의 특정 구역이 다른 언어임을 표시(lang 속성)하는 용도로 사용
  
  ```html
  <body>
     <div class="shadowbox">
        <p>Here's a very interesting note displayed in a lovely shadowed box.</p>
     </div>
  </body>
  ```

> `<span></span>` 태그

- 의미 없는 인라인 컨테이너

- CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음

- class나 id 속성으로 꾸미기 쉽도록 도움

- 문서의 특정 구역이 다른 언어임을 표시(lang 속성)하는 용도로 사용
  
  ```html
  <body>
     <p><span>Some text</span></p>
  </body>
  ```

# html 태그

> `<html></html>` 태그 기본 구조

```html
<!-- html 태그 구조 -->
<html lang="en">
</html>
```

- 문서의 기본 언어 설정 (한국어의 경우, lang="ko")

# head 태그

> `<head></head>` 태그 기본 구조

```html
<!-- head 태그 구조 -->
<head>
  <title>HTML 학습</title>
  <meta charset="UTF-8">
  <link href="style.css" rel="stylesheet">
  <script src="javascript.js"></script>
  <style>
    p {
    color: black;
    }
  </style>
</head>
```

> `<title></title>` 태그

- HTML문서 전체의 타이틀

- 브라우저 상단 탭의 타이틀
  
  ```html
  <head>
    <title>HTML 학습</title>
  </head>
  ```

> `<meta>` 태그

- 문서 레벨 메타데이터 요소
  
  - 문서의 인코딩(character set) 특정
  - 저자(name)와 설명(content) 추가

- Open Graph Data
  
  - 메타 데이터를 표현하는 새로운 규약
  - Facebook이 웹 사이트에 더 풍부한 메타 데이터를 제공하기 위해 발명한 메타 데이터 프로토콜
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
  - 참고자료: [Open Graph Data](https://ogp.me/)
  
  ```html
  <head>
    <meta charset="UTF-8">
    <meta name="author" content="HJ Yun">
    <meta name="description" content="I learned HTML">
    <meta property="og:title" content="The Rock" />
    <meta property="og:type" content="video.movie" />
    <meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
    <meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
  </head>
  ```
  
    ![Open Graph Data을 설명하는 이미지](https://miro.medium.com/max/1400/1*PHdFEeCVNiPYUFC3IX45MA.png)

> `<link>` 태그

- 외부 리소스 (CSS 파일, favicon 등) 연결 요소
  
  ```html
  <head>
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  </head>
  ```

> `<script></script>` 태그

- 스크립트 요소 (JavaScript 파일/코드)
  
  ```html
  <head>
    <script src="javascript.js"></script>
  </head>
  ```

> `<style></style>` 태그

- CSS 직접 작성
  
  ```html
  <head>
    <style>
     p {
     color: black;
     }
    </style>
  </head>
  ```







# CSS

> CSS 기본 구조

![CSS 기본 구조](https://poiemaweb.com/img/css-syntax.png)

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 (Property): 어떤 스타일 기능을 변경할지 결정
  - 값 (Value): 어떻게 스타일 기능을 변경할지 결정

> CSS 정의 방법

1. 인라인(inline) CSS 정의 
   
   ```html
   <body>
      <h1 style="color: blue; font-size: 100px;">Hello</h1>
   </body>
   ```

2. 내부(embedding) CSS 정의
   
   - `<style></style>` 태그 이용
   
   ```html
   <head>
      <style>
        h1 {
          color: black;
          font-size: 100px;
        }
      </style>
   </head>
   ```

3. 외부(link) CSS 정의
   
   - 분리된 CSS 파일의 링크를 연결
   
   ```css
   /* style.css 파일 */
   h1 {
      color: black;
      font-size: 100px;
   }
   ```
   
   ```html
   <!-- main.html 파일 -->
   <head>
      <link href="style.css" rel="stylesheet">
   </head>
   ```

# CSS 기초 선택자

> 요소 선택자

- HTML 태그를 직접 선택

- 기본형
  
  ```css
  태그명 {
    스타일 규칙
  }
  ```

- 예
  
  ```css
  p {
    font-style: italic;
  }
  ```

> 클래스 (class) 선택자  

- `.`문자로 시작하며, 해당 클래스가 적용된 항목을 선택

- 기본형
  
  ```css
  .클래스명 {
    스타일 규칙
  }
  ```

- 예
  
  ```css
  .accent {
    border: 1px solid #000;
  }
  ```

> 아이디 (id) 선택자

- `#`문자로 시작하며, 해당 아이디가 적용된 항목을 선택

- 일반적으로 하나의 문서에 1번만 사용

- 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

- 기본형
  
  ```css
  #아이디명 {
    스타일 규칙
  }
  ```

- 예
  
  ```css
  #container {
    width: 500px;
  }
  ```
