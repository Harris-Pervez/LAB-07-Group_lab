#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for mehtane?", "NH4"),
        ("What is the chemical symbol for sodium chloride?", "NaCl")
        # Add more questions as tuples (question, answer)
    ],"Math":[
        ("What is the sqare of 2","4"),
        ("What is the sqare of 3","9"),
        ("What is the sqare of 4","16")
              ],
    "English":[
        ("Which fov is used in present Tense","1st"),
        ("Which fov is used in Past Tense","2nd"),
        ("Which fov is used in Future Tense","1st")
        ]
}

hints = {
    "Science": [ questions["Science"][0][1],
                questions["Science"][1][1],
                questions["Science"][2][1]
        # Pair each question with a corresponding hint.
    ],
    "Math":[questions["Math"][0][1],
            questions["Math"][1][1],
            questions["Math"][2][1]
            ],
    "English":[questions["English"][0][1],
               questions["English"][1][1],
               questions["English"][2][1]]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #-----------------------
    # -
    if category in questions:
        L=len(questions[category])
        ran_no=random.randint(0,L-1)
        que=questions[category][ran_no][0]
        ans=questions[category][ran_no][1]
        return (que,ans) 
    raise NotImplementedError("This function is not implemented yet.")







    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #-----------------------
    return player_answer==correct_answer
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    # """
    # #------------------------
    # # Add your code here
    # #------------------------
    # if category in questions:
        
        
        
        
        
        
        
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    
    
    
    
    
    
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




