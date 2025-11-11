function exibirResultados(data) {
  const container = document.getElementById('grid-projects');
  projetos = data.projetos;


  if (!projetos || projetos.length === 0) {
    container.innerHTML = `
      <div class="nenhum-resultado">
        <p>Nenhum projeto encontrado.</p>
      </div>`;
    return;
  }

  container.innerHTML = projetos.map(projeto => `
    <div class="card">
      <a href="/vitrine/detalhes_projeto/id=${projeto.id}/">
        ${projeto.imagem_url ? `<img src="${projeto.imagem_url}" alt="${projeto.titulo}">` : '<div class="placeholder-image">Sem imagem</div>'}
        <div class="info">
          <h3>${projeto.titulo}</h3>
          <p>${projeto.descricao || 'Sem descrição'}</p>
        </div>
      </a>
    </div>`).join('');
}

function carregandoResultados() {
  const container = document.getElementById('grid-projects');
  container.innerHTML = `
    <div class="carregando">
      <p>Carregando...</p>
    </div>`;
}