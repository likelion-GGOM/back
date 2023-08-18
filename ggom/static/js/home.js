/*
  div사이즈 동적으로 구하기
*/
const outer = document.querySelector(".outer");
const innerList = document.querySelector(".inner-list");
const inners = document.querySelectorAll(".inner");
let currentIndex = 0; // 현재 슬라이드 화면 인덱스

inners.forEach((inner) => {
  inner.style.width = `${outer.clientWidth}px`; // inner의 width를 모두 outer의 width로 만들기
});

innerList.style.width = `${outer.clientWidth * inners.length}px`; // innerList의 width를 inner의 width * inner의 개수로 만들기

/*
  버튼에 이벤트 등록하기
*/
const buttonLeft = document.querySelector(".left-button-list i");
const buttonRight = document.querySelector(".right-button-list i");

buttonLeft.addEventListener("click", () => {
  currentIndex--;
  currentIndex = currentIndex < 0 ? 0 : currentIndex; // index값이 0보다 작아질 경우 0으로 변경
  innerList.style.marginLeft = `-${outer.clientWidth * currentIndex}px`; // index만큼 margin을 주어 옆으로 밀기
});

buttonRight.addEventListener("click", () => {
  currentIndex++;
  currentIndex =
    currentIndex >= inners.length ? inners.length - 1 : currentIndex; // index값이 inner의 총 개수보다 많아질 경우 마지막 인덱스값으로 변경
  innerList.style.marginLeft = `-${outer.clientWidth * currentIndex}px`; // index만큼 margin을 주어 옆으로 밀기
});

// 슬라이드 위치 동그라미
// JavaScript 코드
const slides = document.querySelectorAll(".inner"); // 각 슬라이드 요소
const indicators = document.querySelectorAll(".slide-index span"); // 동그라미 인덱스

// 현재 활성화된 슬라이드의 인덱스를 추적하는 변수
let currentSlideIndex = 0;

// 슬라이드 변경 함수
function changeSlide(index) {
  slides.forEach((slide, i) => {
    slide.style.transform = `translateX($-{index * 100}%)`; // 슬라이드 이동
  });

  indicators.forEach((indicator, i) => {
    indicator.classList.remove("active"); // 모든 동그라미 클래스 제거
  });

  indicators[index].classList.add("active"); // 선택된 슬라이드의 동그라미에 클래스 추가
}

// 슬라이드 오른쪽 버튼 클릭 시
document.querySelector(".right-button-list").addEventListener("click", () => {
  currentSlideIndex = (currentSlideIndex + 1) % slides.length;

  changeSlide(currentSlideIndex);
});

// 슬라이드 왼쪽 버튼 클릭 시
document.querySelector(".left-button-list").addEventListener("click", () => {
  currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
  changeSlide(currentSlideIndex);
});

changeSlide(currentSlideIndex);
