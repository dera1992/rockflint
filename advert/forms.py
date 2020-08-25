from django import forms
from .models import Ads,AdsImages,Category,State,Lga,Offer



class AdsForm(forms.ModelForm):
    property_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'NGN'}
        )
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
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
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='id', required=True,label='Property Type')
    property_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'NGN'}
        )
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
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



