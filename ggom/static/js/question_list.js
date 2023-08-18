document.addEventListener("DOMContentLoaded", function () {
  var button1 = document.getElementById("need_btn");
  var button2 = document.getElementById("solved_btn");

  button1.addEventListener("click", function () {
    if (button1.classList.contains("clicked_btn")) {
      button1.classList.remove("clicked_btn");
      button1.classList.add("need_btn");
      button2.classList.remove("need_btn");
      button2.classList.add("clicked_btn");
    } else {
      button1.classList.remove("need_btn");
      button1.classList.add("clicked_btn");
      button2.classList.remove("clicked_btn");
      button2.classList.add("need_btn");
    }
    // window.location.href = "https://"; // 원하는 URL로 변경
  });

  button2.addEventListener("click", function () {
    if (button2.classList.contains("clicked_btn")) {
      button2.classList.remove("clicked_btn");
      button2.classList.add("need_btn");
      button1.classList.remove("need_btn");
      button1.classList.add("clicked_btn");
    } else {
      button2.classList.remove("need_btn");
      button2.classList.add("clicked_btn");
      button1.classList.remove("clicked_btn");
      button1.classList.add("need_btn");
    }
    // window.location.href = "https://"; // 원하는 URL로 변경
  });
});
