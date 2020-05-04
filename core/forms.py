from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = {
    ('S', 'Stripe'),
    ('P', 'Paypal')
}


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    billing_address = forms.CharField(required=False)

    shipping_address2 = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)

    shipping_country = CountryField(blank_label='Select country').formfield(
        required=False,
        widget=CountrySelectWidget(
            attrs={
                'class': 'custom-select d-block w-100'
            }))
    billing_country = CountryField(blank_label='Select country').formfield(
        required=False,
        widget=CountrySelectWidget(
            attrs={
                'class': 'custom-select d-block w-100'
            }))

    shipping_zip_code = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    billing_zip_code = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    same_billing_address = forms.BooleanField(
        required=False, widget=forms.CheckboxInput())

    set_default_shipping_address = forms.BooleanField(required=False)
    set_default_billing_address = forms.BooleanField(required=False)

    use_default_shipping_address = forms.BooleanField(required=False)
    use_default_billing_address = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2"
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
