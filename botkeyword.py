import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- Step 1: Securely Load Your Google AI API Key ---
load_dotenv()
# We now look for a GOOGLE_API_KEY in the .env file
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("Google AI API key not found. Please set it in your .env file as GOOGLE_API_KEY=your_key_here")

# Configure the library with your key
genai.configure(api_key=google_api_key)


def extract_keywords_from_text(text_content):
    """
    Uses the Google Gemini API to extract legal keywords and terminology.
    """
    # --- Step 2: Configure and Communicate with the Gemini API ---
    model = genai.GenerativeModel('gemini-1.5-flash-latest') # Or 'gemini-pro'

    prompt = f"""
    As a specialized legal assistant bot for 'LegalSathi', your task is to analyze the following legal document text. 
    Your goal is to identify and extract all significant keywords and legal terminology.
    
    Focus on:
    - Legal Principles (e.g., Res Judicata, Caveat Emptor)
    - Key Parties or Roles (e.g., Plaintiff, Defendant, Appellant)
    - Legal Actions or Procedures (e.g., Litigation, Arbitration, Injunction)
    - Important Acts, Sections, or Articles
    - Core concepts and definitions
    
    Please return the results as a clean, comma-separated list.

    --- DOCUMENT TEXT ---
    {text_content}
    --- END OF DOCUMENT ---

    Extracted Keywords and Terminologies:
    """
    try:
        # Make the API call to Google Gemini
        response = model.generate_content(prompt)
        # Extract the text from the response object
        return response.text.strip()
    except Exception as e:
        return f"An error occurred with the Google Gemini API: {e}"


def main():
    """
    Main function to run the bot on a directory of files.
    """
    database_folder = r"D:\LegalSathi\legalSatthi\Database"

    if not os.path.isdir(database_folder):
        print(f"❌ ERROR: The specified folder does not exist: {database_folder}")
        return

    print(f"📁 Scanning for .txt files in: {database_folder}\n")
    
    for filename in os.listdir(database_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(database_folder, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    document_text = file.read()
                
                if not document_text.strip():
                    print(f"📄 Skipping empty file: {filename}\n")
                    continue

                print(f"--- Processing File: {filename} ---")
                print("🤖 Contacting Google AI for keyword extraction...")

                keywords = extract_keywords_from_text(document_text)

                print("✅ Extracted Legal Keywords & Terminology:")
                print(keywords)
                print(f"--- Finished with {filename} ---\n")

            except Exception as e:
                print(f"❌ An error occurred while processing {filename}: {e}\n")


if __name__ == "__main__":
    main()