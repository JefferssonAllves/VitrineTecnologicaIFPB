
function closeModal(modal) {
  document.getElementById(modal).style.display = "none";
}


url = window.location.href.split('/').filter(string => string !== "");
url = url[url.length - 1];
document.getElementById(url).classList.add("active");
