from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Ads,AdsImages,Category,State,Lga,Offer



class AdsForm(forms.ModelForm):
    # AGE = (
    #     ('', ''),
    #     ('05', '0-5 Years'),
    #     ('10', '0-10 Years'),
    #     ('15', '0-15 Years'),
    #     ('20', '0-20 Years'),
    #     ('21', '20+ Years'),)
    #
    # BEDROOMS = (
    #     ('', ''),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', 'More than 5'),)
    #
    # BATHROOMS = (
    #     ('', ''),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', 'More than 5'),)
    #
    # ROOMS = (
    #     ('', ''),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', 'More than 5'),)
    #
    # PERIOD = (
    #     ('', ''),
    #     ('monthly', 'Monthly'),
    #     ('yearly', 'Yearly'),)
    #
    # CONDITION = (
    #     ('', ''),
    #     ('new', 'New'),
    #     ('old', 'Old'),
    #     ('uncompleted', 'Uncompleted'),
    #     ('renovated', 'Renovated'),)
    #
    # property_title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'Enter Title'}
    #     )
    # )
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='id', required=True,label='Property Type')
    # state = forms.ModelChoiceField(queryset=State.objects.all(), to_field_name='id', required=True)
    # property_offer = forms.ModelChoiceField(queryset=Offer.objects.all(), to_field_name='id', required=True,label='Property Status')
    # # subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), to_field_name='id', required=True,)
    # condition = forms.ChoiceField(choices=CONDITION, required=True)
    property_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'NGN'}
        )
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    # property_area = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'sq.ft'}
    #     )
    # )
    # building_age = forms.ChoiceField(choices=AGE, required=False)
    # rent_period = forms.ChoiceField(choices=PERIOD, required=False,label='Rental Period')
    # property_room = forms.ChoiceField(choices=ROOMS,required=False)
    # bedroom = forms.ChoiceField(choices=BEDROOMS, required=False)
    # bathroom = forms.ChoiceField(choices=BATHROOMS,required=False)
    # address = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
    #     )
    # )
    # lot_size  = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'sq.ft'}
    #     )
    # )
    # plan_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    church = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)

    school = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)

    mosque = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    beach = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    air_conditioning = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    parking = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    sewer = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    water = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    lawn = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    swimming_pool = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    barbecue = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    tv_cable = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    microwave = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    wi_fi = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    gym = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    market = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    hospital = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    resturant = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)

    class Meta:
        model = Ads
        fields = ('property_title', 'category','state','city', 'property_offer', 'condition','property_price','description','property_area',
                  'building_age','rent_period','property_room','bedroom','bathroom','address','lot_size','church',
                  'school','mosque','beach','air_conditioning','parking','sewer','water','lawn','swimming_pool',
                  'barbecue','tv_cable','microwave','wi_fi','gym','market','hospital','resturant','plan_image')

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
            self.fields['city'].queryset = self.instance.state.city.order_by('name')


class AdsImageForm(forms.ModelForm):
    ad_image = forms.ImageField(label='Image')
    class Meta:
        model = AdsImages
        fields = ('ad_image', )



class AdsEditForm(forms.ModelForm):
    # AGE = (
    #     ('', ''),
    #     ('05', '0-5 Years'),
    #     ('10', '0-10 Years'),
    #     ('15', '0-15 Years'),
    #     ('20', '0-20 Years'),
    #     ('21', '20+ Years'),)
    #
    # BEDROOMS = (
    #     ('', ''),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', 'More than 5'),)
    #
    # BATHROOMS = (
    #     ('', ''),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', 'More than 5'),)
    #
    # ROOMS = (
    #     ('', ''),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', 'More than 5'),)
    #
    # PERIOD = (
    #     ('', ''),
    #     ('monthly', 'Monthly'),
    #     ('yearly', 'Yearly'),)
    #
    # CONDITION = (
    #     ('', ''),
    #     ('new', 'New'),
    #     ('old', 'Old'),
    #     ('uncompleted', 'Uncompleted'),
    #     ('renovated', 'Renovated'),)
    #
    # property_title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'Enter Title'}
    #     )
    # )
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='id', required=True,label='Property Type')
    # state = forms.ModelChoiceField(queryset=State.objects.all(), to_field_name='id', required=True)
    # property_offer = forms.ModelChoiceField(queryset=Offer.objects.all(), to_field_name='id', required=True,label='Property Status')
    # # subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), to_field_name='id', required=True,)
    # condition = forms.ChoiceField(choices=CONDITION, required=True)
    property_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'NGN'}
        )
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    # property_area = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'sq.ft'}
    #     )
    # )
    # building_age = forms.ChoiceField(choices=AGE, required=False)
    # rent_period = forms.ChoiceField(choices=PERIOD, required=False,label='Rental Period')
    # property_room = forms.ChoiceField(choices=ROOMS,required=False)
    # bedroom = forms.ChoiceField(choices=BEDROOMS, required=False)
    # bathroom = forms.ChoiceField(choices=BATHROOMS,required=False)
    # address = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
    #     )
    # )
    # lot_size  = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'sq.ft'}
    #     )
    # )
    # plan_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    church = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)

    school = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)

    mosque = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    beach = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    air_conditioning = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    parking = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    sewer = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    water = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    lawn = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    swimming_pool = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    barbecue = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    tv_cable = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    microwave = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    wi_fi = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    gym = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    market = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    hospital = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)
    resturant = forms.BooleanField(
        widget=forms.CheckboxInput(),required=False)

    class Meta:
        model = Ads
        fields = ('property_title', 'category','state','city', 'property_offer', 'condition','property_price','description','property_area',
                  'building_age','rent_period','property_room','bedroom','bathroom','address','lot_size','church',
                  'school','mosque','beach','air_conditioning','parking','sewer','water','lawn','swimming_pool',
                  'barbecue','tv_cable','microwave','wi_fi','gym','market','hospital','resturant','plan_image')

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
            self.fields['city'].queryset = self.instance.state.lga_set.order_by('name')


class AdsEditImageForm(forms.ModelForm):
    ad_image = forms.ImageField(label='Image')
    class Meta:
        model = AdsImages
        fields = ('ad_image', )



