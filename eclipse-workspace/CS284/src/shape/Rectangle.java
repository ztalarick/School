package shape;
/**
 * The class Rectangle models rectangles.
 * @author Zach
 *
 */

public class Rectangle extends Shape {
	//initiating variables
	private double base;
	private double height;
	
	public static int num_of_Rect;
	
	Rectangle(double b, double h, String c){
		super(c);
		height = h;
		base = b;
		
		
		num_of_Rect ++; //calculates the number of rectangles created
	}
	
	//Getters
	public double getBase() {
		return base;
	}
	
	public double getHeight() {
		return height;
	}
	
	//Setters
	/**
	 * Sets the base of a rectangle.
	 * @param b Base of a rectangle.
	 */
	public void setBase(double b) {
		base = b;
	}
	/**
	 * Sets the height of a rectangle.
	 * @param h Height of a rectangle.
	 */
	public void setHeight(double h) {
		height = h;
	}

	
	//methods
	public double area() {
		return base * height;
	}
	
	public String toString() {
		return "Base: " + base + " Height: " + height + " Color: " + color;
	}
	
	public Pair<Double,Double> getBaseHeight() {
		return new Pair<Double, Double>(base, height);
	}
}
