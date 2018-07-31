package TallyProgram;

public class TallyProgram {
	public static String tally(String str1) {
		int a = 0;
		int b = 0;
		int c = 0;
		int d = 0;
		int e = 0;
		//convert to char array
		char chars[] = str1.toCharArray();
		//iterate over char array
		for(int i = 0; i < chars.length; i++) {
			char j = str1.charAt(i);
			//check if character is uppercase then subtract
			if(Character.isUpperCase(j)) {
				if(j == 'A') {
					a -= 1;
				}
				if(j == 'B') {
					b -= 1;
				}
				if(j == 'C') {
					c -= 1;
				}
				if(j == 'D') {
					d -= 1;
				}
				if(j == 'E') {
					e -= 1;
				}
			} //check if char is lowercase then add 
			if(Character.isLowerCase(j)) {
				if(j == 'a') {
					a += 1;
				}
				if(j == 'b') {
					b += 1;
				}
				if(j == 'c') {
					c += 1;
				}
				if(j == 'd') {
					d += 1;
				}
				if(j == 'e') {
					e += 1;
				}
			}
		}
		return "a: " + a + ", b:" + b + ", c: " + c + ", d: " + d + ", e: "+ e; 
	}
	public static void main(String args[]) {
		System.out.println(tally("EbAAdbBEaBaaBBdAccbeebaec"));
	}
}
