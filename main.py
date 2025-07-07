from my_io.speech_to_text import listen
from my_io.text_to_speech import speak
from my_brain.basic_brain import generate_response

def main():
    print("🤖 Assistant started. Speak something...")
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        response = generate_response(user_input)
        speak(response)

if __name__ == "__main__":
    main()
