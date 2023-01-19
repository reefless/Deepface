from deepface import DeepFace
import pandas as pd

df = DeepFace.find(img_path="James12.jpg", db_path="./user/database",
                   model=DeepFace.build_model('Facenet512'))
# print(df.size())

DeepFace.stream(db_path="./user/database")
