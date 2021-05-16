from django.contrib import admin

from .models import Regulations
from .models import Share
# Register your models here.


@admin.register(Regulations)
class RegulationsAdmin(admin.ModelAdmin):

    list_display = (  'id',                     
                     'type_of_regulations',
                     'is_writer_responsible', 
                     'percent_of_the_first_author', 
                     'percent_of_the_second_author', 
                     'percent_of_the_third_author', 
                     'percent_of_the_fourth_author',
                     'percent_of_the_5th_author',
                     'percent_of_the_6th_author', 
                     'percent_article_abstract',                    
                   )

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):

    list_display = (  'id', 
                      'type_of_articel',
                     'type_of_regulations',
                     'score_first_quarter',
                     'score_second_quarter',
                     'score_third_quarter',
                     'score_fourth_quarter'
                   )