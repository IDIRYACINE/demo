package Compilation.SimpleAutomata.Automata;

import Compilation.SimpleAutomata.Automata.AutomataStates.FirstMatchState;
import Compilation.SimpleAutomata.Automata.AutomataStates.IMatchingState;
import Compilation.SimpleAutomata.Automata.AutomataStates.SecondMatchState;
import Compilation.SimpleAutomata.Automata.AutomataStates.ThirdMatchState;

public class AutuomataLanguageValidator implements IAutomataLanguageValidator{
    private IMatchingState state;
    private final IMatchingState[] statesAvaillable = {new FirstMatchState(),new SecondMatchState(),new ThirdMatchState()};
    

    public AutuomataLanguageValidator(){
        state = statesAvaillable[0];
    }

    @Override
    public boolean WordBelongToLanguage(String word){
        int characterIndex = 0 , stateIndex = 0;
        
        while (characterIndex < word.length()){
            try {
                state.matchCharacter(word.charAt(characterIndex));
                stateIndex = state.getNextStateIndex();
            } catch (Exception e) {
                e.printStackTrace();
                return false;
            }
            state = statesAvaillable[stateIndex];
            characterIndex++;
        }
        return true;
    }

    @Override
    public void ReDefineAlphabet(Character firstAlphabet , Character secondAlphabet){
        for (IMatchingState iMatchingState : statesAvaillable) {
            iMatchingState.setNewAlphabet(firstAlphabet, secondAlphabet);
        }
    }
    
}
