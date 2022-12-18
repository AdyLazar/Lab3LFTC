

class FiniteAutomata:
    def __init__(self, states, alphabet, initial_state, final_states, transitions):

        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions



    def __str__(self):
        ret_value = "States: [" + ", ".join(self.states) + "]\n"
        ret_value += "Alphabet: [" + ", ".join(self.alphabet) + "]\n"
        ret_value += "Initial state: " + self.initial_state + "\n"
        ret_value += "Final states: [" + ", ".join(self.final_states) + "]\n"
        ret_value += "Transitions: \n"

        for t in self.transitions:
            ret_value += t + ":\n"
            for transition in self.transitions[t]:
                ret_value += "\t" + transition + " -> "
                ret_value += "".join(self.transitions[t][transition])
                ret_value += "\n"
        return ret_value
