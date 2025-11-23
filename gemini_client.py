from google import genai

client = genai.Client()


def get_gemini_response(prompt):
    """Generates content using the Gemini model."""
    if not client:
        return "Gemini client is not initialized. Please check your API key."

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"


if __name__ == "__main__":
    # Test the function
    print(get_gemini_response("Explain how AI works in a few words"))
