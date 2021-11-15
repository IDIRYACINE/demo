package Compilation.SimpleAutomata.Automata.AutomataStates;
public class ThirdMatchState implements IMatchingState{
    private Integer nextStateIndex;
    private Character FIRST_ALPHABET = '0';
    private Character SECOND_ALPHABET = '1';

    @Override
    public void matchCharacter(Character alphabet) throws Exception {
       if (alphabet.equals(FIRST_ALPHABET)){
            nextStateIndex = 2;
       }    
       else if (alphabet.equals(SECOND_ALPHABET)){
            nextStateIndex = 1 ;
       }
       else{
           throw new Exception("At third  state "+ alphabet + " doesn't belong to automata");
       }
        
    }

    @Override
    public int getNextStateIndex() {
        int nextState = nextStateIndex;
        nextStateIndex = null;
        return nextState;
    }

    @Override
    public void setNewAlphabet(Character firstAlphabet, Character secondAlphabet) {
        FIRST_ALPHABET = firstAlphabet;
        SECOND_ALPHABET = secondAlphabet;
        
    }
    
}
