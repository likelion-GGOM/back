// 1. <div class="pass-field"> 안에 있는 <input>가져오기
const passwordInput = document.querySelector(".password_text input");
// 2. <div class="pass-field"> 안에 있는 <i>가져오기
const eyeIcon = document.querySelector(".password_text i");
// 3. <ul class="requirement-list"> 안에 있는 <li> 전체 가져오기
const requirementList = document.querySelectorAll(".require_list li");

// 요구 사항 목록을 정규식(regex)에 저장
const requirements = [
  { regex: /.{8,}/, index: 0 }, // 최소 8글자
  { regex: /\d/, index: 1 }, // 4. 숫자 최소 1개 이상 포함
  { regex: /[a-z]/, index: 2 }, // 5. 영어 소문자 최소 1개 이상 포함
  //{ regex: /[@,#,$...]/, index: 3 }, // 6. 특수문자 최소 1개 이상 포함 (@,#,$...)
  { regex: /[A-Z]/, index: 3 }, // 7. 영어 대문자 최소 1개 이상 포함
];

// addEventListener: 특정요소의 이벤트를 등록할때 사용
// keyup: 키를 눌렀다가 떼는 순간 발생한다.
passwordInput.addEventListener("keyup", (e) => {
  requirements.forEach((item) => {
    // 8. 암호가 요구 사항 정규식과 일치하는지 확인, 일치할시 isValid에 true가 저장
    const isValid = item.regex.test(passwordInput.value);

    // 9. HTML에서 요구사항(li)을 requirementItem에 저장
    const requirementItem = requirementList[item.index];

    if (isValid) {
      // 일치 했을때 valid를 넣어 연하게 만들어줌
      requirementItem.classList.add("valid");
      // 10. <ul class="requirement-list"> 안에 있는 <li>의 첫번째 요소 <i>의 클래스를 fa-solid fa-check로 바꿔주기
      requirementItem.querySelector("i").className = "fa-solid fa-check";
    } else {
      // 일치하지 않았을때
      requirementItem.classList.remove("valid");
      // 11. <ul class="requirement-list"> 안에 있는 <li>의 첫번째 요소 <i>의 클래스를 fa-solid fa-circle로 바꿔주기
      requirementItem.querySelector("i").className = "fa-solid fa-x";
    }
  });
});

// 눈 아이콘 클릭 시
eyeIcon.addEventListener("click", () => {
  // 12. passwordInput의 type이 password면 text로 type을 변환한다. (text일때는 반대로)
  passwordInput.type = passwordInput.type === "password" ? "text" : "password";
  // 비밀번호 입력 유형에 따라 눈 아이콘  업데이트 -> -slash가 붙도록
  eyeIcon.className = `fa-solid fa-eye${
    passwordInput.type === "password" ? "" : "-slash"
  }`;
});
