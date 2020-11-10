import uuid
from django.db import models
from django_currentuser.db.models import CurrentUserField


class Task(models.Model):
    id = models.UUIDField(
        verbose_name='id da tarefa', primary_key=True, default=uuid.uuid4,
        editable=False
    )
    author = CurrentUserField(editable=False, verbose_name='usuário')
    title = models.CharField('titulo', max_length=200)
    description = models.TextField('decricao')
    to_do = models.BooleanField('a fazer', default = True)
    doing = models.BooleanField('sendo feita', default = False)
    done = models.BooleanField('feita', default = False)
    created_at = models.DateTimeField(
        verbose_name='criado em', auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='modificado em', auto_now=True
    )

    def set_doing(self):
        self.to_do = False
        self.done = False
        self.doing = True
        self.save()

    def set_done(self):
        self.to_do = False
        self.done = True
        self.doing = False
        self.save()
    
    def set_to_do(self):
        self.to_do = True
        self.done = False
        self.doing = False
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"