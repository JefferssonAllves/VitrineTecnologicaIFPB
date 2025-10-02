from django.db import models

# Tabela de projetos
class Projeto(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True, null=True)
  autores = models.TextField(blank=True, null=True)
  categoria = models.CharField(max_length=100)
  imagem = models.ImageField(upload_to='projetos', blank=True, null=True)

  def __str__(self):
    return self.nome

# Tabela de categorias
class AreaConhecimento(models.Model):
  nome = models.CharField(max_length=100, unique=True)
  descricao = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.nome

# Relação de muitos para muitos
class ProjetoArea(models.Model):
  projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
  categoria = models.ForeignKey(AreaConhecimento, on_delete=models.CASCADE)