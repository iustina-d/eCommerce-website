var number = 0;
const buttons = document.querySelectorAll(".badge_message")

buttons.forEach(button => {
  button.addEventListener("click", function() {
    number ++;
    console.log(number);
    document.querySelector(".badge").innerHTML = number;
  });
});
