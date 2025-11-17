from django.db import models

# Tabela de categorias
class Categoria(models.Model):
  nome = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.nome

  @property
  def quantidade_projetos(self):
    return self.projetos.count()

# Tabela campus
class Campus(models.Model):
  nome = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.nome

  @property
  def quantidade_projetos(self):
    return self.projetos.count()

# Tabela de projetos
class Projeto(models.Model):

  class STATUS_CHOICES(models.TextChoices):
    EM_ANDAMENTO = 'Em Andamento'
    CONCLUIDO = 'Concluído'
    PARADO = 'Parado'

  imagem = models.ImageField(upload_to='projetos/imagens/', blank=True, null=True)#
  titulo = models.CharField(max_length=100)#
  servidor_solicitante = models.CharField(max_length=100)
  descricao = models.TextField()#
  setor_lotacao = models.CharField(max_length=20)
  ano_deposito = models.CharField(max_length=4)
  link = models.URLField(blank=True, null=True)
  status = models.CharField(max_length=50, choices=STATUS_CHOICES.choices, default='em andamento')
  certificado = models.FileField(upload_to='projetos/certificados/', blank=True, null=True)
  observacoes = models.TextField(blank=True, null=True)
  categorias = models.ManyToManyField(Categoria, related_name='projetos')#
  campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='projetos')#


  @property
  def get_projetos_em_andamento(self):
    return Projeto.objects.filter(status=self.STATUS_CHOICES.EM_ANDAMENTO).count()

  @classmethod
  def get_projetos_concluidos(cls):
    return cls.objects.filter(status=cls.STATUS_CHOICES.CONCLUIDO).count()

  @classmethod
  def get_projetos_parados(cls):
    return cls.objects.filter(status=cls.STATUS_CHOICES.PARADO).count()

  @classmethod
  def quantidade_projetos(cls):
    return cls.objects.count()

  def __str__(self):
    return self.titulo