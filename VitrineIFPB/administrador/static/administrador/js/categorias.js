function exibirResultados(data) {
  const corpoTabela = document.getElementById("corpo-tabela");
  const editIconUrl = corpoTabela.dataset.editIcon;
  const deleteIconUrl = corpoTabela.dataset.deleteIcon;
  categorias = data.categorias;

  corpoTabela.innerHTML = "";

  // Adicionar novos resultados
  categorias.forEach(categoria => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td data-label="id">${categoria.id}</td>
      <td data-label="nome">${categoria.nome}</td>
      <td data-label="Ações" class="admin-actions">
        <a href=""><img src="${editIconUrl}" alt="" width="24" height="24"></a>
        <a href=""><img src="${deleteIconUrl}" alt="" width="24" height="24"></a>
      </td>
    `;
    corpoTabela.appendChild(row);
  });
}