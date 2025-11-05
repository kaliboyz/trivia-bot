import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# ---- CONFIG ----
CHAT_URL = "https://abababab.chatovod.com/"
BOT_NAME = "ciliciaGame"
QUESTION_INTERVAL = 30  # seconds to wait for answers
NUM_QUESTIONS = 100  # Number of questions per round

# Quiz questions (edit as needed)
quiz = [
    {"q": "What is the capital of Armenia?", "a": "Yerevan"},
    {"q": "What is the official language of Armenia?", "a": "Armenian"},
    {"q": "Which continent is Armenia in?", "a": "Asia"},
    {"q": "What color is the Armenian flag?", "a": "Red, Blue, Orange"},
    {"q": "Armenia is famous for which ancient monastery?", "a": "Geghard"},
    {"q": "Who is the national hero of Armenia?", "a": "David of Sasun"},
    {"q": "What is the currency of Armenia?", "a": "Dram"},
    {"q": "What is the largest city in Armenia?", "a": "Yerevan"},
    {"q": "What is the national dish of Armenia?", "a": "Khorovats"},
    {"q": "Which mountain is a symbol of Armenia?", "a": "Mount Ararat"},
    {"q": "What is Armenia's national animal?", "a": "Golden Eagle"},
    {"q": "When did Armenia gain independence from the Soviet Union?", "a": "1991"},
    {"q": "What is the Armenian word for 'hello'?", "a": "Barev"},
    {"q": "Which river is the longest in Armenia?", "a": "Aras River"},
    {"q": "What is the Armenian name for the Armenian Genocide Memorial?", "a": "Tsitsernakaberd"},
    {"q": "Which ancient civilization is Armenia often linked with?", "a": "Urartu"},
    {"q": "What is the traditional Armenian dance called?", "a": "Duduk"},
    {"q": "Which Armenian church is UNESCO-listed?", "a": "Etchmiadzin Cathedral"},
    {"q": "What is the traditional Armenian bread called?", "a": "Lavash"},
    {"q": "What is the most famous Armenian wine?", "a": "Ararat Brandy"},
    {"q": "Which famous poet is considered the national poet of Armenia?", "a": "Hovhannes Shiraz"},
    {"q": "What is the population of Armenia?", "a": "Approximately 3 million"},
    {"q": "What is Armenia's national sport?", "a": "Wrestling"},
    {"q": "In which year was Armenia first mentioned in ancient records?", "a": "6th century BC"},
    {"q": "What was the name of the first Armenian kingdom?", "a": "Urartu"},
    {"q": "Which Armenian architect designed the Yerevan Opera House?", "a": "Alexander Tamanian"},
    {"q": "Which Armenian leader was a key figure in the Armenian independence movement?", "a": "Levon Shant"},
    {"q": "Which major event took place in Armenia in 1915?", "a": "The Armenian Genocide"},
    {"q": "What is the name of the famous lake in Armenia?", "a": "Lake Sevan"},
    {"q": "What is the name of the famous Armenian fortress located on a hill?", "a": "Khor Virap"},
    {"q": "What is the primary religion in Armenia?", "a": "Christianity (Armenian Apostolic Church)"},
    {"q": "What is Armenia's second largest city?", "a": "Gyumri"},
    {"q": "Which war was fought between Armenia and Azerbaijan in the 1990s?", "a": "Nagorno-Karabakh War"},
    {"q": "What is the traditional Armenian musical instrument?", "a": "Duduk"},
    {"q": "Who was the first president of independent Armenia?", "a": "Levon Ter-Petrosyan"},
    {"q": "What year was the Armenian Apostolic Church established?", "a": "301 AD"},
    {"q": "Which Armenian city is known for its thermal springs?", "a": "Jermuk"},
    {"q": "Which Armenian composer wrote the famous opera 'Arshak II'?", "a": "Aram Khachaturian"},
    {"q": "What is the name of the Armenian language alphabet?", "a": "Armenian alphabet"},
    {"q": "What is the most important holiday in Armenia?", "a": "Easter (Vardavar)"},
    {"q": "What is the tallest mountain in Armenia?", "a": "Mount Aragats"},
    {"q": "What year did Armenia become part of the Soviet Union?", "a": "1920"},
    {"q": "What famous battle was fought near the city of Sardarapat?", "a": "Battle of Sardarapat"},
    {"q": "Which famous Armenian writer was awarded the Nobel Prize in Literature?", "a": "Shirvanzade"},
    {"q": "What is the name of the Armenian ancient script inventor?", "a": "Mesrop Mashtots"},
    {"q": "Which famous church is located in the town of Noravank?", "a": "Noravank Monastery"},
    {"q": "What is the Armenian traditional New Year's celebration called?", "a": "Shnorhali"},
    {"q": "What is the Armenian national flower?", "a": "The Edelweiss"},
    {"q": "What are the main exports of Armenia?", "a": "Minerals, textiles, and brandy"},
    {"q": "Which famous Armenian singer is known for his song 'Qele Qele'?", "a": "Charles Aznavour"},
    {"q": "Which ancient Armenian city is now part of Turkey?", "a": "Ani"},
    {"q": "Which historical figure is credited with converting Armenia to Christianity?", "a": "St. Gregory the Illuminator"},
    {"q": "What is the main ethnic group in Armenia?", "a": "Armenians"},
    {"q": "What is Armenia's largest export partner?", "a": "Russia"},
    {"q": "What Armenian instrument is commonly used in traditional music?", "a": "Duduk"},
    {"q": "Which Armenian city is home to the world's largest collection of medieval manuscripts?", "a": "Yerevan"},
    {"q": "What year did Armenia adopt its first constitution?", "a": "1995"},
    {"q": "Which famous Armenian actor starred in the movie 'The Promise'?", "a": "Oscar Isaac"},
    {"q": "What is the highest point in Armenia?", "a": "Mount Aragats"},
    {"q": "What is the national park in Armenia famous for its wildlife?", "a": "Khosrov Forest State Reserve"},
    {"q": "What is the most famous Armenian dessert?", "a": "Baklava"},
    {"q": "What is the name of the Armenian parliament building?", "a": "National Assembly of Armenia"},
    {"q": "What is the name of the river that flows through Yerevan?", "a": "Hrazdan River"},
    {"q": "What type of climate does Armenia have?", "a": "Continental climate"},
    {"q": "What is the name of the main airport in Yerevan?", "a": "Zvartnots International Airport"},
    {"q": "Which famous Armenian singer is known as the 'Queen of Armenian Pop'?", "a": "Sirusho"},
    {"q": "Which Armenian kingdom was famous for its royal dynasty?", "a": "Kingdom of Urartu"},
    {"q": "What is the national monument of Armenia?", "a": "Victory Park"},
    {"q": "Which ancient fortress is located near Yerevan?", "a": "Erebuni Fortress"},
    {"q": "What was the capital of ancient Armenia?", "a": "Tigranakert"},
    {"q": "Who was the first king of Armenia?", "a": "King Artaxias I"},
    {"q": "What is the Armenian symbol of peace?", "a": "The dove"},
    {"q": "Which Armenian scientist is known for developing the first Armenian encyclopedia?", "a": "Hovhannes Shirlian"},
    {"q": "What is the national motto of Armenia?", "a": "Unity, Happiness, and Freedom"},
    {"q": "What is Armenia's national animal?", "a": "Golden Eagle"},
    {"q": "What is the most famous tourist destination in Armenia?", "a": "Lake Sevan"},
    {"q": "What is the name of the ancient Armenian kingdom located in present-day Turkey?", "a": "Cilicia"},
    {"q": "What is the traditional Armenian greeting?", "a": "Barev dzez"},
    {"q": "What year did Armenia officially declare its independence?", "a": "1991"},
    {"q": "What is the symbol of Armenia's flag?", "a": "The tricolor: Red, Blue, and Orange"},
    {"q": "Who is considered the father of the Armenian alphabet?", "a": "Mesrop Mashtots"},
    {"q": "What is the most famous ancient Armenian site?", "a": "Temple of Garni"},
    {"q": "Which famous Armenian composer wrote the music for Spartacus?", "a": "Aram Khachaturian"},
]

# ---- FUNCTIONS ----
def find_input_box(driver):
    """Find the chat textarea element"""
    try:
        box = driver.find_element("css selector", "textarea")
        return box
    except Exception:
        raise NoSuchElementException("Chat textarea not found. Check selector.")

def find_messages(driver):
    """Return a list of message elements"""
    try:
        return driver.find_elements("css selector", "div.message")
    except Exception:
        return []

def send_message(driver, text):
    """Send a message in chat"""
    try:
        box = find_input_box(driver)
        box.click()
        box.clear()
        box.send_keys(text)
        box.send_keys(Keys.ENTER)
        print("SENT:", text)
    except Exception as e:
        print("Failed to send message:", e)

# ---- MAIN ----
def start_quiz(driver):
    """Start the quiz loop, ask 100 questions and wait for answers"""
    for q_index in range(NUM_QUESTIONS):  # Loop for 100 questions
        q = quiz[q_index % len(quiz)]  # Cycle through the quiz list
        send_message(driver, "Question: " + q["q"])
        correct_answer = q["a"].lower().strip()

        answered = False
        start = time.time()
        while time.time() - start < QUESTION_INTERVAL:
            try:
                msgs = find_messages(driver)
                if not msgs:
                    time.sleep(1)
                    continue
                last_text = msgs[-1].text.strip().lower()
                if last_text == correct_answer:
                    send_message(driver, f"Correct answer by user! 🎉 Answer: {q['a']}")
                    answered = True
                    break
            except Exception:
                pass
            time.sleep(1)

        if not answered:
            send_message(driver, f"Time's up! Answer: {q['a']}")

        time.sleep(2)  # short pause between questions

def main():
    driver = webdriver.Chrome()  # Make sure chromedriver.exe is in same folder
    driver.maximize_window()
    driver.get(CHAT_URL)

    print("Browser opened. Please log in manually and solve CAPTCHA if any.")
    input("After you finish login and can type in chat, press Enter here to start the bot...")

    # Test input box
    try:
        find_input_box(driver)
    except NoSuchElementException as e:
        print("ERROR: cannot find chat textarea after login. Check selector.")
        print(e)
        driver.quit()
        return

    # Greet
    send_message(driver, f"Hello! I am {BOT_NAME}! Trivia game will start automatically every {QUESTION_INTERVAL}s.")

    # Start quiz in a loop
    while True:
        start_quiz(driver)  # Start the quiz with 100 questions
        send_message(driver, "Trivia game finished! Thanks for playing! 👍")
        print("Game complete. You can close the browser.")
        print("Preparing for next round...")
        
        # Add a pause before restarting
        time.sleep(5)  # 5 seconds delay between rounds (adjust as needed)

if __name__ == "__main__":
    main()
