function mostrarModal() {
  modal = document.getElementById("modal_certificado");

  if (modal.style.display === "flex") {
    modal.style.display = "none";
  } else {
    modal.style.display = "flex";
  }
}
