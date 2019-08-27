# _image_library = {}
# def get_image(path):
#         global _image_library
#         image = _image_library.get(path)
#         if image == None:
#                 canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#                 image = pygame.image.load(canonicalized_path)
#                 _image_library[path] = image
#         return image


# _sound_library = {}
# def play_sound(path):
#   global _sound_library
#   sound = _sound_library.get(path)
#   if sound == None:
#     canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#     sound = pygame.mixer.Sound(canonicalized_path)
#     _sound_library[path] = sound
#   sound.play()

# effect = pygame.mixer.Sound('beep.wav')
# effect.play()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

# run_game(400, 300, 60, TitleScene())