from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Ads,AdsImages,Category,SubCategory,State,Lga



class AdsForm(forms.ModelForm):
    AGE = (
        ('05', '0-5 Years'),
        ('10', '0-10 Years'),
        ('15', '0-15 Years'),
        ('20', '0-20 Years'),
        ('21', '20+ Years'),)

    BEDROOMS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'More than 5'),)

    BATHROOMS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'More than 5'),)

    ROOMS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'More than 5'),)

    PERIOD = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),)

    CONDITION = (
        ('new', 'New'),
        ('old', 'Old'),
        ('uncompleted', 'Uncompleted'),
        ('renovated', 'Renovated'),)

    ad_title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Title'}
        )
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='id', required=True)
    state = forms.ModelChoiceField(queryset=State.objects.all(), to_field_name='id', required=True)
    ad_offer = forms.ModelChoiceField(queryset=State.objects.all(), to_field_name='id', required=True)
    # subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), to_field_name='id', required=True,)
    condition = forms.ChoiceField(choices=CONDITION, required=True)
    ad_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Price'}
        )
    )
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    ad_area = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'sq.ft'}
        )
    )
    building_age = forms.ChoiceField(choices=AGE, required=True)
    rent_period = forms.ChoiceField(choices=PERIOD, required=True)
    ad_room = forms.ChoiceField(choices=ROOMS,required=True)
    bedroom = forms.ChoiceField(choices=BEDROOMS, required=True)
    bathroom = forms.ChoiceField(choices=BATHROOMS,required=True)
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
        )
    )
    lot_size  = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'sq.ft'}
        )
    )

    class Meta:
        model = Ads
        fields = ('ad_title', 'category','state','city', 'ad_offer', 'condition','ad_price','description','ad_area',
                  'building_age','rent_period','ad_room','bedroom','bathroom','address','lot_size','church',
                  'school','mosque','beach','air_conditioning','parking','sewer','water','lawn','swimming_pool',
                  'barbecue','tv_cable','microwave','wi_fi','gym','market','hospital','resturant')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = Lga.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = Lga.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')


class AdsImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = AdsImages
        fields = ('ad_image', )



