from django import forms#.ModelForm, forms.CharField, forms.HiddenInput
from django.forms import widgets
from . import models
from django.utils.safestring import mark_safe

# (1) https://stackoverflow.com/questions/43481931/how-to-upload-an-image-through-copy-paste-using-django-modelform#43502536

class PictureWidget(widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None): # (2) https://stackoverflow.com/questions/52039654/django-typeerror-render-got-an-unexpected-keyword-argument-renderer
        # => eso de 'renderer=None' no estaba inicialmente en la referencia (1), se lo agrego porque me daba error sin eso (solucion sacada de referencia (2))
        print('rendering... value='+str(value))
        #if str(value) == '': # (esto saco porque value!='' siempre, es None (hasta ahora.. siempre)
        if value is None:
            html1 = "<img id='id_imagen' style='display:block' class='rounded float-left d-block'/>"
        else:
            html1 = "<img id='id_imagen' style='display:block' class='rounded float-left d-block' src='" + str(value) + "'/>"
        return mark_safe(html1)

class Formulario(forms.ModelForm):
    imagen_container = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = models.Modelo
        fields = '__all__'
        widgets = {
            'imagen': PictureWidget(),
        }
    def save(self, commit=True):
        # check image_container data
        self.instance.image.delete(False)
        imgdata = self.cleaned_data['imagen_container'].split(',')
        print('imgdata is '+str(imgdata))
        try:
            ftype = imgdata[0].split(';')[0].split('/')[1]
            fname = slugify(self.instance.title)
            self.instance.image.save('%s.%s' % (fname, ftype), ContentFile(imgdata[1].decode("base64")))
        except:
            print('passing!')
            pass
        return super(MyForm, self).save(commit=commit)
