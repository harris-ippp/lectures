import pandas as pd, numpy as np

def table(request):

    df = pd.DataFrame(np.random.randn(10, 5), 
                      columns = list("abcde"))

    table = df.to_html()

    return HttpResponse(table)
