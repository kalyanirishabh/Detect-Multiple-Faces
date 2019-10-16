def extract_face(path,image,required_size=(160, 160)):
    """
      This function extract multiple faces from a given image or path of the image using MTCNN 
      and returns array of faces.
    """
    if path!='':
        image=Image.open(path)
    image=image.convert('RGB')
    pixels=asarray(image)
    detector=MTCNN()
    results=detector.detect_faces(pixels)
    face_array=[]
    for i in range(len(results)): # multiple faces
        x1,y1,width,height=results[i]['box']
        x1,y1=abs(x1),abs(y1)
        x2,y2=x1+width,y1+height
        face=pixels[y1:y2,x1:x2]
        image=Image.fromarray(face)
        image=image.resize(required_size)
        face_array.append(asarray(image))
    return face_array
