from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    project_name = forms.CharField(label='Project')
    client = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    num_sample = forms.IntegerField(label='# of Samples')

    description = forms.CharField(label='notes', widget=forms.Textarea)

    sample_type = forms.ChoiceField(required=False, label='Sample Type', choices=[('','---'), ('wet sediment', 'Wet Sediment'), ('dry sediment', 'Dry Sediment'), ('water', 'Water'),
     ('water with solvent', 'Water With Solvent'), ('extract', 'Extract')])

    extraction_method = forms.ChoiceField(required=False, label='Extraction Method', choices=[('','---'), ('soxhlet', 'Soxhlet'), ('saponification', 'Saponification'), ('sepratory funnel', 'Sepratory Funnel'), 
    ('roller', 'Roller'), ('other', 'Other')])

    sample_cleanup = forms.ChoiceField(required=False, label='Sample Cleanup', choices=[('','---'), ('silica gel', 'Silica Gel'), ('gpc', 'GPC'), ('none', 'None'), 
    ('purge & trap', 'Purge & Trap'), ('other', 'Other')])

    analysis_instrumentation = forms.ChoiceField(required=False, label='Analysis Instrumentation', choices=[('','---'), ('gc/ms', 'GC/MS'), ('gc/fid', 'GC/FID'), ('spectrophotometer', 'Spectrophotometer'), 
    ('iatroscan', 'Iatroscan'), ('lc', 'LC'), ('other', 'Other')])

    
    #analysis_type = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=analysis_type_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'project_name',
           
            Submit('submit', 'Submit', css_class='btn-success')
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'email', 'quantity','description', 'sample_type', 'extraction_method',
         'sample_cleanup', 'analysis_instrumentation','analysis_pah','analysis_alkanes','analysis_phenols', 'analysis_tph', 'analysis_btex',
         'log_comments')
        labels = {'name':'Client Name', 'analysis_pah':'PAHs', 'analysis_alkanes':'Alkanes','log_comments': 'Comments',
         'analysis_phenols': 'Phenols','analysis_tph': 'TPH','analysis_tph':'BTEX'}   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'quantity',
            'description',
            'sample_type',
            'extraction_method',
            'sample_cleanup',
            'analysis_instrumentation',
            'analysis_pah', 
            'analysis_alkanes',
            'analysis_phenols',
            'analysis_tph',
            'analysis_btex',
            'log_comments',
            Submit('submit', 'Submit', css_class='btn-success')
        )
    
    