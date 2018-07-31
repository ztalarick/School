package lists;

import shape.Pair;

public class MyListLL<E> {
	public class Node<E>{
		private E data;
		private Node<E> next;
		//Constructors
		Node(E data){
			this.data = data;
			this.next = null;
		}
		Node(E data, Node<E> next){
			this.data = data;
			this.next = next;
		}
	}
	private Node<E> head;
	private int size;
	
	MyListLL(){
		head = null;
		size = 0;
	}
	public boolean add(E item) {
		head = new Node<E>(item, head);
		size++;
		return true;
	}
	public boolean addLast(E item) {
		if(head == null) { //list is empty
			head = new Node<E>(item);
		}else { //list isn't empty
			Node<E> current = head;
			while(current.next != null) {
				current = current.next;
			}
			current.next = new Node<E>(item);
		}
		size++;
		return true;
	}
	public E removeFirst() {
		if(head == null) {
			throw new IllegalArgumentException("List is empty.");
		}else {
		E result = head.data;
		head = head.next;
		size--;
		return result;
		}
	}
	public E removeLast() {
		if(head == null) {
			throw new IllegalArgumentException("List is empty.");
		}if(head.next == null) {
			return this.removeFirst();
		}else {
		Node<E> current = head;
		while(current.next.next != null) {
			current = current.next;
		}
		E result = current.next.data;
		current.next = null;
		size--;
		return result;
		}
	}
	public E remove(int index) {
		if(head == null) {
			throw new IllegalArgumentException("List is empty.");
		}else if(index < 0 || index > size - 1){
			throw new IllegalArgumentException("Index is out of range.");
		}else if(index == 0) {
			return this.removeFirst();
		}
		else {
			
			Node<E> current = head;
			for(int i = 0; i < index - 1; i++) {
				current = current.next;
			}
			E result = current.next.data;
			current.next = current.next.next;
			size--;
			return result;
		}
	}
	
	public String toString() {
		String result = "";
		Node<E> current = head;
		while(current != null) {
			result += ", " + current.data;
			current = current.next;
		}
		return result;
	}
	private boolean isSingleton(Node<E> list) {
		return list != null && list.next == null;
	}
	public boolean isSingleton() {
		return isSingleton(this.head);
	}
	private MyListLL<Pair<E,E>>.Node<Pair<E,E>> zip(Node<E> current1, Node<E> current2){
		if(current1 == null || current2 == null) {
			return null;
		}else { //both lists are not empty
			//return new Node<Pair<E,E>>(); 
			return null;
		}
		
	}
	
	public MyListLL<Pair<E,E>> zip(MyListLL<E> l2){
		MyListLL<Pair<E,E>> r = new MyListLL<Pair<E,E>>();
		r.size = Math.min(size, l2.size);
		r.head = zip(this.head, l2.head);
		return r;
		}
	
	private Node<E> take(int n, Node<E> current){
		if(n == 0 || current == null) {
			return null;
		} else {
			return new Node<E>(current.data, take(n - 1, current.next));
		}

	}
	public MyListLL<E> take(int n){
		MyListLL<E> result = new MyListLL<E>();
		result.size = Math.min(size, n);
		result.head = take(n, head);
		return result;
	}
	
	
}


