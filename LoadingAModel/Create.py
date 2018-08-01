import tensorflow as tf

with tf.Graph().as_default():
    a = tf.placeholder(tf.float32, name="a")
    b = tf.constant(3.0, name="b")

    c = tf.add(a, b, name="add")

    with tf.Session() as sess:
        result = sess.run(c, feed_dict={a: 3.0})
        print(result)

        inputs = {"a": a}
        outputs = {"prediction": c}

        tf.saved_model.simple_save(
            sess, 'LoadingAModel/savepath', inputs, outputs
        )