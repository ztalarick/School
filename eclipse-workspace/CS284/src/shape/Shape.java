package shape;

public abstract class Shape implements HasColor{
protected String color;
	Shape(String c){
		color = c;
	}
	public String getColor(){
		return color;
	}
	public void setColor(String c) {
		color = c;
	}
	public String toString() {
		return "Color: " +  color;
	}
	//must be implemented by subclasses
	public abstract double area();
}
