function exibirResultados(data) {
  const corpoTabela = document.getElementById("corpo-tabela");
  categorias = data.categorias;

  corpoTabela.innerHTML = "";

  // Adicionar novos resultados
  categorias.forEach(categoria => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td data-label="id">${categoria.id}</td>
      <td data-label="nome">${categoria.nome}</td>
      <td data-label="projetos">${categoria.quantidade_projetos}</td>
      <td data-label="Ações" class="admin-actions">
        <button class="btn primary"onclick="openEditModalCategoria('${ categoria.id }', '${ categoria.nome}')">Editar</button>
        <button class="btn danger"onclick="openDeleteModalCategoria('${ categoria.id }', '${ categoria.nome}')">Excluir</button>
      </td>
    `;
    corpoTabela.appendChild(row);
  });
}

function modalAdicionarCategoria(){
  const content = document.getElementById("admin-content-wrapper");
  const modal = document.getElementById("adicionar-categoria");
  if (modal.style.display === "flex") {
    modal.style.display = "none";
    content.style.height = 480 + "px";
  }else{
    modal.style.display = "flex";
    content.style.height = 650 + "px";

  }
}

function modalEditCategoria(id, nome){
  modal = document.getElementById("modal_edit_categoria");

  if(modal.style.display === "flex"){
    modal.style.display = "none";
  }else{
    modal.style.display = "flex";
    document.getElementById("categoria_id_edit").value = id;
    document.getElementById("categoria_nome_edit").value = nome;
  }
}

function modalDeleteCategoria(id, nome){
  modal = document.getElementById("modal_delete_categoria");

  if(modal.style.display === "flex"){
    modal.style.display = "none";
  }else{
    modal.style.display = "flex";
    document.getElementById("categoria_id_delete").value = id;
    document.getElementById("categoria_nome_delete").value = nome;
  }
}
