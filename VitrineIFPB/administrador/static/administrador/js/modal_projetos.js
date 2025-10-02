function openEditModalProjeto(id, titulo, descricao, autores, categoria) {
  const edit_modal = document.getElementById("modal_edit_projeto");

  // Altera o valor dos inputs para os dados do Projeto
  document.getElementById("projeto_id").value = id;
  document.getElementById("projeto_titulo_edit").value = titulo;
  document.getElementById("projeto_descricao_edit").value = descricao;
  document.getElementById("projeto_autores_edit").value = autores;
  document.getElementById("projeto_categoria_edit").value = categoria;

  console.log(document.getElementById("projeto_autores_edit").value);
  edit_modal.style.display = "block";
}

function openDeleteModalProjeto(id, title) {
  const delete_modal = document.getElementById("modal_delete_projeto");
  const delete_message = document.getElementById("delete_message_projeto");

  // Altera o valor do input hidden para o id do Projeto
  document.getElementById("projeto_id_delete").value = id;

  delete_message.innerHTML = `Tem certeza que deseja excluir o Projeto: <strong>${title}</strong>? Esta ação não pode ser desfeita.`;
  delete_modal.style.display = "block";
}

function closeModal(modal_id) {
  const modal = document.getElementById(modal_id);
  modal.style.display = "none";
}
