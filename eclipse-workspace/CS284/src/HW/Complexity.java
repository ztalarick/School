package HW;

/**
 * I pledge my honor that I have abided by the Stevens Honor System. ztalaric
 * @author Zachary Talarick
 * @date 2/11/18
 */
public class Complexity {
	/**
	 * O(n)
	 */
	public void method0(int n) {
		int count = 0;
		for(int i = 0; i < n; i++) {
			count++;
		}
		System.out.println("Total Operations: " + count);
	}
	/**
	 * O(n^2)
	 */
	public void method1(int n) {
		int count = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				count++;
			}
		}
		System.out.println("Total Operations: " + count);
	}
	/**
	 * O(n^3)
	 */
	public void method2(int n) {
		int count = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				for(int k = 0; k < n; k++) {
				count++;
				}
			}
		}
		System.out.println("Total Operations: " + count);		
	}
	/** 
	 * O(log(n))
	 */
	public void method3(int n) {
		int count = 0;
		for(int i = 1; i < n; i *= 2) {
			count++;
		}
		System.out.println("Total Operations: " + count);
	}
	/** 
	 * O(n*log(n))
	 */
	public void method4(int n) {
		int count = 0; //number of operations
		for(int i = 0; i < n; i++) {
			for(int j = 1; j < n; j *= 2) {
				count++;
			}
		}
		System.out.println("Total Operations: " + count);
	}
	/**
	 * O(log log n)
	 */
	public void method5(int n) {
		int count = 0; //number of operations
		double d = (double) n;
		for(int i = 0; i < d; i++) {
			d = Math.sqrt(d);
			count++;
		}
		System.out.println("Total Operations: " + count);
	}
	/** Bonus (use recursion)
	 * O(2^n)
	 */
	int count6 = 0;
	public void method6(int n) {
		if(n <= 1) {
			return;
		}else {
			count6++;
			System.out.println(count6);
			this.method6(n - 1); 
			this.method6(n - 2);
		}
	}
	public static void main(String[] args) {
		Complexity c = new Complexity();
		c.method4(100);
	}
}
