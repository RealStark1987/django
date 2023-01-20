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
    
    created = models.DateField(      
    )    
    
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= "Creada Por:"
    )
    
    def __str__(self) -> str:
        return self.nombre

class Planteamiento(models.Model):
    plant_name = models.CharField(
        max_length=80,
        verbose_name="Nombre del Planteamiento",
        null=True
    )
    
    created_at = models.DateField(
        
    )
    
    description = models.TextField(
        max_length=500,
        verbose_name="Descripcion"
    )
    
    created_by = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        null=True
    )
    
    on_act = models.ForeignKey(
        Acta,
        on_delete=models.CASCADE,
        null=True,
        verbose_name= "Planteamiento en Acta:"
    )
    
    def __str__(self) -> str:
        return self.plant_name + " planteado por: " + self.created_by.name


  
