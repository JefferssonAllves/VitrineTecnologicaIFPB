let timeoutBusca = null;

function realizarBusca(termo) {
  const urlBusca = "/vitrine/buscar_projetos/";

  clearTimeout(timeoutBusca);


  timeoutBusca = setTimeout(async () => {
    try {
      const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

      const response = await fetch(urlBusca, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
          termo: termo,
        }),
      });

      const data = await response.json();
      exibirResultados(data.projetos);

    } catch (error) {
      console.error("Erro:", error);
    } finally {
      console.log("Busca finalizada");
    }
  }, 500);
}

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
  const inputBusca = document.getElementById('campo-busca');

  if (inputBusca) {
    inputBusca.addEventListener('input', function(e) {
      const termo = e.target.value.trim();
      realizarBusca(termo);
    });
    // realizarBusca('');
  }
});
