from django.forms import ModelForm
from ..models import Worker 

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields=[
            'name','lastname','user_uci','correo',
            'age','sexo','DNI','address','cell',
            'occupation','salary','civil_state','kids',
            
        ] 
        