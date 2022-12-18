import json
from finitAutomata import FiniteAutomata

def load_data(json_file):
    with open(json_file) as file:
        data = json.load(file)
    return data



def construct_automata(json_data):
    try:
        a = FiniteAutomata(
            json_data["states"],
            json_data["alphabet"],
            json_data["initial_state"],
            json_data["final_states"],
            json_data["transitions"]
        )
        return a
    except ValueError as ex:
        print(ex)



def load_automata():

    a = load_data(r"C:\Users\adria\OneDrive\Desktop\year3\CS\LFTC\Laboratory\Lab3\Finit.json")
    automata = construct_automata(a)
    return (automata)


if __name__ == "__main__":

    automata = load_automata()
    print(automata)
