let timeoutBusca = null;

function realizarBusca(termo, urlBusca) {
  carregandoResultados();
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
      exibirResultados(data);

    } catch (error) {
      console.error("Erro:", error);
    }
  }, 500);
}

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
  const inputBusca = document.getElementById('campo-busca');
  const urlBusca = document.getElementById('url-busca').value;

  if (inputBusca) {
    inputBusca.addEventListener('input', function(e) {
      const termo = e.target.value.trim();
      realizarBusca(termo, urlBusca);
    });
    // realizarBusca('');
  }
});
