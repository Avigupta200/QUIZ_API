import requests
import time
from termcolor import colored

api_key = "YOUR_API_KEY"  


headers = {
    "Authorization": f"Bearer {api_key}"
}



url = "https://quizapi.io/api/v1/quizzes"

params = {
    "limit": 5
}

response = requests.get(url, headers=headers, params=params)

data = response.json()


quizzes = data["data"] 
for index, quiz in enumerate(quizzes):
    print(f"{colored(index + 1, 'yellow')}. {colored(quiz['title'], 'yellow')}")
    print("ID:", quiz["id"])
    print("Category:", quiz["category"])
    print("Difficulty:", quiz["difficulty"])
    print("\n****************************************\n")

choice = int(input("Enter the number of the quiz you want to take: ")) - 1

selected_quiz = quizzes[choice] 
print("\n****************************************\n")
print(f"You selected: {colored(selected_quiz['title'], 'red', attrs=['underline'])} (ID: {selected_quiz['id']})\n")


quiz_id = selected_quiz["id"]

url = "https://quizapi.io/api/v1/questions"

params = {
    "quiz_id": quiz_id,
    "include_answers": "true"
}

response = requests.get(url, headers=headers, params=params)

data = response.json()

questions = data["data"]

for index, question in enumerate(questions):
    print(f"Question {index + 1}: {colored(question['text'], color ='green', attrs=['bold'])}\n") #que
    print(f"Type: {question['type']}\n") # mcq
    print(f"Difficulty: {question['difficulty']}\n") # diff
    for i in range(len(question['answers'])):
        print(colored(f"Option {i + 1}: {question['answers'][i]['text']}", color='blue', attrs=['bold']))

        #took user input for ans
    user_answer = int(input("Enter your answer: "))
        
    selected_answer = question['answers'][user_answer - 1]
    if selected_answer['isCorrect']:
        print(colored("Correct!\n", color='green'))
    else:
        print(colored("Incorrect!\n", color='red'))
        
    print (f"Explanation: {question['explanation']}\n")
    print("\n****************************************\n") 
    time.sleep(2)  # Add a delay of 2 seconds between questions
 