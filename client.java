/*
    Created by Julian Meyn
*/

import java.util.Scanner;

public class client
{
	
    public static void main(String args[])
    {
    	String userInput;
    	Scanner sc = new Scanner(System.in);
    	
    	
    	do
    	{
    		System.out.print("What do you want to do? (type \'help\' for more info) > ");
    		userInput = sc.nextLine();
    		
    		switch(userInput.toLowerCase())
    		{
    		case "help":
    		case "h":
    			System.out.println("help!");
    			break;
    		case "new":
    		case "n":
    			System.out.println("new!");
    			break;
    		case "check":
    		case "c":
    			System.out.println("check!");
    			break;
    		case "all":
    		case "a":
    			System.out.println("all!");
    			break;
    		case "q":
    		case "quit":
    			break;
			default:
				System.out.println("Unknown command \"" + userInput + "\". Try again.");
    		}
    	} while (!userInput.equals('q'));
    	
    	sc.close();
    	System.exit(0);
    }

}