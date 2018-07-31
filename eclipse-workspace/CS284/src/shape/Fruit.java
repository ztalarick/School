package shape;

public class Fruit implements HasColor{
	private String fruitColor;
	
	Fruit(String color){
		fruitColor = color;
	}
	public String getColor() {
		return fruitColor;
	}
	public void setColor(String fruitColor) {
		this.fruitColor = fruitColor;
	}
}
