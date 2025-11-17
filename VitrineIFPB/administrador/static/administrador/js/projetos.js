function exibirResultados(data) {
  const corpoTabela = document.getElementById("corpo-tabela");
  projetos = data.projetos;

  corpoTabela.innerHTML = "";

  if (projetos.length === 0) {
    corpoTabela.innerHTML = `
      <tr>
        <td colspan="7" style="text-align: center;">Nenhum projeto encontrado.</td>
      </tr>
    `;
    return;
  }

  projetos.forEach(projeto => {
    const linha = document.createElement("tr");

    linha.innerHTML = `
      <td data-label="Id">${projeto.id}</td>
      <td data-label="Título">${projeto.titulo}</td>
      <td data-label="Setor de Lotação">${projeto.setor_lotacao}</td>
      <td data-label="Ano do depósito">${projeto.ano_deposito}</td>
      <td data-label="Status">
        <span class="status
          ${projeto.status === "Concluído" ? "concluido" : ""}
          ${projeto.status === "Em Andamento" ? "em-andamento" : ""}
          ${projeto.status === "Parado" ? "parado" : ""}">${projeto.status}</span>
      </td>
      <td data-label="Observações de Tramitação">${projeto.observacoes}</td>
      <td data-label="Ações" class="admin-actions">Editar</td>
    `;

    corpoTabela.appendChild(linha);
  });
}