import java.io.*;
import java.util.*;

public class Course implements Serializable
{
	public static final File FILE_NAME = new File("grades.txt");

	private String name;
	private boolean weighted;
	private HashMap<String, HashMap<String, Double>> categories = new HashMap<String, HashMap<String, Double>>();

    public Course(String name, boolean weighted)
    {
    	this.name = name;
		this.weighted = weighted;
	}

	public static void readAll() throws IOException, ClassNotFoundException
	{

		
		//"fi" stands for FileInput, "oi" stands for ObjectInput
		FileInputStream fiStream = new FileInputStream(FILE_NAME);
		ObjectInputStream oiStream = new ObjectInputStream( fiStream );

		while( fiStream.available() > 0 )
		{
				
			Course buffer = (Course) oiStream.readObject();
			System.out.println( buffer.toString() );
			
		}
			
		oiStream.close();
		fiStream.close();
		
	}

	public void write() throws IOException
    {
		//"fo" stands for FileOutput, "oo' stands for ObjectOutput
		FileOutputStream foStream = new FileOutputStream(FILE_NAME);
		ObjectOutputStream ooStream = new ObjectOutputStream(foStream);

		// Write object to file
		ooStream.writeObject( this );

		ooStream.close();
		foStream.close();
	}

	public void addCategory(String key)
	{
		categories.put(key, null);
	}

	public void addCategory(String key, double weight)
	{
		categories.put(key, );
		add(key, "Weight", weight);
	}

	public void add(String category, String key, Double grade)
	{
		categories.get(category).put(key, grade);
	}

	public Course read() throws IOException, ClassNotFoundException
	{

		//"fi" stands for FileInput, "oi" stands for ObjectInput
		FileInputStream fiStream = new FileInputStream(FILE_NAME);
		ObjectInputStream oiStream = new ObjectInputStream( fiStream );

		while( fiStream.available() > 0 )
		{

			Course buffer = (Course) oiStream.readObject();
			if (buffer.getName() == this.getName())
			{
				oiStream.close();
				fiStream.close();

				return buffer;
			}
		}

		oiStream.close();
		fiStream.close();

		return null;
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
			+ "\nWeighted? "   + weighted
			+ "\nCategories: " + categories;
	}
}