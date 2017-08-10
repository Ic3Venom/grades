/*
    Created by Julian Meyn
*/

import java.util.*;

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
				help();
    			break;
    		case "new":
    		case "n":
    			break;
    		case "check":
    		case "c":
    			break;
    		case "all":
    		case "a":
    			break;
    		case "q":
     		case "quit":
    			break;
			default:
				System.out.println("Unknown command \"" + userInput + "\". Try again.");
			}
    	} while (!userInput.toLowerCase().equals("q") && !userInput.toLowerCase().equals("quit"));
    	sc.close();
		
		ArrayList<Course> courses = new ArrayList<Course>();
		courses.add(new Course("CS38", true));
		
		try
		{
			courses.get(0).addCategory("Tests", 50);
			courses.get(0).add("Tests", "Test1", (double)100);
			courses.get(0).write();
			Course.readAll();
		}
		catch (Exception e)
		{
			System.out.print(e.getMessage());
			System.exit(1);
		}

		System.out.println("Terminating program.");
		System.exit(0);
	
	}

    private static void help()
    {
		System.out.println("<grades help page>"
			+ "\nAvailable commands:"
			+ "\n\t'help' ('h'): shows the help page"
			+ "\n\t'new [arg]' ('n [a]'): creates a new: [C]course/[]category/[G]grade"
			+ "\n\t'all'  ('a'): shows all grades from all courses"
			+ "\n\t'quit' ('q'): quits the program");
	}
	
}

