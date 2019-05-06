import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten

def iniciar_modelo():
    model = Sequential()
    return model

def definir_modelo(model, numeroClases):
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(128,128,3))))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(numeroClases, activation='softmax'))
    return model

def compilar_modelo(optimizador, loss, metrics, model):
    model.compile(optimizer=optimizador, loss=loss, metrics=[metrics])
    model.summary()
    return model

def fitModel(model, train_data, train_labels_one_hot, epochs, batch_size, test_data, test_labels_one_hot, URLbase):
    model.fit(train_data, train_labels_one_hot,epochs=epochs ,batch_size=batch_size, verbose=1, validation_data=(test_data, test_labels_one_hot))
    model.save(URLbase+'/modelo.h5')
