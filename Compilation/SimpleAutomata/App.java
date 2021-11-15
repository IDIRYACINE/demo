package Compilation.SimpleAutomata;
import java.util.Scanner;

import Compilation.SimpleAutomata.Automata.AutuomataLanguageValidator; 

public class App
{
	public static void main(String[] args) {
		EnterAwordAndTestAgainstAutomata();
	}

	public static void EnterAwordAndTestAgainstAutomata(){
		System.out.print("Enter a word : ");
		Scanner scanner = new Scanner(System.in);
		String word = scanner.next();
		AutuomataLanguageValidator language = new AutuomataLanguageValidator();
		if (language.WordBelongToLanguage(word)){
			System.out.println("First Alphabet : 0" );
			System.out.println("Second Alphabet : 1" );
			System.out.println("Language Regex : 0*11(0*|11)*" );
			System.out.println("Belong to Automata " + word );
		}
		scanner.close();
	}
    
}


