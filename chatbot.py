import os

os.environ['PYDEVD_WARN_SLOW_RESOLVE_TIMEOUT'] = '1.0'

import tkinter as tk
from tkinter import scrolledtext, filedialog
from nltk.chat.util import Chat, reflections
import pyttsx3
import speech_recognition as sr
import threading

# Define some patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello! How can I help you?', 'Hey there! If you have any queries about KRISHNA CHAITANYA INSTITUTE OF TECHNOLOGY & SCIENCES feel free to ask.', 'Hi! How can I assist you?']),
    (r'how are you?', ['I am good, thank you!', 'I\'m doing well, thanks for asking.']),
    (r'Branches?|Departments?', ['The branches present in our college are CSE, ECE, EEE, AI&ML, and for diploma are DECE, DEEE, DCME.']),
    (r'Admission requirements?', ['Our college admission requirements are original certificates of 10th and Intermediate marklist and TC\'s.']),
    (r'Campus facilities?', ['Libraries, Laboratories, recreational areas, Hostel, Sports, Transportation.']),
    (r'Internships?', ['Our college provides internships from various companies like 1stop, AICTE, Naresh technologies.']),
    (r'Hostel Facilities?', ['There is hostel facility within college; there are two options available AC and NON AC.']),
    (r'Career services?', ['Our college conducts NSS and GSS service programs. Our college visits old age homes and government schools apart from this service program.']),
    (r'Cultural events?', ['Our college conducts cultural events twice a month. Technical fests are organized by students as student coordinators.']),
    (r'Graduation rate?', ['The graduation rate of our college is 100 percent.']),
    (r'Extracurricular opportunities?', ['Our college conducts technical fests to give students a chance to explore their talent and ideas. We have MOU with various companies like Neolysi Technologies Pvt.Ltd., NAVICA COMMUNICATIONS PVT.LTD. to provide training for students.']),
    (r'Support services from professors?', ['Our professors are always available to the students to provide support services like mentorship in which we enquire students about their problems and give suggestions to all of them.']),
    (r'Achievements?', ['Our college was awarded as the best college in AP.']),
    (r'Class strength?', ['The average class strength is 70 members.']),
    (r'how interactive are the classes?', ['Our college provides excellent interactive classes with excellent faculty.']),
    (r'Principal?', ['KITS college principal is Dr.V KRISHNA REDDY.']),
    (r'CSE HOD?|cse hod?|', ['KITS CSE HOD is DR.J V ANIL KUMAR']),
    (r'ECE HOD?|ece hod?', ['KITS ECE HOD is DR.A RANGANAYAKULU']),
    (r'AIML HOD?|aiml hod?|ai hod?|AI HOD?', ['KITS AIML/AI HOD is MS. AMRUTHAVALLI']),
    (r'Chairman?', ['KITS college director is Sri.A.RamBABU sir.']),
    (r'Secretary?', ['KITS college Secretary is Sri.A.KRISHNA CHAITANYA SIR.']),
    (r'Safety and security measures?', ['We can ensure that safety and security measures are the top priorities of our college. We always inform parents when students are going for outing.']),
    (r'Fee structure?', ['Visit the Official Website https://kits-anna.com/ to inquire about attendance, including tuition, fees, and living expenses.']),
    (r'Job opportunities?', ['Yes, we provide work-study programs campus job opportunities.']),
    (r'Extracurricular activities?', ['Our college provides English club activities, sports, cultural activities like dance, singing, roleplay, anchoring, stand-up comedy.']),
    (r'Nutritional meals?', ['Our college provides nutritious meals including items like idli, upma, rice dishes, chapati, dosa, etc.']),
    (r'Name?|College Name?', ['Our college name is KITS-MARKAPUR.']),
    (r'College location?', ['Our college address is DEVARAJUGATTU-MARKAPUR.']),
    (r'College founded?', ['Our college was founded in 2008.']),
    (r'Mission and vision?', ['Our Mission: To impart affordable and quality education in order to meet the needs of industries and achieve excellence in teaching-learning process. Our Vision: To contribute for sustainable development of the nation through achieving excellence in technical education and research while facilitating transformation of students into responsible citizens and competent professionals.']),
    (r'Academic programs?', ['Our college provides various academic programs like CSI (computer society of india) and various webinars from industrial experts.']),
    (r'Students enrolled?', ['About 50 percent of Diploma students are enrolled in our college. About 80 percent of B.Tech students are enrolled in our college.']),
    (r'Transportation facilities?', ['Our college provides bus transportation from various villages.']),
    (r'College facilities description?', ['The hostel atmosphere is very conducive for the students to concentrate on studies. Each room is also well ventilated with basic amenities such as a cot, study table, chair, and a rack. Ragging-free environment, monitored study hours, special classes for weak students, special coaching for students having backlogs, state-of-the-art kitchen and spacious dining area have been provided in all the hostels.']),
    (r'Students percent?', ['About 80 percent of students live on campus.']),
    (r'Academic qualifications?', ['Our college admission requirements are 70 percent in SSC and Intermediate.']),
    (r'Contact details?', ['Our college contact details are: Phone number: 9652010001, Email: contact@kits-markapur.com']),
    (r'blocks?', ['Our college contains 3 blocks, 1 block is for Hostel, 2nd block is for Mess, 3rd block is for College.']),
    (r'Floors?', ['Our college contains 4 floors.']),
    (r'Campus building?', ['Our college has a vibrant learning environment nestled on sprawling 5-acre land. The campus is adorned with three distinct buildings each showcasing modern architecture and state of the art facilities. The main academic building houses spacious and well-equipped classrooms, lecture halls, and laboratories.']),
    (r'Admission rate?', ['Our college retention rate of students from freshman to sophomore year is increasing year by year.']),
    (r'Ragging free?', ['Yes, our college is ragging free with the best students.']),
    (r'Distinctive features?', ['Our college is Co-Education institute, which is a unique feature about our college.']),
    (r'Quality of education?', ['Excellent.']),
    (r'Teaching methods?', ['Highly effective.']),
    (r'Infrastructure?', ['Excellent.']),
    (r'Sufficient academic needs?', ['Yes, they are more than sufficient.']),
    (r'Support and guidance?', ['Yes, our college provides satisfied support and guidance to students from management.']),
    (r'Technology?', ['Our college technology is amazing that we provide facilities like E-classes and Auditorium.']),
    (r'Rating of faculty?', ['Excellent.']),
    (r'Opportunities?', ['Yes, our college provides various opportunities like extracurricular activities, job opportunities, internships.']),
    (r'Placement services?', ['Our college provides various placement services like job training, webinars, and job opportunities from various companies.']),
    (r'College efforts?', ['Our college puts great efforts for students growth.']),
    (r'Rating?', ['On the scale of 1 to 10, our college can be at 9.']),
    (r'help', ['You can ask me questions about the college, such as "admission requirements", "campus facilities", "hostel facilities", "cultural events", "job opportunities", "extracurricular activities", etc.']),
    (r'quit', ['Bye, take care!', 'Goodbye, see you soon.']),
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

# Function to handle user input and display response
def send_message(event=None):
    user_input = entry.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot.respond(user_input)
    if response:
        chat_history.insert(tk.END, "Bot: " + response + "\n\n")
        tts_engine.say(response)
        tts_engine.runAndWait()
    else:
        chat_history.insert(tk.END, "Bot: I'm sorry, I didn't understand that. Please try asking something else or type 'help' for assistance.\n\n")
        tts_engine.say("I'm sorry, I didn't understand that. Please try asking something else or type 'help' for assistance.")
        tts_engine.runAndWait()
    chat_history.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Function to clear the chat history
def clear_chat():
    chat_history.config(state=tk.NORMAL)
    chat_history.delete('1.0', tk.END)
    chat_history.config(state=tk.DISABLED)

# Function to save the chat history to a text file
def save_chat():
    chat_file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if chat_file:
        chat_file.write(chat_history.get("1.0", tk.END))
        chat_file.close()

# Function to handle voice input and output
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            tts_engine.say("Please say something")
            tts_engine.runAndWait()
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            entry.insert(0, user_input)
            send_message()
        except sr.UnknownValueError:
            tts_engine.say("Sorry, I could not understand the audio")
            tts_engine.runAndWait()
        except sr.RequestError as e:
            tts_engine.say(f"Could not request results; {e}")
            tts_engine.runAndWait()

# Create a tkinter window
window = tk.Tk()
window.title("KITS Chatbot")

# Add a heading
heading = tk.Label(window, text="KITS CHATBOT\nYou can chat with me", font=("Helvetica", 16), pady=10)
heading.pack()

# Create a chat history text widget with a scrollbar
chat_frame = tk.Frame(window)
chat_history = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, font=("Helvetica", 12))
chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(chat_frame, command=chat_history.yview)
chat_history.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for user input
entry_frame = tk.Frame(window)
entry = tk.Entry(entry_frame, width=50, font=("Helvetica", 12))
entry.bind("<Return>", send_message)
entry.pack(side=tk.LEFT, padx=10)

# Create a send button
send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)
entry_frame.pack(pady=10)

# Create a clear button
clear_button = tk.Button(window, text="Clear Chat", command=clear_chat)
clear_button.pack(pady=5)

# Create a save button
save_button = tk.Button(window, text="Save Chat", command=save_chat)
save_button.pack(pady=5)

# Create a voice input button
voice_button = tk.Button(window, text="Voice Input", command=lambda: threading.Thread(target=voice_input).start())
voice_button.pack(pady=5)

# Run the tkinter main loop
window.mainloop()
