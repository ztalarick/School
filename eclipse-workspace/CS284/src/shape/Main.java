package shape;

import java.util.Arrays;

public class Main {
	public static void printArea(Shape r) {
		System.out.println(r.area());
	}
	public static String[] colors(HasColor[] ss) {
		String[] res = new String[ss.length];
		int i = 0;
		for (HasColor s:ss) {
			res[i] = s.getColor();
			i++;
		}
		return res;
	}
	
	public static void main(String[] args) {
		Rectangle r = new Rectangle(4, 5, "red");
		circle c = new circle(3, "blue");
		System.out.println(r);
		
		Shape[] rs = new Shape[3];
		rs[0] = r;
		rs[1] = new Rectangle(2.3, 4.3, "Orange");
		rs[2] = c;
		
		
		for (Shape aShape:rs) {
			System.out.println(aShape.area());
		}
		
		System.out.println(Arrays.toString(colors(rs)));
		
		Fruit[] fs = new Fruit[3];
		fs[0] = new Fruit("red");
		fs[1] = new Fruit("blue");
		fs[2] = new Fruit("yellow");
		System.out.println(Arrays.toString(colors(fs)));
	}

}
