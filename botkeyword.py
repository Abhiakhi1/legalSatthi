# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# # --- Step 1: Securely Load Your Google AI API Key ---
# load_dotenv()
# # We now look for a GOOGLE_API_KEY in the .env file
# google_api_key = os.getenv("GOOGLE_API_KEY")

# if not google_api_key:
#     raise ValueError("Google AI API key not found. Please set it in your .env file as GOOGLE_API_KEY=your_key_here")

# # Configure the library with your key
# genai.configure(api_key=google_api_key)


# def extract_keywords_from_text(text_content):
#     """
#     Uses the Google Gemini API to extract legal keywords and terminology.
#     """
#     # --- Step 2: Configure and Communicate with the Gemini API ---
#     model = genai.GenerativeModel('gemini-1.5-flash-latest') # Or 'gemini-pro'

#     prompt = f"""
#     As a specialized legal assistant bot for 'LegalSathi', your task is to analyze the following legal document text. 
#     Your goal is to identify and extract all significant keywords and legal terminology.
    
#     Focus on:
#     - Legal Principles (e.g., Res Judicata, Caveat Emptor)
#     - Key Parties or Roles (e.g., Plaintiff, Defendant, Appellant)
#     - Legal Actions or Procedures (e.g., Litigation, Arbitration, Injunction)
#     - Important Acts, Sections, or Articles
#     - Core concepts and definitions
    
#     Please return the results as a clean, comma-separated list.

#     --- DOCUMENT TEXT ---
#     {text_content}
#     --- END OF DOCUMENT ---

#     Extracted Keywords and Terminologies:
#     """
#     try:
#         # Make the API call to Google Gemini
#         response = model.generate_content(prompt)
#         # Extract the text from the response object
#         return response.text.strip()
#     except Exception as e:
#         return f"An error occurred with the Google Gemini API: {e}"


# def main():
#     """
#     Main function to run the bot on a directory of files.
#     """
#     database_folder = r"D:\LegalSathi\legalSatthi\Database"

#     if not os.path.isdir(database_folder):
#         print(f"❌ ERROR: The specified folder does not exist: {database_folder}")
#         return

#     print(f"📁 Scanning for .txt files in: {database_folder}\n")
    
#     for filename in os.listdir(database_folder):
#         if filename.endswith(".txt"):
#             file_path = os.path.join(database_folder, filename)
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     document_text = file.read()
                
#                 if not document_text.strip():
#                     print(f"📄 Skipping empty file: {filename}\n")
#                     continue

#                 print(f"--- Processing File: {filename} ---")
#                 print("🤖 Contacting Google AI for keyword extraction...")

#                 keywords = extract_keywords_from_text(document_text)

#                 print("✅ Extracted Legal Keywords & Terminology:")
#                 print(keywords)
#                 print(f"--- Finished with {filename} ---\n")

#             except Exception as e:
#                 print(f"❌ An error occurred while processing {filename}: {e}\n")


# if __name__ == "__main__":
#     main()

# import os
# import json
# import google.generativeai as genai
# from dotenv import load_dotenv

# # --- Step 1: Securely Load Your Google AI API Key ---
# load_dotenv()
# # We now look for a GOOGLE_API_KEY in the .env file
# google_api_key = os.getenv("GOOGLE_API_KEY")

# if not google_api_key:
#     raise ValueError("Google AI API key not found. Please set it in your .env file as GOOGLE_API_KEY=your_key_here")

# # Configure the library with your key
# genai.configure(api_key=google_api_key)


# def extract_structured_legal_info(text_content):
#     """
#     Uses the Google Gemini API to extract legal keywords, terminologies, and entities.
#     Returns a Python dictionary parsed from the API's JSON response.
#     """
#     # --- Step 2: Configure and Communicate with the Gemini API ---
#     model = genai.GenerativeModel('gemini-1.5-flash-latest')

#     prompt = f"""
#     As a specialized legal assistant bot for 'LegalSathi', your task is to analyze the following legal document text.
#     Your goal is to identify and extract all significant keywords, legal terminology, and legal entities.

#     Please categorize your findings into three distinct lists:
#     1.  **keywords**: General important topics or subjects (e.g., "breach of contract", "intellectual property", "negligence").
#     2.  **legal_terminologies**: Specific legal terms, phrases, or Latin maxims (e.g., "Res Judicata", "Caveat Emptor", "writ of mandamus").
#     3.  **legal_entities**: Named parties, courts, acts, sections, or specific roles (e.g., "Plaintiff", "Defendant", "Supreme Court of India", "Indian Penal Code, Section 302").

#     Return the result as a single, valid JSON object with the keys "keywords", "legal_terminologies", and "legal_entities". Do not include any text before or after the JSON object.

#     --- DOCUMENT TEXT ---
#     {text_content}
#     --- END OF DOCUMENT ---

#     JSON Output:
#     """
#     try:
#         # Make the API call to Google Gemini
#         response = model.generate_content(prompt)
#         # Clean up the response to ensure it's valid JSON
#         # Models can sometimes wrap the JSON in markdown backticks
#         cleaned_response_text = response.text.strip().replace("```json", "").replace("```", "").strip()
        
#         # Parse the JSON string into a Python dictionary
#         return json.loads(cleaned_response_text)
    
#     except json.JSONDecodeError as e:
#         print(f"❌ JSON Parsing Error: {e}")
#         print(f"   Raw response from API was: {response.text}")
#         return None # Return None if parsing fails
#     except Exception as e:
#         print(f"An error occurred with the Google Gemini API: {e}")
#         return None


# def main():
#     """
#     Main function to run the bot on a directory of files and save results to a JSON file.
#     """
#     database_folder = r"D:\LegalSathi\legalSatthi\Dataset"
#     output_json_file = "legal_extractions.json"
#     all_extractions = [] # A list to hold all the extracted data dictionaries

#     if not os.path.isdir(database_folder):
#         print(f"❌ ERROR: The specified folder does not exist: {database_folder}")
#         return

#     print(f"📁 Scanning for .txt files in: {database_folder}\n")
    
#     for filename in os.listdir(database_folder):
#         if filename.endswith(".txt"):
#             file_path = os.path.join(database_folder, filename)
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     document_text = file.read()
                
#                 if not document_text.strip():
#                     print(f"📄 Skipping empty file: {filename}\n")
#                     continue

#                 print(f"--- Processing File: {filename} ---")
#                 print("🤖 Contacting Google AI for structured data extraction...")

#                 extracted_data = extract_structured_legal_info(document_text)

#                 # Proceed only if the API call and JSON parsing were successful
#                 if extracted_data:
#                     # Add the source filename to the extracted data
#                     extracted_data["source_file"] = filename
#                     all_extractions.append(extracted_data)
#                     print(f"✅ Successfully extracted and structured data from {filename}.")
#                 else:
#                     print(f"⚠️ Failed to extract data for {filename}.")
                
#                 print(f"--- Finished with {filename} ---\n")

#             except Exception as e:
#                 print(f"❌ An unexpected error occurred while processing {filename}: {e}\n")
    
#     # After processing all files, write the aggregated data to a JSON file
#     if all_extractions:
#         try:
#             with open(output_json_file, 'w', encoding='utf-8') as f:
#                 json.dump(all_extractions, f, indent=4)
#             print(f"🎉 Success! All data has been written to {output_json_file}")
#         except Exception as e:
#             print(f"❌ Error writing to JSON file: {e}")
#     else:
#         print("No data was extracted from any files.")


# if __name__ == "__main__":
#     main()
