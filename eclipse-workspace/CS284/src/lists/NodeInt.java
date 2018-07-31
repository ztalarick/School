package lists;

public class NodeInt {
	private Integer data;
	private NodeInt next;
	
	NodeInt(Integer data){
		this.data = data;
		this.next = null;
	}
	
	NodeInt(Integer data, NodeInt next){
		this.data = data;
		this.next = next;
	}
	
	public NodeInt bump(){
		if(this.next == null) {
			return new NodeInt(this.data + 1);
		}
		return new NodeInt(this.data + 1, next.bump());
	}
	public NodeInt filterEven() {//THIS DOESN'T WORK
		if(this.next == null) {
			return new NodeInt(this.data);
		}
		if(this.data % 2 == 0) {
			return new NodeInt(this.data, next.filterEven());
		} else {
			return next.filterEven();
		}
	}
	
	public boolean allPositive() {
		boolean result = true;
		NodeInt current = this;
		while(current != null) {
			if(this.data < 0) {
				result = false;
			}
			current = current.next;
		}
		return result;
	}
	
	public int size() {
		int count = 1;
		NodeInt current = this;
		while(current.next != null) {
			count++;
			current = current.next;
		}
		return count;
	}
	
	public String toString() {
		if(next == null) {
			return data.toString();
		}else {
			return data.toString() + ", " + next.toString();
		}
	}
	
	public static void main(String[] args) {
		NodeInt n1 = new NodeInt(3);
		NodeInt n2 = new NodeInt(1, n1);
		NodeInt n3 = new NodeInt(2, n2);
		NodeInt n4 = new NodeInt(6, n3);
		
		
		System.out.println(n4.filterEven());
	}
}
