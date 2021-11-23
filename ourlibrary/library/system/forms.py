from django.forms import ModelForm, FileInput, forms
from .models import Student, Book
class std_update(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', "photo", ]
        widgets = {
            'photo': FileInput(),
        }


class br_process(ModelForm):

    class Meta:
        model = Book
        fields = ['return_date', ]
        # labels = {
        #     'active': 'Read All Instructions',
        # }
