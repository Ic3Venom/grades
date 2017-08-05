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

	public String getName(){return name;}
	public boolean getWeighted(){return weighted;}
	public void setName(String name){this.name = name;}
	public void setWeighted(boolean weighted){this.weighted = weighted;}
}