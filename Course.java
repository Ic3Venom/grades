import java.io.Serializable;

public class Course implements Serializable
{

	private String name;
	private boolean weighted;
	
    public Course(String name, boolean weighted )
    {
    	this.name = name;
    	this.weighted = weighted;
    	
    	
    }
}