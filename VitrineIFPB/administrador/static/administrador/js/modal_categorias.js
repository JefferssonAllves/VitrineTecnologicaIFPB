function openEditModalCategoria(id, nome) {
  const edit_modal = document.getElementById("modal_edit_categoria");

  // Altera o valor dos inputs para os dados da Categoria
  document.getElementById("categoria_id_edit").value = id;
  document.getElementById("categoria_nome_edit").value = nome;

  edit_modal.style.display = "block";
}

function openDeleteModalCategoria(id, nome) {
  const delete_modal = document.getElementById("modal_delete_categoria");
  const delete_message = document.getElementById("delete_message_categoria");

  // Altera o valor do input hidden para o id da Categoria
  document.getElementById("categoria_id_delete").value = id;

  delete_message.innerHTML = `Tem certeza que deseja excluir a Categoria: <strong>${nome}</strong>? Esta ação não pode ser desfeita.`;
  delete_modal.style.display = "block";
}
