from django.shortcuts import render
import requests
from django.http import JsonResponse
from decouple import config
# Home view


def index(request):
    return render(request, 'index.html')  # This will use templates/index.html

# Chatroom view


def chatroom(request):
    # This will use templates/chatroom.html
    return render(request, 'chatroom.html')

# API call to Hugging Face for chatbot responses


def get_chatbot_response(request):
    # Get user message from request
    user_message = request.GET.get('message', '')

    if user_message:
        # Hugging Face API URL (using BlenderBot)
        url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        headers = {
            "Authorization": f"Bearer {config('HUGGINGFACE_API_KEY')}"
        }

        try:
            # Send request to Hugging Face API
            response = requests.post(url, headers=headers, json={
                                     "inputs": user_message})
            # Log response status
            print(f"Response Status: {response.status_code}")
            print(f"Response JSON: {response.json()}")  # Log response content
            # Check if the response is successful (HTTP status code 200)
            if response.status_code == 200:
                # Extract the chatbot's reply from the response
                chatbot_reply = response.json()[0]['generated_text']
            else:
                # Handle cases where the response is not successful
                chatbot_reply = "Sorry, I couldn't understand that. Please try again."
        except requests.exceptions.RequestException as e:
            # Handle exceptions (e.g., network issues)
            chatbot_reply = f"Error: {str(e)}"

        # Return the response as a JSON object
        return JsonResponse({"reply": chatbot_reply})

    # In case there's no message
    # return JsonResponse({"reply": "No message received."})
