from django.shortcuts import redirect, render,get_object_or_404
from django.http import JsonResponse
import google.generativeai as genai
from dotenv import load_dotenv

# Create your views here.
def homepage(request):
    return render(request, 'app/home.html')

def chatpage(request,*args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(request, 'app/login.html')
    context={}
    return render(request, 'app/chatwithfriends.html',context)


def chatbot(request):
    load_dotenv()
    genai.configure(api_key=("apikey"))

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"""You're a dedicated and enthusiastic elementary school teacher with over 10 years of experience in engaging students in creative learning experiences. You excel at simplifying complex concepts and making lessons fun and interactive for kids while fostering a positive and inclusive classroom environment. 
        The response should not contain any "*" or "#" or any highlighted headings like * **Definition:**. 
        Please avoid overloading with extra information and do not include any additional introductory text or characters like "*" or "#", etc.
        Please use simple terms for in-depth explanation."""
    )

    history = []

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(user_input)
        model_response = response.text

        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "bot", "parts": [model_response]})

        return JsonResponse({"response": model_response})

    
    return render(request, 'app/chatwithai.html')


def technews(request):
    return render(request, 'app/technews.html')


def mentor(request):
    load_dotenv()
    genai.configure(api_key=("apikey"))

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"""You're a dedicated and enthusiastic college teacher with over 10 years of experience in engaging students in creative learning experiences. You excel at simplifying complex concepts and making lessons fun and interactive for kids while fostering a positive and inclusive classroom environment. 
        The response should not contain any "*" or "#" or any highlighted headings like * **Definition:**. 
        Please avoid overloading with extra information and do not include any additional introductory text or characters like "*" or "#", etc.
        Please use simple terms for in-depth explanation."""
    )

    history = []

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(user_input)
        model_response = response.text

        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "mentor", "parts": [model_response]})

        return JsonResponse({"response": model_response})

    
    return render(request, 'app/mentor.html')

def about(request):
    return render(request, 'app/About.html')
