from django.conf.urls.defaults import *
from views import *
  
urlpatterns = patterns('',
    (r'habitatrepresentation/mpa/(\d+)/(\w+)/$',mpa_habitat_representation),
    (r'habitatrepresentation/array/(\d+)/(\w+)/$',array_habitat_representation_summed),
    url(r'habitatreplication/array/(\d+)/(\w+)/$',array_habitat_replication, name='array_replication'),
    url(r'habitatspreadsheet/array/(?P<array_id_list_str>(\d+,?)+)/$',array_list_habitat_excel, name='array_habitat_spreadsheet'),
)