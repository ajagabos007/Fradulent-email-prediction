from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from scam_report.data_processing import email, load_email, predict_spam
from scam_report.forms import UploadFileForm
import os
from scam_report.filers import handle_uploaded_file


def upload_file(request):
    file_dir = os.path.dirname(__file__)  # get current directory
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            file_path = handle_uploaded_file(request.FILES['file'])
            data = load_email(file_path)
            result = predict_spam(data)
            # return JsonResponse({'data':file_path})
            return render(request, 'scam_report/upload.html', {'result': result, 'is_fraudulent':result[0], 'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'scam_report/upload.html', {'form': form})

def predictEmailScam(request):
    """
    List all code snippets, or create a new snippet.
    """
    # http://127.0.0.1:8000/static/scam-report/file1.eml

    if request.method == 'GET':
        file_path = request.GET.get('file_path')
        module_dir = os.path.dirname(__file__)  # get current directory
        email_file = request.get('http://127.0.0.1:8000/static/scam-report/file1.eml')
        file_path = os.path.join(module_dir, 'email_messages/1.emil')
        with open("email_messages/1.eml", 'rb') as f:
            data = email.parser.BytesParser(policy=email.policy.default).parse(f)
        # data = load_email("file:///home/ajagabos007/Downloads/spam-predictor-model/api_scam_report/scam_report/email_messages/1.eml")
        result = predict_spam(data)
        print(result)
        # data = bytes(email_file.text, 'utf-8')
        # response = predict_spam("http://127.0.0.1:8000/static/scam-report/file1.eml")
        return JsonResponse({'data': "data loaded"})

    elif request.method == 'POST':
        
        return JsonResponse({'text': 'POST REQUEST RECEIVED'})
