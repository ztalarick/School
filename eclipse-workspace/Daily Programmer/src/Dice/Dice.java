package Dice;
import java.util.Scanner;
import java.lang.Math;

public class Dice {
	public static void main(String[] args) {
		System.out.println("Enter # of dice: ");
		Scanner reader = new Scanner(System.in);
		int dice = reader.nextInt();
		reader.close();
		
		System.out.println("Enter # of sides: ");
		Scanner reader2 = new Scanner(System.in);
		int sides = reader2.nextInt();
		reader2.close();
		
		int sum = 0;
		while(dice != 0) {
			sum += Math.random() * sides + 1;
			dice -= 1;
		}
		System.out.println(sum);
	}

}
