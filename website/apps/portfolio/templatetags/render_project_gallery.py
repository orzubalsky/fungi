from django import template

register = template.Library()

def render_project_gallery(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        args = token.split_contents()
        if len(args) == 2:
            tag_name, project = args

    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires two arguments" % token.contents.split()[0]

    return RenderProjectGalleryNode(project)

class RenderProjectGalleryNode(template.Node):
    def __init__(self, project):
        self.project = template.Variable(project)

    def render(self, context):
        project = self.project.resolve(context)
        
        if project.gallery_style == 'slideshow':
            template_name = 'render_gallery_slideshow.html'
        elif project.gallery_style == 'list':
            template_name = 'render_gallery_list.html'
        elif project.gallery_style == 'thumbnails':
            template_name = 'render_gallery_thumbnails.html'
                
        context['project'] = project
        
        t = template.loader.get_template(template_name)
        
        html = t.render(context)

        return html


register.tag('render_project_gallery', render_project_gallery)