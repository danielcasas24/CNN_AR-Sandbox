import Datos as dt
import Modelo as md

URLdatos = 'URL/donde/estan/los/datos'
carpetas = ['carpeta 1', 'carpeta 2', '...', 'carpeta N']
numero_clases = len(carpetas)
optimizador = 'RMSprop'
loss = 'categorical_crossentropy'
metrics = 'accuracy'
epochs = 10
batch_size = 32
URLguardado = 'URL/donde/se/guarda/el/modelo'
datos_entrenamiento, datos_prueba = dt.cargar_datos(URLdatos,carpetas)
target_entrenamiento, target_prueba = dt.generar_target(carpetas)
datos_entrenamiento, target_entrenamiento, datos_prueba, target_prueba = procesar_datos(datos_entrenamiento,
                                                                                        target_entrenamiento,
                                                                                        datos_prueba,
                                                                                        target_prueba)


modelo = md.iniciar_modelo()
modelo = definir_modelo(modelo)
modelo = definir_modelo(modelo, num_classes)
modelo = compilar_modelo(optimizador, loss, metrics, model)
modelo = fit_model(modelo, datos_entrenamiento, target_entrenamiento,
                   epochs, batch_size, datos_prueba, target_prueba,URLguardado)
