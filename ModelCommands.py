import tensorflow as tf

model = tf.saved_model.load('one_step')

def predict_text(text, length):
    length = int(length)

    states = None
    text = text[:-1] # gets rid of the added newline
    text = tf.constant([text])
    result = [text]

    for _ in range(length):
      text, states = model.generate_one_step(text, states=states)
      result.append(text)

    result = tf.strings.join(result)
    extended = result[0].numpy().decode('utf-8')
    return extended

def predict_letter(text):
    states = None
    text = tf.constant([text])
    result = [text]

    text, states = model.generate_one_step(text, states=states)
    result.append(text)

    result = tf.strings.join(result)
    extended = result[0].numpy().decode('utf-8')
    return extended

def extend_text(prompt, length_scale, updateColor):
  text = prompt.get("1.0", "end")
  print(text)
  print("\n\n" in text)
  prompt.delete("1.0", "end")
  prompt.insert("1.0", predict_text(text, length_scale.get()))
  updateColor()
