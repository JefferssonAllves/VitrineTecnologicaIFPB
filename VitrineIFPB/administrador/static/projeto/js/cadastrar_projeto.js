class MultiStepForm {
  constructor() {
    this.tabs = document.querySelectorAll(".tab");
    this.currentTab = 0;
    this.prevBtn = document.getElementById("prevBtn");
    this.nextBtn = document.getElementById("nextBtn");
    this.submitButton = document.getElementById("submitBtn");

    this.init();
  }

  init() {
    this.prevBtn.style.display = "none";
    this.showTab(this.currentTab);

    this.prevBtn.addEventListener("click", () => this.prevTab());
    this.nextBtn.addEventListener("click", () => this.nextTab());
  }

  showTab(n) {
    this.tabs.forEach((tab) => tab.classList.remove("active"));
    this.tabs[n].classList.add("active");

    if (this.currentTab === this.tabs.length - 1) {
      this.nextBtn.style.display = "none";
      this.submitButton.style.display = "inline";
    } else {
      this.nextBtn.style.display = "inline";
      this.submitButton.style.display = "none";
    }

    if (this.currentTab === 0) {
      this.prevBtn.style.display = "none";
    } else {
      this.prevBtn.style.display = "inline";
    }
  }

  prevTab() {
    this.currentTab--;
    this.showTab(this.currentTab);
  }


  nextTab() {
    this.currentTab++;
    this.showTab(this.currentTab);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new MultiStepForm();
});

function atualizarLabel(input){
  console.log(input);
  console.log(input.value);
  const nome = input.value.replace(/^.*[\\\/]/, '');
  const id = input.name;

  label = document.getElementsByClassName(id);
  caminho_imagem_label = document.getElementById('caminho_icone').value;
  label[0].textContent = nome;
  label[0].appendChild(document.createElement("img")).src = caminho_imagem_label;
}


function atualizarImagemPreview(input) {
  if (input.files && input.files[0]) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const imagemPreview = document.getElementById('projeto_imagem_edit');
      imagemPreview.src = e.target.result;
    };

    reader.readAsDataURL(input.files[0]);
  }
}

document.getElementById('abrir-modal-categorias').addEventListener('click', function() {
  const modal = document.querySelector('.modal-categorias');
  if (modal.style.display === "none" || modal.style.display === "") {
    modal.style.display = "flex";
  } else {
    modal.style.display = "none";
  }
});

document.addEventListener('click', function(event) {
  const modal = document.querySelector('.modal-categorias');
  const button = document.getElementById('abrir-modal-categorias');

  if (!modal.contains(event.target) && !button.contains(event.target)) {
    modal.style.display = 'none';
  }
});

function atualizarCategoriasSelecionadas() {
  const checkboxes = document.querySelectorAll('.projeto-checkbox');
  const categoriasSelecionadas = [];
  checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
      categoriasSelecionadas.push(checkbox.id);
    }
  });
  if (categoriasSelecionadas.length === 0) {
    categoriasSelecionadas.push('Selecione as categorias que o projeto se encaixa');
  }
  document.getElementById('abrir-modal-categorias').textContent = categoriasSelecionadas.join(', ');
  document.getElementById('abrir-modal-categorias').appendChild(document.createElement("img")).src = document.getElementById('caminho_icone_seta').value;

}

const checkboxes = document.querySelectorAll('.projeto-checkbox');
const checkboxesEdit = document.querySelectorAll('.projeto-categorias-edit');
checkboxes.forEach(checkbox => {
  checkboxesEdit.forEach(checkboxEdit => {
    if (checkbox.id === checkboxEdit.value) {
      checkbox.checked = true;
    }
  });
  checkbox.addEventListener('change', atualizarCategoriasSelecionadas);
});

atualizarCategoriasSelecionadas();