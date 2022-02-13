def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'sup'):
        return "Hey! How is it going?"

    if user_message in ('who are you', 'who are you?'):
        return 'I am BuildYourTripBot'

    return "I don't understand you"




