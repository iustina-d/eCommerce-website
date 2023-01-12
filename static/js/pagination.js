const links = document.querySelectorAll(".link")
let general_url = "http://127.0.0.1:5000/"
let url = window.location.href

getLinksToActive()

function getLinksToActive() {
  page = 0
  if (url.toString() != general_url) {
    parameter = url.toString()
    number = parameter.substring(parameter.length - 1)
    page = parseInt(number, 10) - 1
    links[0].classList.remove("active")
  }
  links[page].classList.add("active")
}

function activeLink() {
  currentValue = event.target.value
  window.location = general_url + currentValue
}
function getPageNumber(value) {
  if (url.toString() == general_url) {
    currentPage = 2
  } else {
    parameter = url.toString()
    number = parameter.substring(parameter.length - 1)
    currentPage = parseInt(number, 10) + value
  }
  return currentPage
}
function Btn(value) {
  page = getPageNumber(value)
  if ((page >= 1 && value == -1) || (page <= 6 && value == 1)) {
    currentValue = page.toString()
    window.location = general_url + currentValue
  }
}

function Arr(value) {
  currentValue = value.toString()
  window.location = general_url + currentValue
}
