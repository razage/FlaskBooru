from os.path import abspath, dirname, join

from yaml import load

basedir = abspath(dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = "a secure string"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(basedir, 'app.db')

# load booru.yml and adjust settings accordingly
with open(join(basedir, 'booru.yml')) as cfg:
    _tmpdata = load(cfg)
    ALLOWEDTYPES = []
    for ext in range(len(_tmpdata['allowed_extensions'])):
        ALLOWEDTYPES.append(_tmpdata['allowed_extensions'][ext].lower())

    CONTENTLEVELS = _tmpdata['content_levels']

    IMAGEFOLDERNAME = _tmpdata['folder_images']
    IMAGEFOLDER = join(basedir, "app", "static", IMAGEFOLDERNAME)

    IMAGESPERPAGE = _tmpdata['images_per_page']

    IMAGETEMPNAME = _tmpdata['folder_temp']
    IMAGETEMP = join(basedir, "app", "static", IMAGETEMPNAME)

    LOGINREQUIRED = _tmpdata['login_required']

    MAXIMAGESIZE = tuple(_tmpdata['max_dimensions'])

    NAMESPACES = []
    for ns in range(len(_tmpdata['namespaces'])):
        NAMESPACES.append(_tmpdata['namespaces'][ns].lower())

    SITENAME = _tmpdata['sitename']

    THUMBFOLDERNAME = _tmpdata['folder_thumbs']
    THUMBFOLDER = join(basedir, "app", "static", THUMBFOLDERNAME)