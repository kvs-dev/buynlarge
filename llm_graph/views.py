from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .graph_manager import process_question
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@permission_classes([AllowAny])
def ask_question(request):
    """
    Endpoint to process questions about the store database.
    Expects a JSON body with a "question" field.
    """
    try:
        question = request.data.get('question')
        if not question:
            return Response(
                {'error': 'Question field is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Process the question and get all steps
        steps = process_question(question)
        
        # Extract the final answer from the last step
        final_answer = None
        for step in steps:
            if 'answer' in step:
                final_answer = step['answer']
        
        return Response({
            'answer': final_answer,
            'steps': steps  # Include all steps for debugging/transparency
        })
        
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) 