import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, MaxPooling2D, AveragePooling2D, Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.utils import class_weight
import numpy as np

# Define directories
train_dir = 'C:/Users/Ananya/Desktop/major_prjct/Train'
test_dir = 'C:/Users/Ananya/Desktop/major_prjct/Test'

# Define parameters
batch_size = 16
img_height = 128
img_width = 128

# Image Data Generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

# Calculate class weights to handle class imbalance
classes = train_generator.classes
class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(classes),
    y=classes
)
class_weights = dict(enumerate(class_weights))

# Load the ResNet50 model with pretrained weights and exclude the top layers
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))

# Adding custom layers on top
x = base_model.output
x = Conv2D(256, (3, 3), activation='relu', padding='same')(x)  # Custom convolutional layer
x = MaxPooling2D(pool_size=(2, 2))(x)  # Max pooling
x = Dropout(0.5)(x)  # Dropout for regularization
x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = AveragePooling2D(pool_size=(2, 2))(x)  # Average pooling
x = Dropout(0.5)(x)

# Global Average Pooling
x = GlobalAveragePooling2D()(x)

# Dense layers
x = Dense(1024, activation='relu')(x)  # Increase the dense layer size
x = Dropout(0.5)(x)
x = Dense(512, activation='relu')(x)  # Additional dense layer
x = Dropout(0.5)(x)

# Final output layer
predictions = Dense(3, activation='softmax')(x)  # 3 classes

# Create the final model
model = Model(inputs=base_model.input, outputs=predictions)

# Unfreeze the last few layers of the base model for fine-tuning
for layer in base_model.layers[-10:]:
    layer.trainable = True

# Compile the model with class weights
model.compile(optimizer=Adam(learning_rate=0.00001), loss='categorical_crossentropy', metrics=['accuracy'])

# Define callbacks
checkpoint = ModelCheckpoint('custom_resnet_lung_model.keras', save_best_only=True, monitor='val_loss', mode='min')
early_stopping = EarlyStopping(monitor='val_loss', patience=5, mode='min')

# Train the model with class weights
history = model.fit(
    train_generator,
    epochs=4,
    validation_data=test_generator,
    class_weight=class_weights,
    callbacks=[checkpoint, early_stopping]
)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(test_generator)
print(f"Test loss: {loss:.4f}")
print(f"Test accuracy: {accuracy:.4f}")

# Save the model
model.save('custom_resnet_lung_model.keras')