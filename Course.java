import java.io.*;
import java.util.*;

public class Course implements Serializable
{
	private String name;
	private boolean weighted;
	private List<List<String>> categories = new ArrayList<List<String>>();

    public Course(String name, boolean weighted)
    {
    	this.name = name;
		this.weighted = weighted;
	}

    public static void write(Course c) throws IOException
    {
		//"fo" stands for FileOutput, "oo' stands for ObjectOutput
		FileOutputStream foStream = new FileOutputStream(new File("fileOutput.txt"));
		ObjectOutputStream ooStream = new ObjectOutputStream( foStream );

		// Write object to file
		ooStream.writeObject( c );

		ooStream.close();
		foStream.close();
	}

	public void readCategories()
	{
		for(int i = 0; i < categories.size(); ++i)
		{
			List<String> subArray = categories.get(i);

			for(int j = 0; j < subArray.size(); ++j)
			{
				System.out.print(subArray.get(j)+"  ");
			}

			System.out.println("");
		}
	}
	public static void readCategory() throws IOException, ClassNotFoundException
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
	
	public boolean categoryExists(String name)
	{
		return categories.indexOf(name) >= 0 ? true : false;
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