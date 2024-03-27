from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, ScoreEverything
from django.core.validators import MinValueValidator, MaxValueValidator


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


#add record form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    image = forms.ImageField(required=False, label="Profile Picture")

    class Meta:
        model = Record
        exclude = ("user",)

class ScoreForm(forms.ModelForm):
    pn_performance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Performance", "class":"form-control"}), label="Performance Number (Poise and Bearing)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    pn_elegance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Elegance", "class":"form-control"}), label="Performance Number (Elegance)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    pn_beauty = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Beauty", "class":"form-control"}), label="Performance Number (Beauty)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    pn_audience = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Audience", "class":"form-control"}), label="Performance Number (Audience Impact)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    sw_poise = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Poise and Bearing", "class":"form-control"}), label="Swimsuit (Poise and Bearing)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    sw_body = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Body Proportion", "class":"form-control"}), label="Swimsuit (Body Proportion)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    sw_beauty = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Beauty", "class":"form-control"}), label="Swimsuit (Beauty)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    sw_audience = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Audience Impact", "class":"form-control"}), label="Swimsuit (Audience Impact)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    eg_poise = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Poise and Bearing", "class":"form-control"}), label="Evening Gown (Poise and Bearing)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    eg_elegance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Elegance", "class":"form-control"}), label="Evening Gown (Elegance)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    eg_beauty = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Beauty", "class":"form-control"}), label="Evening Gown (Beauty)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    eg_audience = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Audience Impact", "class":"form-control"}), label="Evening Gown (Audience Impact)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    fq_wisdom = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Wisdom", "class":"form-control"}), label="Final Question and Answer (Wisdom)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    fq_charisma = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Charisma", "class":"form-control"}), label="Final Question and Answer (Charisma)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    fq_intelligence = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Intelligence", "class":"form-control"}), label="Final Question and Answer (Intelligence)", validators=[MinValueValidator(1), MaxValueValidator(10)])
    fq_persuasion = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Persuasion", "class":"form-control"}), label="Final Question and Answer (Persuasion)", validators=[MinValueValidator(1), MaxValueValidator(10)])

    pn_total = forms.FloatField(widget=forms.HiddenInput(), required=False)
    sw_total = forms.FloatField(widget=forms.HiddenInput(), required=False)
    eg_total = forms.FloatField(widget=forms.HiddenInput(), required=False)
    fq_total = forms.FloatField(widget=forms.HiddenInput(), required=False)
    t_avg = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = ScoreEverything
        exclude = ("judge", "candidate", )

    def clean(self):
        cleaned_data = super().clean()
        pn_performance = cleaned_data.get('pn_performance', 0)
        pn_elegance = cleaned_data.get('pn_elegance', 0)
        pn_beauty = cleaned_data.get('pn_beauty', 0)
        pn_audience = cleaned_data.get('pn_audience', 0)

        pn_total = ((pn_performance * 30) + (pn_elegance * 30) + (pn_beauty * 30) + (pn_audience * 10)) / 10
        cleaned_data['pn_total'] = pn_total
        
        # Second set of variables (sw_total)
        sw_poise = cleaned_data.get('sw_poise', 0)
        sw_body = cleaned_data.get('sw_body', 0)
        sw_beauty = cleaned_data.get('sw_beauty', 0)
        sw_audience = cleaned_data.get('sw_audience', 0)

        sw_total = ((sw_poise * 30) + (sw_body * 30) + (sw_beauty * 30) + (sw_audience * 10)) / 10
        cleaned_data['sw_total'] = sw_total
        
        # Third set of variables (eg_total)
        eg_poise = cleaned_data.get('eg_poise', 0)
        eg_elegance = cleaned_data.get('eg_elegance', 0)
        eg_beauty = cleaned_data.get('eg_beauty', 0)
        eg_audience = cleaned_data.get('eg_audience', 0)

        eg_total = ((eg_poise * 30) + (eg_elegance * 30) + (eg_beauty * 30) + (eg_audience * 10)) / 10
        cleaned_data['eg_total'] = eg_total
        
        # Fourth set of variables (fq_total)
        fq_wisdom = cleaned_data.get('fq_wisdom', 0)
        fq_charisma = cleaned_data.get('fq_charisma', 0)
        fq_intelligence = cleaned_data.get('fq_intelligence', 0)
        fq_persuasion = cleaned_data.get('fq_persuasion', 0)

        fq_total = ((fq_wisdom * 30) + (fq_charisma * 30) + (fq_intelligence * 30) + (fq_persuasion * 10)) / 10
        cleaned_data['fq_total'] = fq_total

        # Calculate t_avg
        t_avg = (pn_total + sw_total + eg_total + fq_total) / 4
        cleaned_data['t_avg'] = t_avg
        
        return cleaned_data