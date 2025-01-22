from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import pipeline
from .models import ProcessedResult
from .serializers import ProcessedResultSerializer

class ProcessTextAPIView(APIView):

    def post(self, request):
        # Extract input text and task from the request payload
        text = request.data.get('text')
        task = request.data.get('task', 'summarization')  # Default task is summarization

        # Validate input
        if not text:
            return Response({"error": "Text field is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Initialize the LLM pipeline based on the requested task
            if task == 'summarization':
                model = pipeline('summarization')
                result = model(text)[0]['summary_text']
            elif task == 'sentiment':
                model = pipeline('sentiment-analysis')
                result = model(text)[0]
            else:
                return Response({"error": "Unsupported task."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:

            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save the processed result to the database
        processed_result = ProcessedResult.objects.create(
            input_text=text, 
            result=result, 
            task=task
        )
        serializer = ProcessedResultSerializer(processed_result)

       
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HistoryAPIView(APIView):
    def get(self, request):
        results = ProcessedResult.objects.all()
        serializer = ProcessedResultSerializer(results, many=True)
        return Response(serializer.data)
