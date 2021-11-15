package Compilation.SimpleAutomata.Automata.AutomataStates;

public interface IMatchingState {
    public void matchCharacter(Character alphabet) throws Exception ;
    public int getNextStateIndex();
    public void setNewAlphabet(Character firstAlphabet , Character secondAlphabet);
}
