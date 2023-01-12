const card_number = document.querySelector(".number")
let number = ""
const name_user = document.querySelector(".inputname")
const expire_date = document.querySelector(".expire")
const security_number = document.querySelector(".ccv")



card_number.addEventListener("mouseout", () => {
  number = card_number.value
  document.querySelector(".card_number").innerHTML = number
})

name_user.addEventListener("mouseout", () => {
  admin = name_user.value
  document.querySelector(".fullname").innerHTML = admin
})
expire_date.addEventListener("mouseout", () => {
  dateEX = expire_date.value
  document.querySelector(".date_value").innerHTML = dateEX
})
security_number.addEventListener("mouseout", () => {
  numberSe = security_number.value
  document.querySelector(".fullname").innerHTML = numberSe
})
