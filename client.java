/*
    Created by Julian Meyn
*/

import java.util.Scanner;
import java.io.*;

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
    			showAllGrades();
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
    	} while (!userInput.toLowerCase().equals("q") && !userInput.toLowerCase().equals("quit"));
    	
    	sc.close();
    	
    	
    	
    	System.exit(0);
    }
    
    private static void showAllGrades()
    {
    	
    	return;
    }
    
    private static void help()
    {
    	
    	
    }

    private static void change(Course c)
    {
    	try
        {
            //"fo" stands for FileOutput, "oo' stands for ObjectOutput
            FileOutputStream foStream = new FileOutputStream(new File("fileOutput.txt"));
            ObjectOutputStream ooStream = new ObjectOutputStream( foStream );

            // Write object to file
            ooStream.writeObject( c );

            ooStream.close();
            foStream.close();

        }
        catch (FileNotFoundException e) 
        {
            
            System.out.println("File not found");
                
        } 
        catch (IOException e) 
        {
            
            System.out.println("Error initializing stream");
        
        }
	}
	
	private static void read()
	{
		try
		{
			//"fi" stands for FileInput, "oi" stands for ObjectInput
			FileInputStream fiStream = new FileInputStream(new File("fileOutput.txt"));
			ObjectInputStream oiStream = new ObjectInputStream( fiStream );

			while( fiStream.available() > 0 )
			{
					
				Course buffer = (Course) oiStream.readObject();
				System.out.println( buffer.toString() );
				
			}
				
			oiStream.close();
			fiStream.close();
		}
		catch (FileNotFoundException e) 
        {
            
            System.out.println("File not found");
                
        } 
        catch (IOException e) 
        {
            
            System.out.println("Error initializing stream");
        
        } 
        catch (ClassNotFoundException e) {
        
            e.printStackTrace();

        }
	}
    
    private static void classExists()
    {
    	
    }
    
    private static void categoryExists()
    {
    	
    }
    
}

