import keras
from keras.datasets import mnist
from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Dense,Flatten
from keras.models import Sequential


(train_x,train_y),(test_x,test_y) = mnist.load_data()

train_x = train_x.reshape(train_x.shape[0],28,28,1)
test_x  = train_x.reshape(test_x.shape[0],28,28,1)

train_x = train_x / 255
test_x = test_x / 255

train_y = keras.utils.to_categorical(train_y,10)
test_y = keras.utils.to_categorical(test_y,10)

model = Sequential()

model.add(Conv2D(6,kernel_size=(5,5),activation='relu',input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(16,kernel_size=(5,5),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(16,activation='softmax'))

model.compile(loss=keras.metrics.categorical_crossentropy,optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

model.fit(train_x,train_y,batch_size=128,epochs=1,verbose=1,validation_data=(test_x,test_y))

score = model.evaluate(test_x,test_y)

print('误差：%0.4lf' %score[0] )
print('准确率',score[1])