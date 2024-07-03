import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from PyPDF2 import PdfReader
import io
from pdf_summary import settings

openai.api_key = settings.API_KEY

class SummarizePDF(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print(request.data)
        
        if 'file' not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        pdf_file = request.FILES['file']
        try:
            pdf_reader = PdfReader(pdf_file)
            page_text = ""

            if len(pdf_reader.pages) > 0:
                page = pdf_reader.pages[0]
                page_text = page.extract_text()
            
            client = openai.OpenAI(api_key=KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": 'You summarize text'
                     },
                    {
                        "role" : "user",
                        "content" : f"Summarize the following text:\n\n{page_text}"
                     },
                    ],
            )

            summary = response.choices[0].message.content
            return Response({"summary": summary})
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
