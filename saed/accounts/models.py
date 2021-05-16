from django.db import models
from django.db.models.fields import IntegerField

from jcr.models import TimeStampedModel
from .validators import validate_size

from enum import Enum
# Create your models here.

class Regulations(TimeStampedModel):

    class WriterResponsible(Enum):
        YES = ('1','بله')
        NO = ('0','خیر')       
        
        @classmethod
        def get_value(self,member):
            return cls[member].value[0]

    class TypeOfRegulations(Enum):
        regulations_absorption = ("absorption", 'جذب')
        regulations_promotional = ('promotional','ترفیع')              
        regulations_grant = ('grant', 'پژوهانه یا گرنت')        
        regulations_right_to_encouragement = ('right_to_encouragement','حق التشویق')
        regulations_status_conversion = ('status_conversion', 'تبدیل وضعیت')
        
        @classmethod
        def get_value(self,member):
            return cls[member].value[0]
    type_of_regulations = models.CharField(verbose_name='نوع آیین نامه', max_length=200,
                                           choices=[x.value for x in TypeOfRegulations],
                                           default='absorption'
                                          ) 
    is_writer_responsible = models.CharField(verbose_name='نویسنده مسئول', max_length=1,
                                          choices=[x.value for x in WriterResponsible],
                                          default='1'
                                         )                                             
    percent_of_the_first_author = models.DecimalField(verbose_name='سهم یک نفر', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)
    percent_of_the_second_author = models.DecimalField(verbose_name='سهم دونفر', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)
    percent_of_the_third_author = models.DecimalField(verbose_name='سهم سه نفر', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)
    percent_of_the_fourth_author = models.DecimalField(verbose_name='سهم چهار نفر', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)
    percent_of_the_5th_author = models.DecimalField(verbose_name='سهم پنج نفر', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)
    percent_of_the_6th_author = models.DecimalField(verbose_name='سهم شش نفر', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)
    percent_article_abstract = models.DecimalField(verbose_name='درصد چکیده بودن مقاله', max_digits=19, decimal_places=5, validators=[validate_size], blank=True, null= True)

class Share(TimeStampedModel):

    class TypeOfArticle(Enum):
        articel_jcr = ("JCR", 'JCR')
        articel_scopus = ('SCOPUS','SCOPUS')              
        articel_wos = ('WOS', 'WOS')        
        articel_scientific_research = ('Scientific_research', 'علمی پژوهشی')       
        
        @classmethod
        def get_value(self,member):
            return cls[member].value[0]

    class TypeOfRegulations(Enum):
        regulations_absorption = ("absorption", 'جذب')
        regulations_promotional = ('promotional','ترفیع')              
        regulations_grant = ('grant', 'پژوهانه یا گرنت')        
        regulations_right_to_encouragement = ('right_to_encouragement','حق التشویق')
        regulations_status_conversion = ('status_conversion', 'تبدیل وضعیت')
        
        @classmethod
        def get_value(self,member):
            return cls[member].value[0]

    type_of_regulations = models.CharField(verbose_name='نوع آیین نامه', max_length=200,
                                           choices=[x.value for x in TypeOfRegulations],
                                           default='absorption'
                                          )             
    type_of_articel = models.CharField(verbose_name='نوع مقاله', max_length=200,
                                        choices=[x.value for x in TypeOfArticle],
                                        default='JCR'
                                          ) 
    score_first_quarter = models.DecimalField(verbose_name='امتیاز چارک اول', max_digits=19, decimal_places=5, blank=True, null= True)
    score_second_quarter = models.DecimalField(verbose_name='امتیاز چارک دوم', max_digits=19, decimal_places=5, blank=True, null= True)
    score_third_quarter = models.DecimalField(verbose_name='امتیاز چارک سوم',  max_digits=19, decimal_places=5, blank=True, null= True)
    score_fourth_quarter = models.DecimalField(verbose_name='امتیاز چارک چهارم', max_digits=19, decimal_places=5, blank=True, null= True)

    
    
    
    