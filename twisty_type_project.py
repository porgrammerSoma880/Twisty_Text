#twisty_type_FINAL.py
import random
from typing import List, Optional      #to type hint the whole program in a proper way







def twisted_text_generate(text:str) -> Optional[str]:   
    """
    Function to generate a twisted version of input text by shuffling the words.

    Args:
        text (str): The input text to be twisted.

    Returns:
        str or None: A twisted version of the text, or None if input is invalid.
    """
    print(f"Normal text: {text}\n")           #user input printed on the terminal for a clearer UI
    splitted_text:List[str] = text.split()    #spitting the text to shuffle the words in it



    # Validate input text
    if len(splitted_text) == 0:  #if not input is entered at all, program will pause and inform the user to provide more words as the input
        print("Please enter some text.\n")
        return None
    elif len(splitted_text) < 2: #if one-word-input is provided, program will pause and inform the user to provide more words as the input
        print("One word can't be shuffled! Please provide more words.\n")
        return None



    # Shuffle text until the order changes
    twisted_list:List[str] = splitted_text[:]    #copy the spillted_list because we're gonna shuffle the list now using random
    while twisted_list == splitted_text:
        random.shuffle(twisted_list)




    twisted_text:str = " ".join(twisted_list)      #generate a twisted text at this point
    print(f"Twisted version: {twisted_text}\n")    #\n used for better-looking UI
    return twisted_text











def main():
    """
    Main function to repeatedly take user input and generate twisted text.
    """
    print("Welcome to the Twisted Text Generator!")
    print("Type 'exit' to quit the program.\n")



    while True:    #to run the program in infinity
        
        #taking the user input 
        normal_text : str=  input("Enter text to get a fun, twisted version (text must include more than one word!): ").strip()
        
        # Exit condition
        if normal_text.lower() == 'exit':
            print("Goodbye!")
            break

        # Generate twisted text
        twisted_text_generate(normal_text)






# Starting the program
if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"An error occured: {err}")


