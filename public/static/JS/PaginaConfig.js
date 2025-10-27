// Controle das abas
const tabButtons = document.querySelectorAll(".tab-button");
const tabContents = document.querySelectorAll(".tab-content");

tabButtons.forEach(button => {
  button.addEventListener("click", () => {
    tabButtons.forEach(btn => btn.classList.remove("active"));
    tabContents.forEach(tab => tab.classList.remove("active"));

    button.classList.add("active");
    document.getElementById(button.dataset.tab).classList.add("active");
  });
});

// Controle dos botões de toggle
const toggles = document.querySelectorAll(".toggle-group .toggle");
toggles.forEach(toggle => {
  toggle.addEventListener("click", () => {
    const group = toggle.parentNode.querySelectorAll(".toggle");
    group.forEach(btn => btn.classList.remove("active"));
    toggle.classList.add("active");
  });
});

// Escolher personagem
const icons = document.querySelectorAll(".icon img");
const avatarImg = document.querySelector(".avatar-img img");

icons.forEach(icon => {
  icon.addEventListener("click", () => {
    const newSrc = icon.getAttribute("src");
    avatarImg.setAttribute("src", newSrc);
  });
});
