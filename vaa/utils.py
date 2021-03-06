from random import choice

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def trunc(text, size):
    return text[:size] + (" ..." if len(text) > size else "")


def max_d(dataset, q_pks):
    z = zipvalues(dataset, q_pks, True)
    print z
    return sum([[4,3,2,3,4,settings.INDECISION_PARAMETER][q-1]*i for q, i in z.values()])


def zipvalues(dataset, question_pks, d=False):
    dataset = dict(dataset)
    print dataset, question_pks
    if not d:
        return [(int(dataset.get('q_'+str(i), 6)), int(dataset.get('i_'+str(i), 3))) for i in question_pks]    
    else:
        return dict([('q_%s' % i, (int(dataset.get('q_'+str(i), 6)), int(dataset.get('i_'+str(i), 3)))) for i in question_pks])

class render_with:
    def __init__(self, template):
        self.template = template

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            context = f(*args, **kwargs)
            return render(args[0], self.template, context)
        return wrapped

def randstring(length, charset="abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ01234567890.!"):
    return "".join([choice(charset) for x in xrange(length)])

