package stacks;

import java.util.EmptyStackException;

public class StackLL<E> implements StackInt<E> {
	private class Node<E>{
		private E data;
		private Node<E> next;
		
		Node(E item){
			data = item;
			this.next = next;
		}
		Node(E item, Node<E> next){
			data = item;
			this.next = next;
		}
	}
	private Node<E> topmost;
	private int size;
	
	StackLL(){
		topmost = null;
		size = 0;
	}
	
	public E push(E item) {
		topmost = new Node<E>(item, topmost);
		size++;
		return item;
	}
	
	public E top() {
		if(this.empty()) {
			throw new EmptyStackException();
		}
		return topmost.data;
	}
	
	public E pop() {		
		E result = this.top();
		topmost = topmost.next;
		size--;
		return result;
	}
	
	public boolean empty() {
		return topmost == null;
	}

}
