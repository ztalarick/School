package queues;

import java.util.NoSuchElementException;

public class QueueLL<E> {
	public class Node<E>{
		private E data;
		Node <E> next;
		Node(E item){
			data = item;
			next = null;
		}
		Node(E item, Node<E> next){
			data = item;
			this.next = next;
		}
	}
	Node<E> front;
	Node<E> rear;
	int size = 0;
	
	QueueLL(){
		this.front = null;
		this.rear = null;
		size = 0;
	}
	public E element() {
		if (size == 0) {
			throw new NoSuchElementException();
		}
			return front.data;
		
	}
	public boolean offer(E item) {
		Node<E> temp = rear;
		rear = new Node<E>(item);
		temp.next = rear;
		if(front == null) {
			front = rear;
		}else {
			temp.next = rear;
		}
		size++;
		return true;
	}
	public E remove(){
		if(size == 0) {
			throw new NoSuchElementException();
		}
		E result = rear.data;
		Node<E> current = front;
		while(current.next.next != null) {
			rear = current.next;
			current = current.next;
		}
		return result;
	}
	public int size() {
		return size;
	}
}
