package lists;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Arrays;

public class MyList<E> {
	// Data fields
	static int INITIAL_CAPACITY = 0;
	private E[] data;
	private int size;
	int capacity;
	
	//Constructor
	MyList(){
		this.data = (E[]) new Object[INITIAL_CAPACITY];
		size = 0;
		capacity = INITIAL_CAPACITY;
	}
	
	//Methods
	public boolean add(E item) {
		if (size == data.length) {
			throw new ArrayIndexOutOfBoundsException();
		} 
		data[size] = item;
		size ++;
		return true;
	}
	public void add(int index, E item) {
		if (index < 0 || index > size) {
			throw new ArrayIndexOutOfBoundsException();
		}
		if(size == data.length) {
			throw new IllegalArgumentException();
		}
		for(int i = size; i > index; i--) {
			data[i] = data[i - 1];
		}
		data[index] = item;
	}
	public String toString() {
		return Arrays.toString(data);
	}
	

	
	public static void main(String[] args){
		MyList<Integer> is = new MyList<Integer>();
		is.add(1);
		is.add(2);
		is.add(3);
		is.add(4);
		is.add(5);

		
		System.out.println(is);
	}
}
