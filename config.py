from json import dump, load
from os.path import abspath, dirname, join
from random import SystemRandom

basedir = abspath(dirname(__file__))

try:
    settings = load(open(join(basedir, 'booru.json')))
except IOError:
    skey = ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    settings = {'secret_key': skey, 'allowed_extensions': ['gif', 'jpeg', 'jpg', 'png'],
                'content_levels': [[0, 'Pure'], [1, 'Ecchi Sketchy'], [2, 'L-lewd']], 'folder_images': 'booruimg',
                'folder_temp': 'tmp', 'folder_thumbs': 'thumb', 'images_per_page': 20,
                'login_required': {'imagelist': False, 'imageview': False, 'statistics': False, 'upload': True},
                'max_dimensions': (800, 600), 'namespaces': ['artist', 'character', 'series'], 'sitename': 'FlaskBooru'}
    dump(settings, open(join(basedir, 'booru.json'), 'w'))

WTF_CSRF_ENABLED = True
SECRET_KEY = settings['secret_key']

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(basedir, 'app.db')

ALLOWEDTYPES = []
for ext in range(len(settings['allowed_extensions'])):
    ALLOWEDTYPES.append(settings['allowed_extensions'][ext].lower())

CONTENTLEVELS = settings['content_levels']

IMAGEFOLDERNAME = settings['folder_images']
IMAGEFOLDER = join(basedir, "app", "static", IMAGEFOLDERNAME)

IMAGESPERPAGE = settings['images_per_page']

IMAGETEMPNAME = settings['folder_temp']
IMAGETEMP = join(basedir, "app", "static", IMAGETEMPNAME)

LOGINREQUIRED = settings['login_required']

MAXIMAGESIZE = tuple(settings['max_dimensions'])

NAMESPACES = []
for ns in range(len(settings['namespaces'])):
    NAMESPACES.append(settings['namespaces'][ns].lower())

SITENAME = settings['sitename']

THUMBFOLDERNAME = settings['folder_thumbs']
THUMBFOLDER = join(basedir, "app", "static", THUMBFOLDERNAME)