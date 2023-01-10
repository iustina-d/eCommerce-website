//menu
const categories = document.querySelectorAll(".category")
categories.forEach((category) => {
  category.addEventListener("click", () => {
    if (category.classList.contains("open")) {
      category.classList.remove("open")
    } else {
      const categoryIsOpen = document.querySelectorAll(".category.open")
      categoryIsOpen.forEach((quest) => {
        quest.classList.remove("open")
      })
      category.classList.add("open")
    }
  })
})
