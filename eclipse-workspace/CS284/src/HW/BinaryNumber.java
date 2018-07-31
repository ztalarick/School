package HW;

public class BinaryNumber {
	//Data Fields
	private int data[];
	private boolean overflow;
	
	//Constructor
	/**
	 * Creates a binaryNumber and stores length 0s into an int array data.
	 * @param length - length of binary number
	 */
	BinaryNumber(int length){
		data = new int[length];
		for(int i = 0; i < length; i++) {
			data[i] = 0;
		}
	}
	/**
	 * Creates a BinaryNumber and stores every char in str into an int array data.
	 * @param str string representation of a BinaryNumber
	 */
	BinaryNumber(String str){
		data = new int[str.length()];
		for(int i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			data[i] = Character.getNumericValue(c);
		}
	}
	/**
	 * Gets the length of a BinaryNumber
	 * @return the length of the int array data that the BinaryNumber is stored in.
	 */
	public int getLength() {
		return data.length;
	}
	/**
	 * Gets the corresponding digit for a given index
	 * @param index The specified place to look for the digit
	 * @return the value stored in data at index
	 */
	public int getDigit(int index) {
		if(data.length > index) {
			return data[index];
		}else {
			System.out.println("Error, index out of range.");
			return -1;
		}
		
	}
	/**
	 * Converts a BinaryNumber to decimal
	 * @return result is iterated over every int in data.
	 */
	public int toDecimal() {
		int result = 0;
		for(int i = 0; i < data.length; i++) {
			result += java.lang.Math.pow(data[i] * 2, i); 
		}
		return result;
	}
	/**
	 * Adds amount 0s to the beginning of a BinaryNumber
	 * @param amount the amount of 0s to be added.
	 */
	public void shiftR(int amount) { 
		int[] newData = new int[data.length + amount];
		for(int i = 0; i < amount; i++) {
			newData[i] = 0;
		}
		for(int i = amount; i < data.length + amount; i++) {
		newData[i] = data[i - amount];	
		}
		data = newData;
	}
	/**
	 * Adds this and aBinaryNumber.
	 * @param aBinaryNumber a BinaryNumber to add to this
	 */
	public void add(BinaryNumber aBinaryNumber) {
		int x = aBinaryNumber.toDecimal();
		int y = this.toDecimal();
		int sum = 0;
		
		if (data.length != aBinaryNumber.getLength()) {
			System.out.println("The two numbers are not the same size");
		}else {
			sum = x + y;
			String strSum1 = Integer.toBinaryString(sum);
			String strSum = new StringBuilder(strSum1).reverse().toString();
			
			if(data.length == strSum.length()) {
			for(int i = 0; i < strSum.length(); i++) {
				char c = strSum.charAt(i);
				data[i] = Character.getNumericValue(c);
				}
			}else {
				int[] newData = new int[data.length + 1];
				for(int i = 0; i < strSum.length(); i++) {
					char c = strSum.charAt(i);
					newData[i] = Character.getNumericValue(c);
					}
				data = newData;
			}
			}
	
		}
	
	public void clearOverflow() {
		
	}
	/**
	 * String representation of BinaryNumber.
	 */
	public String toString() {
		//return java.util.Arrays.toString(data);
		String result = "";
		for(int i = 0; i < data.length; i++) {
			result += Integer.toString(data[i]);
		}
		return result;
	}
	
	public static void main(String[] args) {
		BinaryNumber b = new BinaryNumber("10110");
		
		System.out.println(b);
		b.add(new BinaryNumber("11101"));
		System.out.println(b);
	}
}
