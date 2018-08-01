import tensorflow as tf
from tensorflow.python.saved_model import tag_constants

graph = tf.Graph()
with graph.as_default():
    with tf.Session() as sess:
        tf.saved_model.loader.load(
            sess,
            [tag_constants.SERVING],
            'LoadingAModel/savepath',
        )
        
        a = graph.get_tensor_by_name('a:0')
        c = graph.get_tensor_by_name('add:0')
        res = sess.run(c, feed_dict={a: 3.0})
        print(res)