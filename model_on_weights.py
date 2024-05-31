import os
import matplotlib.pyplot as plt
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.utils import array_to_img
from tensorflow.keras import layers
from tensorflow import keras
import tensorflow as tf
import numpy as np


input_dir = "images/images/"
target_dir = "annotations_2/annotations/annotations/trimaps/"
input_img_paths = sorted(
    [os.path.join(input_dir, fname)
    for fname in os.listdir(input_dir)
    if fname.endswith(".jpg")])
target_paths = sorted(
    [os.path.join(target_dir, fname)
    for fname in os.listdir(target_dir)
    if fname.endswith(".png") and not fname.startswith(".")])

#print(input_img_paths)

plt.axis("off")
plt.imshow(load_img(input_img_paths[9]))
plt.show()

def display_target(target_array):
    normalized_array = (target_array.astype("uint8") - 1) * 127
    plt.axis("off")
    plt.imshow(normalized_array[:, :, 0])
    plt.show()
img = img_to_array(load_img(target_paths[9], color_mode="grayscale"))
display_target(img)


img_size = (200, 200)
num_imgs = len(input_img_paths)
print("Общее количество образцов : " + str(num_imgs))
#random.Random(1337).shuffle(input_img_paths)
#random.Random(1337).shuffle(target_paths)
def path_to_input_image(path):
    return img_to_array(load_img(path, target_size=img_size))
def path_to_target(path):
    img = img_to_array(
        load_img(path, target_size=img_size, color_mode="grayscale"))
    img =  img.astype("uint8") - 255
    #print("IMG")
    #print(img)
    #for i in img:
    #   print(i)
    return img
input_imgs = np.zeros((num_imgs,) + img_size + (3,), dtype="float32")
targets = np.zeros((num_imgs,) + img_size + (1,), dtype="uint8")
for i in range(num_imgs):
    input_imgs[i] = path_to_input_image(input_img_paths[i])
    targets[i] = path_to_target(target_paths[i])
    f = tf.shape(targets[i])
    #print("Train_targetS")
    #print(f)
num_val_samples = 350
train_input_imgs = input_imgs[:-num_val_samples]
train_targets = targets[:-num_val_samples]
val_input_imgs = input_imgs[-num_val_samples:]
val_targets = targets[-num_val_samples:]

# 0.46

data_augmentation = keras.Sequential(
 [
 layers.RandomFlip("horizontal"),
 layers.RandomRotation(0.1),
 layers.RandomZoom(0.2),
 ]
)

def get_model(img_size, num_classes):
 inputs = keras.Input(shape=img_size + (3,))
 x = layers.Rescaling(1./255)(inputs)
 x = layers.Conv2D(64, 3, strides=2, activation="relu", padding="same")(inputs)
 x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
 x = layers.Conv2D(128, 3, strides=2, activation="relu", padding="same")(x)
 x = layers.Conv2D(128, 3, activation="relu", padding="same")(x)
 x = layers.Conv2D(256, 3, strides=2, padding="same", activation="relu")(x)
 x = layers.Conv2D(256, 3, activation="relu", padding="same")(x)
 x = layers.Conv2DTranspose(256, 3, activation="relu", padding="same")(x)
 x = layers.Conv2DTranspose(
 256, 3, activation="relu", padding="same", strides=2)(x)
 x = layers.Conv2DTranspose(128, 3, activation="relu", padding="same")(x)
 x = layers.Conv2DTranspose(
 128, 3, activation="relu", padding="same", strides=2)(x)
 x = layers.Conv2DTranspose(64, 3, activation="relu", padding="same")(x)
 x = layers.Conv2DTranspose(
 64, 3, activation="relu", padding="same", strides=2)(x)
 #x = layers.Flatten()(x)
 #x = layers.Dropout(0.5)(x)
 outputs = layers.Conv2D(num_classes, 2, activation="softmax",
 padding="same")(x)
 model = keras.Model(inputs, outputs)
 return model

model = get_model(img_size=img_size, num_classes=2)
model.summary()


model.compile(optimizer="rmsprop",  loss='sparse_categorical_crossentropy', metrics=["accuracy"])

#model.compile(loss='sparse_categorical_crossentropy', optimizer="rmsprop", metrics=['accuracy'])
callbacks = [
 keras.callbacks.ModelCheckpoint("oxford_segmentation.x",  # x => keras
 save_best_only=True)
]
a = tf.shape(train_input_imgs[0])
print("Train_input_imgS")
print(a)
b = tf.shape(train_targets[0])
print("Train_targetS")
print(b)
model_path = "saved_model.pb"

# Загружаем модель
with tf.compat.v1.Session() as sess:
    with tf.io.gfile.GFile(model_path, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def)

# Полный путь к входному тензору
input_tensor = sess.graph.get_tensor_by_name(val_input_imgs[i])

# Полный путь к выходному тензору
output_tensor = sess.graph.get_tensor_by_name(val_input_imgs[i])

# Выполнение предсказаний 
with tf.compat.v1.Session() as sess:
    result = sess.run(output_tensor, feed_dict={input_tensor: val_input_imgs[i]})

model = keras.models.load_model("oxford_segmentation.x")
i = 0
test_image = val_input_imgs[i]
plt.axis("off")
plt.imshow(array_to_img(test_image))
mask = model.predict(np.expand_dims(test_image, 0))[0]
def display_mask(pred):
 mask = np.argmax(pred, axis=-1)
 mask *= 127
 plt.axis("off")
 plt.imshow(mask)
 plt.show()
display_mask(mask)


import matplotlib.pyplot as plt
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, "bo", label="Точность на этапе обучения")
plt.plot(epochs, val_acc, "b", label="Точность на этапе проверки")
plt.title("Точность на этапах обучения и проверки")
plt.legend()
plt.figure()
plt.plot(epochs, loss, "bo", label="Потери на этапе обучения")
plt.plot(epochs, val_loss, "b", label="Потери на этапе проверки")
plt.title("Потери на этапах обучения и проверки")
plt.legend()
plt.show()