import os
import shutil
from pathlib import Path

def organizar_archivos(ruta_origen):
    #definir extencion por categoría
    extenciones = {
        'imagenes': ['.jpg','.png','.gif','.jpeg','bmp','webp'],
        'documentos': ['.pdf','.doc','.docx','.txt','.xlsx','.pptx','.ppt','.odt'],
        'peliculas': ['.mp4','.avi','.mkv','.mov','.ts'],
        'audio': ['.mp3','.wav','.flac'],
        'codigo': ['.py','.js','.html','.css','.java','.cpp','.c','.c++','.h'],
        'libros': ['.epub'],
        'apk': ['.apk','.jar'],
        'datos': ['.csv','.sav'],
        'comic': ['.cbr','.djvu'],
        'zip': ['.zip','.msi','.rar','.xz','.7z'],
        'exe': ['.exe'],
        'iso': ['.iso'],
        'otros': ['.crdownload','.jff','README']
        }
    
    #crear categorias si no existen
    for categoria in extenciones.keys():
        carpeta = Path(ruta_origen) / categoria
        carpeta.mkdir(exist_ok=True)
    
    for archivo in os.listdir(ruta_origen):
        if os.path.isfile(os.path.join(ruta_origen, archivo)):
            extension = Path(archivo).suffix.lower()
            
            for categoria, exts in extenciones.items():
                if extension in exts:
                    origen = Path(ruta_origen) / archivo
                    destino = Path(ruta_origen) / categoria / archivo
                    shutil.move(str(origen), str(destino))
                    print(f"Movido: {archivo} -> {categoria}/")
                    break
            
#ejecutar
organizar_archivos("/home/emmagon/Pictures/")
