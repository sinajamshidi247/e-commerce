from django import forms



class CouponForm(forms.Form):
    code = forms.CharField()



class ContactForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
	full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your full  name'}))	
	body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'your idea'}))