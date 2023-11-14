import g4f

# GPTManager use gpt4free. Link: https://github.com/xtekky/gpt4free
#
# If you want use this ChatGPT manager in your code, you can include this file.
#
# INCLUDE:
# Add this file in directory with your project and in including file type:
#
# from gpt import GPTManager
# ^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# USING:
# Into the ChatGPT you can send message and get the answer using GPTManager().send()
# This function return type string-answer.
#
# EXAMPLE:
# str = "What is the area of the Australia?"
# output = GPTManager().send(str)
# print(output)
#
# OR:
# print(GPTManager().send("What is the area of the Australia?"))



class GPTManager:
    context = ""
    globalContext = ""

    def __init__(self):
        self.globalContext = "C этого момента пиши только кириллицей."

    def send(self, data):
        response = g4f.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": (self.globalContext + " Контекст: " + self.context + "\nОтветь на это в контексте: " + data)}],
            stream = False
        )
        output = ""
        self.context += data + "\n"
        for msg in response:
            output += msg
        self.context += output + "\n"
        return output