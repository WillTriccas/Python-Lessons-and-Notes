def SentenceMaker(phrase):
    capitalized = phrase.capitalize()
    Question_words = ("how", "what", "who", "why,", "when", "where")
    if phrase.startswith(Question_words):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

#  print(SentenceMaker("how are you big boi"))             this is just to test the above function works, not included in final code

FinalSentence = []

while True:
    user_input = input("write something here: ")
    if user_input == "/end":
        break
    else:
        FinalSentence.append(SentenceMaker(user_input))

print(" ".join(FinalSentence))