# xbox_moments_voice.py

import elevenlabs

# Setup your Eleven Labs API key
API_KEY = "your_api_key"  # Replace with your Eleven Labs API key
elevenlabs.api_key = API_KEY

# Function to generate and play AI voice
def generate_ai_voice(text, voice_name="XboxMoments"):
    """
    Generates an AI voice for Xbox Moments using Eleven Labs and plays the audio.
    :param text: The text to convert into speech.
    :param voice_name: The name of the voice preset to use.
    """
    try:
        voice = elevenlabs.get_voice(voice_name)
        audio = voice.say(text)
        audio.save("xbox_moments.mp3")
        print(f"Voice generated: {text}")
        # Optionally, you could use a library like pydub to play the generated MP3
    except Exception as e:
        print(f"Error generating voice: {e}")

if __name__ == "__main__":
    welcome_message = "Welcome to Xbox Moments. How can I assist you today?"
    generate_ai_voice(welcome_message)

    # This script would continue interacting with the player based on inputs from the game
