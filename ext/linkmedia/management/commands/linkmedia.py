from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = """
Removes all symlinks in MEDIA_ROOT and then scans all installed applications for a media folder to symlink to MEDIA_ROOT.

If installed app has a media folder, it first attempts to symlink the contents
    ie:   app/media/app_name -> MEDIA_ROOT/app_name
    
If the symlink name already exists, it assumes the media directory is not subfoldered and attempts:
    ie:  app/media -> MEDIA_ROOT/app_name"""
    
    def handle_noargs(self, **options):
        from django.conf import settings
        import os
        
        media_path = settings.MEDIA_ROOT
        for d in os.listdir(media_path):
            path = os.path.join(media_path,d)
            if os.path.islink(path):
                os.remove(os.path.join(path))
                print " - removed %s" % path
        
        for app in settings.INSTALLED_APPS:
            app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
            if 'media' in os.listdir(app_path[0]) and os.path.isdir(os.path.join(app_path[0],'media')):
                app_media = os.path.join(app_path[0],'media')
                try:
                    os.symlink(app_media, os.path.join(media_path,app.split('.')[-1]))
                    print " + added %s as %s" % (app_media, os.path.join(media_path,app.split('.')[-1]))
                except OSError,e:
                     print "ERROR: cannot add media from %s" % app
