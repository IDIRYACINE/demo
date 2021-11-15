package Compilation.SimpleAutomata.Automata.AutomataStates;
public class SecondMatchState implements IMatchingState{
    private Integer nextStateIndex;
    private Character SECOND_ALPHABET = '1';

    @Override
    public void matchCharacter(Character alphabet)throws Exception  {
        if(alphabet.equals(SECOND_ALPHABET)){
            nextStateIndex = 2 ;
        }
        else {
            throw new Exception("At second state "+ alphabet + " doesn't belong to automata");
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
        SECOND_ALPHABET = secondAlphabet;
    }
    
}
