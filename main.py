import requests


api_key = "qa_sk_d4147817fd1747e9753d7b8983e3120e7acb362e"


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
    print(f"{index + 1}. {quiz['title']}")
    print("ID:", quiz["id"])
    print("Category:", quiz["category"])
    print("Difficulty:", quiz["difficulty"])
    print("\n****************************************\n")

choice = int(input("Enter the number of the quiz you want to take: ")) - 1

selected_quiz = quizzes[choice]
print("\n****************************************\n")
print(f"You selected: {selected_quiz['title']} (ID: {selected_quiz['id']})")


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
    print(f"Question {index + 1}: {question['text']}\n")
    print(f"Type: {question['type']}\n")
    print(f"Difficulty: {question['difficulty']}\n")
    print(f"Answers: {question['answers']}\n")
    print(f"Explanation: {question['explanation']}\n")
    print("\n****************************************\n")
 