from django.forms import ModelForm
from .models import Comments

class CommentsForm(ModelForm): #forms.ModelForm  
    class Meta:
        model = Comments
        exclude=["post"]
        labels={
            "user_name":"Your Name",
            'user_email':"Your Email",
            'text':'Your Comment'
        }
        
        '''error_messages = {
            'user_name': {
                'required': 'Your Name is required. Please fill it out.',
            },
            'user_email': {
                'required': 'Your Email is required. Please fill it out.',
            },
            'text': {
                'required': 'Your Comment is required. Please fill it out.',
            },
        }'''