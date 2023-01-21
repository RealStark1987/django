from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Worker(models.Model):
    Femenino = 'F'
    Masculino = 'M'
    SOLTERO = 'S'
    CASADO = 'C'
    DIVORCIADO = 'D'
    VIUDO = 'V'
    PROFESOR = 'Profesor'
    TECNICO = 'Tecnico'
    AUXILIAR = 'Auxiliar'
    SECRETARIO = 'Secretario'
    JEFE_DE_AREA = 'Jefe de Area'
    
    sex_type=[
        (Femenino,'F'),
        (Masculino, 'M')
    ]
    status=[
        (SOLTERO,'Soltero'),
        (CASADO,'Casado'),
        (DIVORCIADO,'Divorciado'),
        (VIUDO,'Viudo'),
    ]
    occupation_type=[
        (PROFESOR,'Profesor'),
        (TECNICO, 'Tecnico'),
        (AUXILIAR,'Auxiliar'),
        (SECRETARIO, 'Secretario'),
        (JEFE_DE_AREA, 'Jefe de Area')
        
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name="Introduza el Nombre"
    )
    
    lastname = models.CharField( 
        max_length=150,
        verbose_name="Introduza sus Apellidos",
        null=True
    )
    
    user_uci = models.CharField(
        max_length=50,
        null=True,
        verbose_name="Introduzca su usuario UCI"
    )
    
    correo= models.CharField(
        max_length=254,
        null=True,
        verbose_name="Introduza su Correo "
    )
    
    age = models.PositiveSmallIntegerField(
        null=True,
        verbose_name="Introduza su Edad "
    )
    
    sexo = models.CharField(
        max_length=1,
        choices=sex_type,
        verbose_name="Introduza su Sexo "
    )
    
    DNI = models.CharField(
        max_length=11,  
        blank=True,
        null=True,
        verbose_name="Introduza su Carnet de Identidad"
    )
    
    address=models.TextField(
        max_length=200,
        default='',
        null=True,
        verbose_name="Diga su Direccion"
    )
    
    cell=models.CharField(
        max_length=11,
        null=True,
        verbose_name="Introduza su Telefono"
    )
     
    occupation = models.TextField(
        choices=occupation_type,
        null=True,
        verbose_name="Ocupacion"
    )
    
    salary=models.FloatField(
        null=True,
        verbose_name="Introduza el Salario "
    )
    
    cuota=models.FloatField(
        null=True,
        verbose_name="Introduza la Cuota Mensual "
    )
    
    civil_state = models.TextField(
        choices=status,
        verbose_name="Estado Civil"
    )
    
    kids = models.PositiveSmallIntegerField(  
        verbose_name="Hijos"
    )   
    
    added_by= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Agregado Por: "
    )
    
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user_uci + ' added by '+ self.added_by.username

class Acta(models.Model):
    nombre = models.CharField(
        max_length=200,
        null=True
    )
    
    description = models.TextField(
        max_length=20000,
        null=True
    )
    
    created = models.DateField(    
        auto_now_add=True,  
    )    
    
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= "Creada Por:"
    )
    
    def __str__(self) -> str:
        return self.nombre

