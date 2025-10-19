function openEditModalCampus(id, nome) {
  const edit_modal = document.getElementById("modal_edit_campus");

  // Altera o valor dos inputs para os dados do Campus
  document.getElementById("campus_id_edit").value = id;
  document.getElementById("campus_nome_edit").value = nome;

  edit_modal.style.display = "block";
}

function openDeleteModalCampus(id, nome) {
  const delete_modal = document.getElementById("modal_delete_campus");
  const delete_message = document.getElementById("delete_message_campus");

  // Altera o valor do input hidden para o id do Campus
  document.getElementById("campus_id_delete").value = id;

  delete_message.innerHTML = `Tem certeza que deseja excluir o Campus: <strong>${nome}</strong>? Esta ação não pode ser desfeita.`;
  delete_modal.style.display = "block";
}
