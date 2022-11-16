def picture_parameters(typ:str, predmet_len, focus_len):

  if typ == 'sob':

    if predmet_len == 2 * focus_len:
      return 'равное, обратное, действительное'

    elif predmet_len == focus_len:
      return 'изображение в бесконечности'

    elif predmet_len > 2 * focus_len:
      return 'уменьшенное, обратное, действительное'

    elif predmet_len < focus_len:
      return 'увеличенное, прямое, мнимое'

    else:
      return 'увеличенное, обратное, действительное'

  else:
    return 'уменьшенное, прямое, мнимое'

print(picture_parameters('sob', 14, 5))
print(picture_parameters('ras', 21, 5))