import tensorflow as tf
# In TF1 use tf.compat.v1.Session

#	==================================================================================================================
#	BASIC Tensor Flow
#	==================================================================================================================
#	
# Creating our first graph computational model
graph1 = tf.Graph()

# COnstant declares a tf.Operation that returns tf.Tensor
with graph1.as_default():
    a = tf.constant([2], name = 'constant_a')
    b = tf.constant([3], name = 'constant_b')

# Printing the value of a
sess = tf.compat.v1.Session(graph = graph1)
result = sess.run(a)
print(result)
sess.close()

# Add function
with graph1.as_default():
    c = tf.add(a, b)
    #c = a + b is also a way to define the sum of the terms

sess = tf.compat.v1.Session(graph = graph1)
result = sess.run(c)
print(result)
sess.close()



#	==================================================================================================================
#	Defining multidimensional arrays using TensorFlow
#	==================================================================================================================

graph2 = tf.Graph()
with graph2.as_default():
    Scalar = tf.constant(2)
    Vector = tf.constant([5,6,2])
    Matrix = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
    Tensor = tf.constant( [ [[1,2,3],[2,3,4],[3,4,5]] , [[4,5,6],[5,6,7],[6,7,8]] , [[7,8,9],[8,9,10],[9,10,11]] ] )

with tf.compat.v1.Session(graph = graph2) as sess:
    result = sess.run(Scalar)
    print ("Scalar (1 entry):\n %s \n" % result)
    result = sess.run(Vector)
    print ("Vector (3 entries) :\n %s \n" % result)
    result = sess.run(Matrix)
    print ("Matrix (3x3 entries):\n %s \n" % result)
    result = sess.run(Tensor)
    print ("Tensor (3x3x3 entries) :\n %s \n" % result)

print(tf.shape)


#	==================================================================================================================
#	Prooves with multidimensional arrays
#	==================================================================================================================

graph3 = tf.Graph()
with graph3.as_default():
    Matrix_one = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
    Matrix_two = tf.constant([[2,2,2],[2,2,2],[2,2,2]])

    add_1_operation = tf.add(Matrix_one, Matrix_two)
    add_2_operation = Matrix_one + Matrix_two

with tf.compat.v1.Session(graph =graph3) as sess:
    result = sess.run(add_1_operation)
    print ("Defined using tensorflow function :")
    print(result)
    result = sess.run(add_2_operation)
    print ("Defined using normal expressions :")
    print(result)


#	==================================================================================================================
#	Prooves with multidimensional arrays and numpy
#	==================================================================================================================
import numpy as np
na = np.array([[1,2,3],[2,3,4],[3,4,5]])

graph31 = tf.Graph()
with graph31.as_default():
	matrix1 = tf.constant(na)
	matrix2 = tf.constant(na*3)
	op1 = matrix2 - matrix1

#	Running the code
with tf.compat.v1.Session(graph = graph31) as sess:
	result = sess.run(op1)
	print("Numpy array as parameter give us: ")
	print(result)
	sess.close()

#	==================================================================================================================
#	Prooves with multidimensional arrays, tf.matmul()
#	==================================================================================================================
graph4 = tf.Graph()
with graph4.as_default():
    Matrix_one = tf.constant([[2,3],[3,4]])
    Matrix_two = tf.constant([[2,3],[3,4]])

    mul_operation = tf.matmul(Matrix_one, Matrix_two)

with tf.compat.v1.Session(graph = graph4) as sess:
    result = sess.run(mul_operation)
    print ("Defined using tensorflow function :")
    print(result)

#	==================================================================================================================
#	Tensor Flow, Variables
#	==================================================================================================================
'''TensorFlow variables are used to share and persistent some stats that are manipulated by our program. That is, when 
you define a variable, TensorFlow adds a tf.Operation to your graph. Then, this operation will store a writable tensor 
value that persists between tf.Session.run calls. So, you can update the value of a variable through each run, while you 
cannot update tensor (e.g a tensor created by tf.constant()) through multiple runs in a session.
How to define a variable?
To define variables we use the command tf.Variable(). To be able to use variables in a computation graph it is necessary 
to initialize them before running the graph in a session. This is done by running tf.global_variables_initializer().

To update the value of a variable, we simply run an assign operation that assigns a value to the variable:
To do this we use the tf.assign(reference_variable, value_to_update) command. tf.assign takes in two arguments,
the reference_variable to update, and assign it to the value_to_update it by.
'''
graph5 = tf.Graph()

with graph5.as_default():
	v = tf.Variable(0)

	# 	Assign
	update = tf.compat.v1.assign(v, v+1)

	#	Variables must be initialized by running an initialization operation after having launched the graph. 
	#	We first have to add the initialization operation to the graph:
	init_op = tf.compat.v1.global_variables_initializer()

#	We then start a session to run the graph, first initialize the variables, then print the initial value of the 
#	state variable, and then run the operation of updating the state variable and printing the result after each update:
with tf.compat.v1.Session(graph = graph5) as session:
    session.run(init_op)
    print(session.run(v))
    for _ in range(3):
        session.run(update)
        print(session.run(v))
    session.close()


#	==================================================================================================================
#	Tensor Flow, Placeholders
#	==================================================================================================================
'''
Now we know how to manipulate variables inside TensorFlow graph, but what about feeding data outside of a TensorFlow graph?
If you want to feed data to a TensorFlow graph from outside a graph, you will need to use placeholders.
So what are these placeholders and what do they do?
Placeholders can be seen as "holes" in your model, "holes" which you will pass the data to, you can create them using
tf.placeholder(datatype), where datatype specifies the type of data (integers, floating points, strings, booleans) along with 
its precision (8, 16, 32, 64) bits.
'''
graph6 = tf.Graph()

#	Init
with graph6.as_default():
	a = tf.compat.v1.placeholder(tf.float32)
	b = a * 2

#	Use
with tf.compat.v1.Session(graph = graph6) as sess:
	result = sess.run(b, feed_dict = {a:3.5})
	print("Result of graph6: ",result)
	sess.close()

# 	Also we can feed with arrays
dictionary={a:[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
			[[13,14,15],[16,17,18],[19,20,21],[22,23,24]]]}

with tf.compat.v1.Session(graph = graph6) as sess:
    result = sess.run(b,feed_dict=dictionary)
    print ("Result of Graph6 with arrays: \n",result)
    sess.close()



#	==================================================================================================================
#	Tensor Flow, Other operations
#	==================================================================================================================
graphEND = tf.Graph()
with graphEND.as_default():
    a = tf.constant([5])
    b = tf.constant([2])
    c = tf.add(a,b)
    d = tf.subtract(a,b)
    e = tf.nn.sigmoid(1.25)

with tf.compat.v1.Session(graph = graphEND) as sess:
    result = sess.run(c)
    print ('c =: %s' % result)
    result = sess.run(d)
    print ('d =: %s' % result)
    result = sess.run(e)
    print('e =: %s' % result)