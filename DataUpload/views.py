import pandas as pd
from io import StringIO
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        df = pd.read_csv(myfile)
        request.session['df'] = df.to_json()
        return redirect('success')
    return render(request, 'home.html')

def success(request):
    df_html = request.session.get('df', None)
    if df_html:
        return render(request, 'index2.html')
        # return render(request, 'index2.html', {'df_html': df_html})
    return redirect('upload_file')

def preview(request):
    df = request.session.get('df', None)
    if df:
        df = pd.read_json(df)
        df_head = df.head()
        n_rows = df.shape[0]
        n_cols = df.shape[1]
        return render(request, 'index2.html', {'df_head':df_head.to_html(), 'n_rows':n_rows, 'n_cols':n_cols})
    return redirect('success')

def NullSum(request):
    df = request.session.get('df', None)
    if df:
        df = pd.read_json(df)
        df_null = df.isnull().sum()
        df_null = df_null.to_frame(name='Null_values_per_column').to_html()
        return render(request, 'index2.html', {'df_null':df_null})
    return redirect('success')