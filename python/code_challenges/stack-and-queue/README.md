# Stacks and Queues
### Stask :
 + Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out)

### Queue

+ Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

## Challenge
## Stacks and Queues
Features
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
## Stack
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:

+ push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

+ pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

+ peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

+ is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.
## Queue
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:

+ enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

+ dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

+ peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack

+ is empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty
You have access to the Node class and all the properties on the Linked List class.

## Approach & Efficiency
### Stack
`push()`, `pop()`, `isEmpty()` and `peek()` all take O(1) time.

### Queue
`Enque()`, `Deque()`,`isEmpty()`, `peek()` all take O(1) time.



## API
### Stack Methods :

`PUSH `
Push  refers to inserting an element in the stack. Since there’s only one position at which the new element can be inserted — Top of the stack, the new element is inserted at the top of the stack.

`POP `
Pop  refers to the removal of an element. Again, since we only have access to the element at the top of the stack, there’s only one element that we can remove. We just remove the top of the stack. Note: We can also choose to return the value of the popped element back, its completely at the choice of the programmer to implement this.

`PEEK `
Peek  allows the user to see the element on the top of the stack.

`isEmpty` Check if stack is empty or not.

### Queue Methods :

`Enqueue` Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.

`Dequeue` Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.


`PEEK `
Peek  allows the user to see the element on the fornt of the queue .

`isEmpty` Check if queue is empty or not.




