package shape;

public class circle extends Shape {
	private double radius;
	
	circle (double r, String c){
		super(c);
		radius = r;
	}
	public double getRadius() {
		return radius;
	}
	public void setRadius(double r) {
		radius = r;
	}

	public String toString() {
		return "Radius: " + radius +  " Color: " + color;
	}
	
	public double area() {
		return Math.PI * radius * radius;
	}
}
