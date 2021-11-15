package Compilation.SimpleAutomata.Automata;

public interface IAutomataLanguageValidator {
    public boolean WordBelongToLanguage(String word);
    public void ReDefineAlphabet(Character firstAlphabet , Character secondAlphabet);
}
