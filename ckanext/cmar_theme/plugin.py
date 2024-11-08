import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation

def latest_datasets(count=9):
    datasets = toolkit.get_action('package_search')(
            {}, {'sort': 'metadata_created desc', 'rows': count,
                 'fl': 'name,title,notes,metadata_created'}
        )

    return datasets['results']

class CmarThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    
    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "cmar_theme")

    
    def get_helpers(self):
        return {'cmar_theme_latest_datasets': latest_datasets}