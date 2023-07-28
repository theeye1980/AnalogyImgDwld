import os
from transliterate import translit

def cyrillic_to_latin(text):
    latin_text = translit(text, 'ru', reversed=True)
    return latin_text

def image_data_with_features_pkl(model_name, cat):
    cat=cyrillic_to_latin(cat)
    cat=cat.replace(' ','-')
    image_data_with_features_pkl = os.path.join(f'{cat}/','metadata-files/',f'{model_name}/','image_data_features.pkl')
    return image_data_with_features_pkl

def image_features_vectors_idx(model_name, cat):
    cat = cyrillic_to_latin(cat)
    cat = cat.replace(' ', '-')
    image_features_vectors_idx = os.path.join(f'{cat}/','metadata-files/',f'{model_name}/','image_features_vectors.idx')
    return image_features_vectors_idx
