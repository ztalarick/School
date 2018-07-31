package stacks;

public class PalindromeChecker {
	private String str;
	private StackLL<Character> charStack;
	
	PalindromeChecker(String str){
		this.str = str;
		charStack = new StackLL<Character>();
		fillStack(str);
	}
	private void fillStack(String str) {
		for(int i = 0; i < str.length(); i++) {
			charStack.push(str.charAt(i));
		}
	}
	private String buildReverse() {
		StringBuilder s = new StringBuilder();
		while(!charStack.empty()) {
			s.append(charStack.pop());
		}
		return s.toString();
	}
	
	public boolean isPalindrome() {
	return str.equalsIgnoreCase(this.buildReverse());
	}
}
