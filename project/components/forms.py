from django.forms import ModelForm
from ..models import *

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields=[
            'name','lastname','user_uci','correo',
            'age','sexo','DNI','address','cell',
            'occupation','salary','cuota','civil_state','kids',
            
        ] 
        

class ActForm(ModelForm):
    class Meta:
        model = Acta
        fields=[
            'nombre','description','created_by',
        ] 