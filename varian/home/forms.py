from django import forms


class LoginForm(forms.Form):
    account_id =    forms.CharField(label="Username", max_length=25, required=False)
    account_pass =  forms.CharField(label="Password", max_length=64, required=False)


class RegForm(forms.Form):
    a_id =          forms.CharField(max_length=25, required=False)
    a_email =       forms.EmailField(required=False)
    a_pass =        forms.CharField(max_length=64, min_length=8, required=False)
    a_check_pass =  forms.CharField(max_length=64, min_length=8, required=False)

class DataAssign(forms.Form):
    height =        forms.IntegerField(max_value=250, min_value=100, required=False)
    weight =        forms.IntegerField(max_value=250, min_value=30, required=False)
    allergies =     forms.CharField(max_length=300, required=False)
    others =        forms.CharField(max_length=500, required=False)
    first_name =    forms.CharField(required=False)
    last_name =     forms.CharField(required=False)
    taj =           forms.CharField(required=False)
    age =           forms.IntegerField(required=False)
    sex =           forms.CharField(required=True)
    region =        forms.CharField(required=True)
    tick =          forms.BooleanField(required=False)
    password =      forms.CharField(required=False)
    checkPassword = forms.CharField(required=False)
    email =         forms.EmailField(required=False)

#class DoctorSubmit(forms.Form):


