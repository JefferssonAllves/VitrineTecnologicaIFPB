from django.db import models

# Tabela de categorias
class Categoria(models.Model):
  nome = models.CharField(max_length=100, unique=True)
  descricao = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.nome


  #TODO 
  @property
  def quantidade_projetos(self):
    return self.projetos.count()

# Tabela de projetos
class Projeto(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True, null=True)
  autores = models.TextField(blank=True, null=True)
  categoria = models.CharField(max_length=100)
  imagem = models.ImageField(upload_to='projetos', blank=True, null=True)
  areas_conhecimento = models.ManyToManyField(Categoria, related_name='projetos')

  def __str__(self):
    return self.titulo
