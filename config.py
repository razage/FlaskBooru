from os.path import abspath, dirname, join

from yaml import load

basedir = abspath(dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = "a secure string"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(basedir, 'app.db')

# load booru.yml and adjust settings accordingly
with open(join(basedir, 'booru.yml')) as cfg:
    _tmpdata = load(cfg)
    ALLOWEDTYPES = _tmpdata['allowed_extensions']

    CONTENTLEVELS = _tmpdata['content_levels']

    IMAGEFOLDERNAME = _tmpdata['folder_images']
    IMAGEFOLDER = join(basedir, "app", "static", IMAGEFOLDERNAME)

    IMAGESPERPAGE = _tmpdata['images_per_page']

    IMAGETEMPNAME = _tmpdata['folder_temp']
    IMAGETEMP = join(basedir, "app", "static", IMAGETEMPNAME)

    NAMESPACES = _tmpdata['namespaces']

    SITENAME = _tmpdata['sitename']

    THUMBFOLDERNAME = _tmpdata['folder_thumbs']
    THUMBFOLDER = join(basedir, "app", "static", THUMBFOLDERNAME)