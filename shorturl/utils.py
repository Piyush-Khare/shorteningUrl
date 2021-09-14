from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_UR_CHARS", 7)
AVAILABLE_CHARS = ascii_letters + digits

def create_random(chars = AVAILABLE_CHARS):
    return "".join([choice(chars) for _ in range(SIZE)])



def create_short_url(model_instance):
    randomCode = create_random()
    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=randomCode):
        return create_short_url(model_instance)

    return randomCode