function exibirResultados(data) {
  const corpoTabela = document.getElementById("corpo-tabela");
  campus = data.campus;

  corpoTabela.innerHTML = "";

  // Adicionar novos resultados
  campus.forEach(campi => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td data-label="id">${campi.id}</td>
      <td data-label="nome">${campi.nome}</td>
      <td data-label="projetos">${campi.quantidade_projetos}</td>
      <td data-label="Ações" class="admin-actions">
        <button class="btn primary"onclick="openEditModalcampi('${ campi.id }', '${ campi.nome}')">Editar</button>
        <button class="btn danger"onclick="openDeleteModalcampi('${ campi.id }', '${ campi.nome}')">Excluir</button>
      </td>
    `;
    corpoTabela.appendChild(row);
  });
}

function modalAdicionarCampus(){
  const content = document.getElementById("admin-content-wrapper");
  const modal = document.getElementById("adicionar-campus");
  if (modal.style.display === "flex") {
    modal.style.display = "none";
    content.style.height = 450 + "px";
  }else{
    modal.style.display = "flex";
    content.style.height = 620 + "px";

  }
}

function modalEditCampus(id, nome){
  modal = document.getElementById("modal_edit_campus");

  if(modal.style.display === "flex"){
    modal.style.display = "none";
  }else{
    modal.style.display = "flex";
    document.getElementById("campus_id_edit").value = id;
    document.getElementById("campus_nome_edit").value = nome;
  }
}

function modalDeleteCampus(id, nome){
  modal = document.getElementById("modal_delete_campus");

  if(modal.style.display === "flex"){
    modal.style.display = "none";
  }else{
    modal.style.display = "flex";
    document.getElementById("campus_id_delete").value = id;
    document.getElementById("campus_nome_delete").value = nome;
  }
}
