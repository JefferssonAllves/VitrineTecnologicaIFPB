function openTab(evt, tabId) {
  const contents = document.querySelectorAll(".tab-content");
  contents.forEach((c) => c.classList.remove("active"));

  const links = document.querySelectorAll(".tab-link");
  links.forEach((l) => l.classList.remove("active"));

  document.getElementById(tabId).classList.add("active");
  evt.currentTarget.classList.add("active");
}
