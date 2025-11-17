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
  const nome = input.value.replace(/^.*[\\\/]/, '');
  const id = input.id;
  
  label = document.getElementsByClassName(id);
  caminho_imagem_label = document.getElementById('caminho_icone').value;
  label[0].textContent = nome;
  label[0].appendChild(document.createElement("img")).src = caminho_imagem_label;
}