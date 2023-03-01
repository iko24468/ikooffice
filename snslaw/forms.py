
from django.forms import ModelForm
from .models import MyClient, ClientFiles, NewTadFile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm, TextInput, EmailInput

# from .models import User

class UserInfoForm(ModelForm):
    class Meta:
        model = MyClient
        fields = ['first_name', 'mail']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'mail': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }
class DateInput(forms.DateInput):
    input_type = 'date'


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    my_date_field = forms.DateField(widget=DateInput)
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


class MyclientForm(ModelForm):
    # required_css_class = 'required'
    class Meta:
        model = MyClient
        fields = '__all__'
        widgets = {
            "birth_date": DateInput()}
        # date = forms.DateField(widget=DateInput(format='%d-%m-%Y'),
        #                        input_formats=['%d-%m-%Y'])


class ClientFileForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = ClientFiles
        fields = ['file_type', 'status', 'open_date', 'close_date', 'superior', 'work_accident']
        widgets = {
            "open_date": DateInput(),
            "close_date": DateInput()
        }


# class TadFileForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.fields['event_place'].initial = 'כיכר העיר'
#
#     required_css_class = 'required'
#
#     class Meta:
#         model = TadFile
#         fields = '__all__'
#         labels = {'file_header': 'סוג התיק',}
#         widgets = {
#             "event_date": DateInput()
#         }

class NewTadFileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['event_place'].initial = 'מקום התאונה'

    required_css_class = 'required'
    # file_header = forms.ModelChoiceField(queryset=ClientFiles.objects.filter(file_type="תאונת דרכים"))
    class Meta:
        model = NewTadFile
        fields = ['status',
                  'work_accident',
                  'open_date',
                  'event_date',
                  'event_place',
                  'car_number',
                  'insurance_company',
                  'evacuation',
                  'involvment',
                  'circumstances',
                  'first_aid',
                  'complaints_and_findings',
                  'follow_up',
                  'sick_leave',
                  'damage',
                  'missing_documents',
                  'superior'
                  ]
        labels = {'file_header': 'סוג התיק',}
        widgets = {
            "event_date": DateInput(),
            "close_date": DateInput(),
            "open_date": DateInput(),
        }