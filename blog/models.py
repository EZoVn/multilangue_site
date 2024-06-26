from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Blog(models.Model):
  title = models.CharField(_('title'), max_length=200)
  content = models.TextField(_('content'))
  pub_date = models.DateTimeField(_('publication date'), auto_now_add=True)
  
  class Meta:
    verbose_name = _('blog')
    verbose_name_plural = _('blogs')

  def __str__(self):
    return self.title