import java.io.*;
import java.util.*;

public class Course implements Serializable
{
	private String name;
	private boolean weighted;
	private HashMap<String, Object> categories = new HashMap<String, Object>();

    public Course(String name, boolean weighted)
    {
    	this.name = name;
		this.weighted = weighted;
	}

	public void add(String key)
	{
		categories.put(key, null);
	}

    public static void write(Course c)
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
		catch (IOException e)
		{
			System.out.print(e.getMessage());
			System.exit(1);
		}
		catch (Exception e) {
			System.out.print(e.getMessage());
			System.exit(1);
		}
	}

	public static void readAll()
	{

		try {
		
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
		catch (IOException e)
		{
			System.out.print(e.getMessage());
			System.exit(1);
		}
		catch(ClassNotFoundException e)
		{
			System.out.print(e.getMessage());
			System.exit(1);
		}
		catch (Exception e) {
			System.out.print(e.getMessage());
			System.exit(1);
		}
	}
	
	public String getName()
	{
		return name;
	}
	
	public boolean getWeighted()
	{
		return weighted;
	}
	
	public void setName(String name)
	{
		this.name = name;
	}
	
	public void setWeighted(boolean weighted)
	{
		this.weighted = weighted;
	}

	public String toString()
	{
		return "Course Name: " + name
			+ "\nWeighted? " + weighted
			+ "\nCategories: " + categories;
	}
}