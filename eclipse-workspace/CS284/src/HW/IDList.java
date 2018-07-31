package HW;

import java.util.ArrayList;
/**
 * 
 * @author Zachary Talarick
 *
 * @param <E> Any type.
 */
public class IDList<E> {
	/**
	 * 
	 * @author Zach
	 *
	 * @param <E> Any type
	 */
	@SuppressWarnings("hiding")
	public class Node<E>{
		//data fields
		E data;
		Node<E> next;
		Node<E> prev;
		/**
		 * Constructor
		 * @param elem same as data
		 */
		Node(E elem){
			data = elem;
		}
		/**
		 * This is another constructor
		 * @param elem is data
		 * @param prev is the one before
		 * @param next is the one after
		 */
		Node(E elem, Node<E> prev, Node<E> next){
			data = elem;
			this.next = next;
			this.prev = prev;
		}
		
	}
	//data fields
	private Node<E> head;
	private Node<E> tail;
	int size = 0;
	ArrayList<Node<E>> indices;
	/**
	 * Construtor
	 */
	public IDList(){
		indices = new ArrayList<Node<E>>(0); //I don't know what this is I don't keep track of it.
		head = null;
		tail = null;
	}
	/**
	 * adds at an index
	 * @param index the location of add where you want to add something.
	 * @param elem the data
	 * @return true when successfully added
	 */
	public boolean add(int index, E elem) {
		if(index > size) {
			throw new IllegalArgumentException("The index is greater than the size");
		}
		
		Node<E> current = head;
		
		if(head == null || index == 0) {
			head = new Node<E>(elem);
			head.next = current;
			size++;
			return true;
		}
		if(size == index) {
		tail = new Node<E>(elem);
		}
	
		int i = 0;
		while(i < index - 1) {
			current = current.next;
			i++;
			}
		Node<E> temp = current.next;
		current.next = new Node<E>(elem, current.prev, temp);
		size++;
		//current.prev = current.next;
		/**
		Node<E>temp = new Node<E>(elem, current, current.next);
		current.next = temp;
		current.next.prev = temp;
		size++;
		**/
		return true;
	}
	/**
	 * adds at the head or beginning
	 * @param elem the data you want stored
	 * @return true when successfully added
	 */
	public boolean add(E elem) {
		add(0, elem);
		return true;
	}
	/**
	 * adds last, at the end
	 * @param elem the data
	 * @return true when successfully added
	 */
	public boolean append(E elem){
		add(size, elem);
		return true;
	}
	/**
	 * string representation, the string override 
	 */
	public String toString() {
		String r = "";
		Node<E> current = head;
		while(current != null) {
			r += ", " + current.data;
			current = current.next;
		}
		return r;	
	}
	/**
	 * gets the data at the index
	 * @param index the location of the data
	 * @return the data at index
	 */
	public E get(int index){
		Node<E> current = head;
		int i = 0;
		while(i < index) {
			current = current.next;
			i++;
			}
	
		
		return current.data;
	}
	/**
	 * gets the data at the head
	 * @return the data at the head
	 */
	public E getHead() {
		return head.data;
	}
	/**
	 * gets the data at the tail
	 * @return the data at the tail
	 */
	public E getTail() {
		return tail.data;
	}
	/**
	 * how big the linked list is
	 * @return the size
	 */
	public int size() {
		return size;
	}
	/**
	 * removes the head
	 * @return temperary varriable for the data at the head
	 */
	public E remove() {
		E temp = head.data;
		head = head.next;
		return temp;
	}
	/**
	 * removes the tail
	 * @return temperary varriable for the data at the tail
	 */
	public E removeLast() {
		E temp = tail.data;
		Node<E> current = head;
		int i = 0;
		while(i < size - 1) {
			current = current.next;
			i++;
			}
		tail = current;
		current.next = null;
		size--;
		return temp;
	}
	/**
	 *  removes data at an index
	 * @param index is location of the data
	 * @return temperary variable for the data at the index
	 */
	public E removeAt(int index) {
		int i = 0;
		Node<E> current = head;
		while(i < index) {
			current = current.next;
			i++;
		}
		E temp = current.data;
		current.prev = current.next;
		return temp;
	}
	/**
	 * removes elem from the list
	 * @param elem is the data
	 * @return true if found and removed false if not found
	 */
	public boolean remove(E elem) {
    int i = 0;
    Node<E> current = head;
    while(i < size) {
    	if(current.data == elem) {
    		current.prev = current.next;
    		Node<E> current2 = head;
    		int j = 0;
    		while(j < i - 1) {
    			current2 = current2.next;
    			j++;
    		}
    		current2.next = current2.next.next;
    		i--;
    		return true;
    	}
    	current = current.next;
    	i++;
    }
    return false;
	}
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void main(String[] args) {
		IDList test = new IDList();
		test.add("2");
		System.out.println(test);
		test.add("1");
		System.out.println(test);
		test.append("3");
		System.out.println(test);
		test.append("4");
		System.out.println(test);
		test.add(4, "5");
		System.out.println(test);
		System.out.println(test.get(4));
		System.out.println(test.getTail());
		System.out.println(test.size());
		System.out.println(test.remove("4"));
		System.out.println(test);
		
	}
}