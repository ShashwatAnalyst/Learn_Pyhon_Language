class IncorrectOptionNumber(Exception):
    pass
import random

questions = [
    ["Who is Shah Rukh Khan", "Driver", "Actor", "Plumber", "WWE Wrestler", 2, 100000],
    ["Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Earth", 1, 200000],
    ["What is the capital of France?", "Rome", "Paris", "Berlin", "Madrid", 2, 300000],
    ["Who wrote 'Hamlet'?", "William Shakespeare", "Charles Dickens", "George Orwell", "J.K. Rowling", 1, 400000],
    ["What is the largest mammal on Earth?", "Blue Whale", "Elephant", "Giraffe", "Hippopotamus", 1, 500000],
    ["Which language is primarily spoken in Brazil?", "French", "Portuguese", "English", "Spanish", 2, 600000],
    ["What is the chemical symbol for water?", "CO2", "H2O", "NaCl", "O2", 2, 700000],
    ["Who is the founder of Microsoft?", "Elon Musk", "Bill Gates", "Steve Jobs", "Mark Zuckerberg", 2, 800000],
    ["Which continent is the Sahara Desert located in?", "Africa", "Australia", "Asia", "South America", 1, 900000],
    ["What is the fastest land animal?", "Cheetah", "Tiger", "Horse", "Lion", 1, 1000000],
    ["Which ocean is the largest?", "Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", 1, 1100000],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", "Vincent van Gogh", 1, 1200000],
    ["What gas do plants absorb from the atmosphere?", "Carbon Dioxide", "Nitrogen", "Oxygen", "Helium", 1, 1300000],
    ["Which organ pumps blood in the human body?", "Heart", "Lungs", "Brain", "Liver", 1, 1400000],
    ["Which is the smallest prime number?", "2", "1", "0", "3", 1, 1500000]
]



for question in questions:
    print(question[0])
    print("A.",question[1])
    print("B.",question[2])
    print("C.",question[3])
    print("D.",question[4])


    a = int(input("Enter Your Answer.press 1 for a, 2 for b, 3 for c, 4 for d: "))
    if a == question[5]:
        print("Correct Answer")
        print(f"You Won ${question[6]}")
        
    else:
        print("Your Answer is Incorrect")
        print("Better Luck Next Time!")
        break


    
    

        
    
    
    
    

        


    