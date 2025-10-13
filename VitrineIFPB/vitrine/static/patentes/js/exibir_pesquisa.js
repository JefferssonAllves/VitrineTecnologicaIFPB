function exibirResultados(projetos) {
  const container = document.getElementById('patent-list');

  if (!projetos || projetos.length === 0) {
    container.innerHTML = `
      <div class="nenhum-resultado">
        <p>Nenhum projeto encontrado.</p>
      </div>`;
    return;
  }

  container.innerHTML = projetos.map(projeto => `
    <a href="/vitrine/detalhes_projeto/id=${projeto.id}/" class="patent-item">
      <img src="${projeto.imagem_url}" alt="${projeto.titulo}" class="patent-image">
      <div class="patent-info">
        <div class="tags-container">
          ${projeto.areas_conhecimento.map(area => `<span class="tags">${area}</span>`).join('')}
        </div>
        <h3 class="patent-title">${projeto.titulo}</h3>
      </div>
    </a>`).join('');
}

function carregandoResultados() {
  const container = document.getElementById('patent-list');
  container.innerHTML = `
    <div class="carregando">
      <p>Carregando...</p>
    </div>`;
}