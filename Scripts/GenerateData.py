from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


datagen = ImageDataGenerator(
    rotation_range=10,
    shear_range=0.3,
    zoom_range=0.2
)

folder = 'Z'
img_name = 'Z280'


img = load_img(f'Data/{folder}/{img_name}.jpg')
x = img_to_array(img)
x = x.reshape((1,)+x.shape)

i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir='../Data/Z', save_prefix='Znew', save_format='jpeg'):
    i += 1
    if i > 5000:
        break
