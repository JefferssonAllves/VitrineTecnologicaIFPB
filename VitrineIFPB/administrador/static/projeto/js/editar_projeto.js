atualizarLabel(document.getElementById('nome_certificado'));

function modalExcluirProjeto(nome) {
  const delete_modal = document.getElementById("modal_delete_projeto");
  const delete_message = document.getElementById("delete_message_projeto");

  delete_message.innerHTML = `Tem certeza que deseja excluir a Projeto: <strong>${nome}</strong>? Esta ação não pode ser desfeita.`;

  console.log(delete_modal.style.display);

  if (delete_modal.style.display === "none") {
    delete_modal.style.display = "block";
  }else{
    delete_modal.style.display = "none";
  }

}