from django.db import models
from django.forms.widgets import Textarea, TextInput
from django.forms import ModelForm

# Create your models here.

COUNTRY_CHOICES = (
    ('United States of America', ('United States of America')),
    ('Afghanistan', ('Afghanistan')),
    ('Aland Islands', ('Aland Islands')),
    ('Albania', ('Albania')),
    ('Algeria', ('Algeria')),
    ('American Samoa', ('American Samoa')),
    ('Andorra', ('Andorra')),
    ('Angola', ('Angola')),
    ('Anguilla', ('Anguilla')),
    ('Antigua and Barbuda', ('Antigua and Barbuda')),
    ('Argentina', ('Argentina')),
    ('Armenia', ('Armenia')),
    ('Aruba', ('Aruba')),
    ('Australia', ('Australia')),
    ('Austria', ('Austria')),
    ('Azerbaijan', ('Azerbaijan')),
    ('Bahamas', ('Bahamas')),
    ('Bahrain', ('Bahrain')),
    ('Bangladesh', ('Bangladesh')),
    ('Barbados', ('Barbados')),
    ('Belarus', ('Belarus')),
    ('Belgium', ('Belgium')),
    ('Belize', ('Belize')),
    ('Benin', ('Benin')),
    ('Bermuda', ('Bermuda')),
    ('Bhutan', ('Bhutan')),
    ('Bolivia', ('Bolivia')),
    ('Bosnia and Herzegovina', ('Bosnia and Herzegovina')),
    ('Botswana', ('Botswana')),
    ('Brazil', ('Brazil')),
    ('British Virgin Islands', ('British Virgin Islands')),
    ('Brunei Darussalam', ('Brunei Darussalam')),
    ('Bulgaria', ('Bulgaria')),
    ('Burkina Faso', ('Burkina Faso')),
    ('Burundi', ('Burundi')),
    ('Cambodia', ('Cambodia')),
    ('Cameroon', ('Cameroon')),
    ('Canada', ('Canada')),
    ('Cape Verde', ('Cape Verde')),
    ('Cayman Islands', ('Cayman Islands')),
    ('Central African Republic', ('Central African Republic')),
    ('Chad', ('Chad')),
    ('Channel Islands', ('Channel Islands')),
    ('Chile', ('Chile')),
    ('China', ('China')),
    ('China - Hong Kong', ('China - Hong Kong')),
    ('China - Macao', ('China - Macao')),
    ('Colombia', ('Colombia')),
    ('Comoros', ('Comoros')),
    ('Congo', ('Congo')),
    ('Cook Islands', ('Cook Islands')),
    ('Costa Rica', ('Costa Rica')),
    ('Cote d\'Ivoire', ('Cote d\'Ivoire')),
    ('Croatia', ('Croatia')),
    ('Cuba', ('Cuba')),
    ('Cyprus', ('Cyprus')),
    ('Czech Republic', ('Czech Republic')),
    ('Democratic People\'s Republic of Korea', ('Democratic People\'s Republic of Korea')),
    ('Democratic Republic of the Congo', ('Democratic Republic of the Congo')),
    ('Denmark', ('Denmark')),
    ('Djibouti', ('Djibouti')),
    ('Dominica', ('Dominica')),
    ('Dominican Republic', ('Dominican Republic')),
    ('Ecuador', ('Ecuador')),
    ('Egypt', ('Egypt')),
    ('El Salvador', ('El Salvador')),
    ('Equatorial Guinea', ('Equatorial Guinea')),
    ('Eritrea', ('Eritrea')),
    ('Estonia', ('Estonia')),
    ('Ethiopia', ('Ethiopia')),
    ('Faeroe Islands', ('Faeroe Islands')),
    ('Falkland Islands (Malvinas)', ('Falkland Islands (Malvinas)')),
    ('Fiji', ('Fiji')),
    ('Finland', ('Finland')),
    ('France', ('France')),
    ('French Guiana', ('French Guiana')),
    ('French Polynesia', ('French Polynesia')),
    ('Gabon', ('Gabon')),
    ('Gambia', ('Gambia')),
    ('Georgia', ('Georgia')),
    ('Germany', ('Germany')),
    ('Ghana', ('Ghana')),
    ('Gibraltar', ('Gibraltar')),
    ('Greece', ('Greece')),
    ('Greenland', ('Greenland')),
    ('Grenada', ('Grenada')),
    ('Guadeloupe', ('Guadeloupe')),
    ('Guam', ('Guam')),
    ('Guatemala', ('Guatemala')),
    ('Guernsey', ('Guernsey')),
    ('Guinea', ('Guinea')),
    ('Guinea-Bissau', ('Guinea-Bissau')),
    ('Guyana', ('Guyana')),
    ('Haiti', ('Haiti')),
    ('Holy See (Vatican City)', ('Holy See (Vatican City)')),
    ('Honduras', ('Honduras')),
    ('Hungary', ('Hungary')),
    ('Iceland', ('Iceland')),
    ('India', ('India')),
    ('Indonesia', ('Indonesia')),
    ('Iran', ('Iran')),
    ('Iraq', ('Iraq')),
    ('Ireland', ('Ireland')),
    ('Isle of Man', ('Isle of Man')),
    ('Israel', ('Israel')),
    ('Italy', ('Italy')),
    ('Jamaica', ('Jamaica')),
    ('Japan', ('Japan')),
    ('Jersey', ('Jersey')),
    ('Jordan', ('Jordan')),
    ('Kazakhstan', ('Kazakhstan')),
    ('Kenya', ('Kenya')),
    ('Kiribati', ('Kiribati')),
    ('Kuwait', ('Kuwait')),
    ('Kyrgyzstan', ('Kyrgyzstan')),
    ('Lao People\'s Democratic Republic', ('Lao People\'s Democratic Republic')),
    ('Latvia', ('Latvia')),
    ('Lebanon', ('Lebanon')),
    ('Lesotho', ('Lesotho')),
    ('Liberia', ('Liberia')),
    ('Libyan Arab Jamahiriya', ('Libyan Arab Jamahiriya')),
    ('Liechtenstein', ('Liechtenstein')),
    ('Lithuania', ('Lithuania')),
    ('Luxembourg', ('Luxembourg')),
    ('Macedonia', ('Macedonia')),
    ('Madagascar', ('Madagascar')),
    ('Malawi', ('Malawi')),
    ('Malaysia', ('Malaysia')),
    ('Maldives', ('Maldives')),
    ('Mali', ('Mali')),
    ('Malta', ('Malta')),
    ('Marshall Islands', ('Marshall Islands')),
    ('Martinique', ('Martinique')),
    ('Mauritania', ('Mauritania')),
    ('Mauritius', ('Mauritius')),
    ('Mayotte', ('Mayotte')),
    ('Mexico', ('Mayotte')),
    ('Micronesia, Federated States of', ('Micronesia, Federated States of')),
    ('Monaco', ('Monaco')),
    ('Mongolia', ('Mongolia')),
    ('Montenegro', ('Montenegro')),
    ('Montserrat', ('Montserrat')),
    ('Morocco', ('Morocco')),
    ('Mozambique', ('Mozambique')),
    ('Myanmar', ('Myanmar')),
    ('Namibia', ('Namibia')),
    ('Nauru', ('Nauru')),
    ('Nepal', ('Nepal')),
    ('Netherlands', ('Netherlands')),
    ('Netherlands Antilles', ('Netherlands Antilles')),
    ('New Caledonia', ('New Caledonia')),
    ('New Zealand', ('New Zealand')),
    ('Nicaragua', ('Nicaragua')),
    ('Niger', ('Niger')),
    ('Nigeria', ('Nigeria')),
    ('Niue', ('Niue')),
    ('Norfolk Island', ('Norfolk Island')),
    ('Northern Mariana Islands', ('Northern Mariana Islands')),
    ('Norway', ('Norway')),
    ('Occupied Palestinian Territory', ('Occupied Palestinian Territory')),
    ('Oman', ('Oman')),
    ('Pakistan', ('Pakistan')),
    ('Palau', ('Palau')),
    ('Panama', ('Panama')),
    ('Papua New Guinea', ('Papua New Guinea')),
    ('Paraguay', ('Paraguay')),
    ('Peru', ('Peru')),
    ('Philippines', ('Philippines')),
    ('Pitcairn', ('Pitcairn')),
    ('Poland', ('Poland')),
    ('Portugal', ('Portugal')),
    ('Puerto Rico', ('Puerto Rico')),
    ('Qatar', ('Qatar')),
    ('Republic of Korea', ('Republic of Korea')),
    ('Republic of Moldova', ('Republic of Moldova')),
    ('Reunion', ('Reunion')),
    ('Romania', ('Romania')),
    ('Russian Federation', ('Russian Federation')),
    ('Rwanda', ('Rwanda')),
    ('Saint-Barthelemy', ('Saint-Barthelemy')),
    ('Saint Helena', ('Saint Helena')),
    ('Saint Kitts and Nevis', ('Saint Kitts and Nevis')),
    ('Saint Lucia', ('Saint Lucia')),
    ('Saint-Martin (French part)', ('Saint-Martin (French part)')),
    ('Saint Pierre and Miquelon', ('Saint Pierre and Miquelon')),
    ('Saint Vincent and the Grenadines', ('Saint Vincent and the Grenadines')),
    ('Samoa', ('Samoa')),
    ('San Marino', ('San Marino')),
    ('Sao Tome and Principe', ('Sao Tome and Principe')),
    ('Saudi Arabia', ('Saudi Arabia')),
    ('Senegal', ('Senegal')),
    ('Serbia', ('Serbia')),
    ('Seychelles', ('Seychelles')),
    ('Sierra Leone', ('Sierra Leone')),
    ('Singapore', ('Singapore')),
    ('Slovakia', ('Slovakia')),
    ('Slovenia', ('Slovenia')),
    ('Solomon Islands', ('Solomon Islands')),
    ('Somalia', ('Somalia')),
    ('South Africa', ('South Africa')),
    ('Spain', ('Spain')),
    ('Sri Lanka', ('Sri Lanka')),
    ('Sudan', ('Sudan')),
    ('Suriname', ('Suriname')),
    ('Svalbard and Jan Mayen Islands', ('Svalbard and Jan Mayen Islands')),
    ('Swaziland', ('Swaziland')),
    ('Sweden', ('Sweden')),
    ('Switzerland', ('Switzerland')),
    ('Syrian Arab Republic', ('Syrian Arab Republic')),
    ('Tajikistan', ('Tajikistan')),
    ('Thailand', ('Thailand')),
    ('Timor-Leste', ('Timor-Leste')),
    ('Togo', ('Togo')),
    ('Tokelau', ('Tokelau')),
    ('Tonga', ('Tonga')),
    ('Trinidad and Tobago', ('Trinidad and Tobago')),
    ('Tunisia', ('Tunisia')),
    ('Turkey', ('Turkey')),
    ('Turkmenistan', ('Turkmenistan')),
    ('Turks and Caicos Islands', ('Turks and Caicos Islands')),
    ('Tuvalu', ('Tuvalu')),
    ('Uganda', ('Uganda')),
    ('Ukraine', ('Ukraine')),
    ('United Arab Emirates', ('United Arab Emirates')),
    ('United Kingdom', ('United Kingdom')),
    ('United Republic of Tanzania', ('United Republic of Tanzania')),
    ('United States of America', ('United States of America')),
    ('United States Virgin Islands', ('United States Virgin Islands')),
    ('Uruguay', ('Uruguay')),
    ('Uzbekistan', ('Uzbekistan')),
    ('Vanuatu', ('Vanuatu')),
    ('Venezuela (Bolivarian Republic of)', ('Venezuela (Bolivarian Republic of)')),
    ('Viet Nam', ('Viet Nam')),
    ('Wallis and Futuna Islands', ('Wallis and Futuna Islands')),
    ('Western Sahara', ('Western Sahara')),
    ('Yemen', ('Yemen')),
    ('Zambia', ('Zambia')),
    ('Zimbabwe', ('Zimbabwe')),
)
PRESENTATION_TYPE_CHOICES = (
    ('Paper', 'Paper'),
    ('Poster', 'Poster'),
)
FUNDING_CHOICES = (
    ('True','Yes'),
    ('False','No'),
)


class Meeting(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    associated_with = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

# Variable assignments for Abstract model #

PRESENTATION_TYPE_HELP = "(Please evaluate your material carefully and decide whether a " \
                          "paper or poster is most appropriate. Papers and posters are " \
                          "presented in separate, non-concurrent sessions.)"
ABSTRACT_TEXT_HELP = "(Abstracts are limited to 300 words not counting acknowledgements. They must be in English.)"
REFERENCES_HELP = "(Include references only if they are cited in your abstract. Please follow the " \
                  "<a href='/static/pdfs/PaleoAnthropology%20Guidelines_articles.pdf'>journal&apos;s </a>format)"
COMMENTS_HELP = "(Please include any factors that should be included in an evaluation of this abstract. " \
                "For instance, if this paper is not substantially different from a recently given paper it may " \
                "be rejected. Thus, you might want to make clear how this paper differs.)"
FUNDING_HELP = "Check this box if you would like to be considered for partial funding."


class Abstract(models.Model):
    meeting = models.ForeignKey('Meeting')
    contact_email = models.EmailField(max_length=128, null=False, blank=False)
    presentation_type = models.CharField(max_length=20, null=False, blank=False, choices=PRESENTATION_TYPE_CHOICES,
                                         help_text=PRESENTATION_TYPE_HELP)
    title = models.CharField(max_length=128, null=False, blank=False)
    abstract_text = models.TextField(null=False, blank=False, help_text=ABSTRACT_TEXT_HELP)
    acknowledgements = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True, help_text=REFERENCES_HELP)
    comments = models.TextField(null=True, blank=True, help_text=COMMENTS_HELP)
    funding = models.NullBooleanField(help_text=FUNDING_HELP)
    year = models.IntegerField(null=False, blank=False)
    last_modified = models.DateField(null=False, blank=True, auto_now_add=True, auto_now=True)
    created = models.DateField(null=False, blank=True, auto_now_add=True)
    abstract_rank = models.IntegerField(null=True, blank=True)
    abstract_media = models.FileField(upload_to="media/", null=True, blank=True)

    def __unicode__(self):
        return self.title[0:20]


class Author(models.Model):
    abstract = models.ForeignKey('Abstract')
    author_rank = models.IntegerField()
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200, null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    email_address = models.EmailField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name


### Model Forms ###


class AbstractForm(ModelForm):
    class Meta:
        model = Abstract

        fields = (
            'contact_email',
            'presentation_type',
            'title',
            'abstract_text',
            'acknowledgements',
            'references',
            'comments',
            'funding',
        )

        widgets = {
            'contact_email':TextInput(attrs={'size': 40,}),
            'title':TextInput(attrs={'size': 80,}),
            'abstract_text':Textarea(attrs={'cols': 60, 'rows': 20}),
            'acknowledgements':Textarea(attrs={'cols': 60, 'rows': 5}),
            'references':Textarea(attrs={'cols': 60, 'rows': 5}),
            'comments':Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author

        fields = (
            'name',
            'department',
            'institution',
            'country',
            'email_address',
        )

        widgets = {
            'name':TextInput(attrs={'size':50}),
            'department':TextInput(attrs={'size':50}),
            'institution':TextInput(attrs={'size':50}),
            'email_address':TextInput(attrs={'size':50}),
        }
