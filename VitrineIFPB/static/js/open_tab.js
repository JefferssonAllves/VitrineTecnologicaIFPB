function openTab(evt, tabId) {
  // Esconde todos os conteúdos de abas
  const allContents = document.querySelectorAll(
    ".tab-content, .admin-tab-content"
  );
  allContents.forEach((content) => {
    content.classList.remove("active");
  });

  // Desativa todos os botões de abas
  const allButtons = document.querySelectorAll(".tab-link, .admin-tab-button");
  allButtons.forEach((button) => {
    button.classList.remove("active");
  });

  // Mostra o conteúdo da aba selecionada
  const selectedContent = document.getElementById(tabId);
  if (selectedContent) {
    selectedContent.classList.add("active");
  }

  // Ativa o botão que foi clicado
  if (evt && evt.currentTarget) {
    evt.currentTarget.classList.add("active");
  }
}
