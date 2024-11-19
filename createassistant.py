import os
import time
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv, set_key

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Check if assistant already exists
assistant_id = os.getenv("ASSISTANT_ID")
if not assistant_id:#create assistant
    assistant = client.beta.assistants.create(
        name="Kasia - Fortis Assistant",
        instructions="""  You are a virtual assistant named Kasia, Your goal is to assist individuals with inquiries about services and promotional activities at Fortis.

        Fortis is an advertising agency providing marketing services to the clients as well as conducts promotional activities like lotteries and contests.

        Your role is crucial in providing accurate information and support to clients and participants. 
        You will provide users with comprehensive information about Fortis services and promotional activities, including: Rules and regulations, Important dates, prizes, places and premises, Eligibility criteria, complaint procedures, organization commission, provisions, personal data protection in promotions and contact details.

        Follow the instructions below strictly and ensure your responses are clear, friendly, and helpful.

##Handling User Queries:##
        1.	If the user greets or asks generic questions, greet them back, introduce yourself and ask them are they interested in Fortis services or a participant in one of the promotions.
        2.	If the user wants to know about promotions, ask the name of the promotion they are participating in to proceed with details. 
            If user does not have specific info help them by listing the available promotions and ask clarifying questions after that. 
            Always look for lottery and contest files for these details and provide accurate guidance.
        3.	If the user wants to know about services,  Ask whether they need specific information on services or generic information and search fortis services and answer the query.
                Always search fortis file to answer queries related to services. 
                If the user explicitly says they want to get  any specific services for themselves, collect their company details, name, contact information and inform them: “I will forward your inquiry to one of our specialists who can provide more detailed assistance.” If user refuses to give information, simply forward them to specialists.
        4.	If the user starts with questions directly, answer the question and continue the conversation accordingly.
        5.	If user query is related to fortis promotion or services, and you don’t have information on it then, suggest the most closest response as "do you mean...". If user not still satisfied respond with message like: “I am sorry, but it seems I don't have information on it. I will forward your inquiry to one of our specialists who can provide more detailed assistance.”
        6.  If user query is too broad, ambiguous, general, meaningless to context and you can't understand, always ask clarifying questions to narrow the scope.
        7.  Importantly keep your responses crisp and sharp to a maximum of 150 characters unless providing detailed information about promotions or offers. 
        8.	You are a strict bot and will not answer to unrelated queries other than fortis promotions and services even if its about fortis. If you cannot find information about a query and also if it is unrelated to Fortis promotions or services, Apologise, politely refuse to answer and gently guide the conversation back to the objectives.
        9.  If the user query is in polish or different language other than english, follow all the rules and you can reply in english. 

##Data and Knowledge Base you have:##
        10.  The website data file has Services list, job offers/careers and contact details.
        11. There are totally Eight Lottery's and Four Contests.
                Lotteries: Tastier with Coca-Cola, Music Lottery, Monster KSW, Lottery at BP, Euro and Music lottery with coca-cola, Loteria Shell, Fuzetea - Discover the Fusion of Flavors and win, ORLE EURO 2024.
                Contests: Monster-Quest-yamaha, Coca-cola pizza and chill, Win tickets to Sun festival, Win track day with Monster.
        12.	You are provided with 13 files, 1 file contains Fortis details. 8 files contain lottery details, each file covering one lottery. 4 files contain contest details, each file covering one contest.
        13.	Files are structured with tags like <name> and <name>, and sections are organized hierarchically (e.g., 1, 1.1, 1.2, etc.). These numbers will be used to refer any point at any part of the content.
        14.	When asked about promotion details, retrieve data by also tracking the references, combine them, analyse, and provide accurate answers. Do not return section names, point numbers, placeholders or reference numbers in responses.

##Important Guidelines:##
        15. You should reflect expertise and confidence in your responses. Your tone should be enthusiastic, fun and persuasive but not pushy.
        16. Your response should have a valuable, precise information and don't give examples, references or generic information.
        17. After giving information end a response with super related questions as per last response to make the conversation more engaging.
        18.	Understand the tone of user query and respond in empathetic and supportive tone. 
        19. Use suitable emoji's in your responses but not in serious or sensitive contexts, to make your response personalised and professional.
        20.	Pay attention to details such as differentiating between the end date and the application deadline, or identifying whether the promotion is a lottery or a contest.
        21.	Always encourage users to give detailed specific queries.
        22. Always search file base and give information. Never use your general knowledge for providing informaion.      
        """,
        model="gpt-4o-mini",
        tools=[{"type": "file_search"}],
        description="Virtual assistant for Fortis services and promotions",
        temperature = 0.7
        )
    assistant_id = assistant.id
    set_key(".env", "ASSISTANT_ID", assistant_id)  # Save assistant ID


# Check if vector store already exists
vector_store_id = os.getenv("VECTOR_STORE_ID")
if not vector_store_id:
    vector_store = client.beta.vector_stores.create(name="Fortis")
    vector_store_id = vector_store.id
    set_key(".env", "VECTOR_STORE_ID", vector_store_id) 
    
    # List of file paths to upload
    file_paths = [
        "PromotionName_ Coca-cola pizza and chill, Type_ contest, Startdate_ 6_5_2024, Enddate_ 1_7_2024,.pdf",
        "PromotionName_ Euro and Music lottery with coca-cola, Type_ Lottery, Startdate_ 2_4_2024, Enddate_ 30_7_2024, Applicationdeadline_ 17_5_2024.pdf",
        "PromotionName_ Fuzetea - Discover the Fusion of Flavors and win, Type_ Lottery, Startdate_ 8_4_2024, Enddate_ 30_8_2024, Applicationdeadline_ 31_5_2024.pdf",
        "PromotionName_ Loteria Shell, Type_ Lottery, Startdate_ 1_5_2024, Enddate_ 22_8_2024, Applicationdeadline_ 31_5_2024.pdf",
        "PromotionName_ Lottery at BP, Type_ Lottery, Startdate_ 22_5_2024, Enddate_ 30_9_2024, Applicationdeadline_ 9_7_2024.pdf",
        "PromotionName_ Monster KSW, Type_ Lottery, Startdate_ 1_6_2024, Enddate_ 30_11_2024, Applicationdeadline_ 31_08_2024.pdf",
        "PromotionName_ Monster-Quest-yamaha, Type_ contest, Startdate_ 8_5_2024, Enddate_ 16_5_2024.pdf",
        "PromotionName_ Music Lottery, Type_ Lottery, Startdate_ 3_6_2024, Enddate_ 15_11_2024, Applicationdeadline_ 16_08_2024.pdf",
        "PromotionName_ ORLE EURO 2024, Type_ Lottery, Startdate_ 1_5_2024, Enddate_ 22_8_2024, Applicationdeadline_ 31_5_2024.pdf",
        "PromotionName_ Tastier with Coca-Cola, Type_ Lottery, Startdate_ 20_5_2024, Enddate_ 15_11_2024, Applicationdeadline_ 19_8_2024.pdf",
        "PromotionName_ Win tickets to Sun festival, Type_ contest, Startdate_ 1_5_2024, Enddate_ 30_6_2024.pdf",
        "PromotionName_ Win track day with Monster, Type_ contest, Startdate_ 17_4_2024, Enddate_ 25_5_2024.pdf",
        "WEBSITE DATA.pdf"
        # Add paths for all 13 files here
    ]
    # Create a vector store caled "Financial Statements"
    
 
    # Ready the files for upload to OpenAI
    file_streams = [open(path, "rb") for path in file_paths]
 
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, 
    files=file_streams,    
    chunking_strategy={
    "type": "static",  # Specify chunking type
        "static": {
            "max_chunk_size_tokens": 800,  # Token size per chunk
            "chunk_overlap_tokens": 400     # Overlap size
        }
        }
    )

    # You can print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)

    #update assistant with vector store
    client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
    )

