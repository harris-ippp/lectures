from os.path import join
from django.conf import settings
import pandas as pd

def csv(request):

  baby = join(settings.STATIC_ROOT, 'myapp/baby.csv')
  df = pd.read_csv(baby)

  return HttpResponse(df.to_html())
