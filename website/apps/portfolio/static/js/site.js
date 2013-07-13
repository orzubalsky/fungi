;(function($){
var site = window.site = new function() 
{
    this.init = function() 
    {
        this.galleries();
        this.highlighting();
    };


    this.highlighting = function()
    {
        var self = this;

        // listen to clicks on navigation tags
        $('#tag_navigation a').click(function(e)
        {
            // don't redirect anywhere
            e.preventDefault();
            
            // reset highlight style from all tags
            $('#tag_navigation a').removeClass('highlight');
            
            // highlight the tag that was clicked
            $(this).addClass('highlight');
            
            // get the tag name from the clicked element id
            var tag_name = $(this).attr('id');
            
            // selector for all project anchors
            var projects = $('#project_list a');
            
            // reset hightligt style from all projects
            $(projects).removeClass('highlight');
            
            // iterate over projects to find ones 
            // with the tag that was clicked on
            for(var i=0; i<projects.size(); i++)
            {
                // current project
                var project = $(projects).eq(i);
                
                // highlight a project that has the tag as one of its CSS classes
                if ($(project).hasClass(tag_name))
                {
                    $(project).addClass('highlight');
                }
            }
        });
        
    };

    this.galleries = function()
    {        
        var galleries = $('.gallery');
        
        for (var i=0; i<galleries.size(); i++)
        {
            var gallery = $(galleries).eq(i);
            
            $('.item', gallery).eq(0).show();
        }
        
        $('.next').click(function(e)
        {
            e.preventDefault();
            
            var gallery = $(this).parent().parent();
            var count = $('.item', gallery).size();
            
            var index = $('.item:visible', gallery).index();
            index = (index < count-1) ? index+1 : 0;
            $('.item', gallery).hide();
            $('.item', gallery).eq(index).show();
        });
        $('.back').click(function(e)
        {
            e.preventDefault();
            
            var gallery = $(this).parent().parent();
            var count = $('.item', gallery).size();
            
            var index = $('.item:visible', gallery).index();
            index = (index > 0) ? index-1 : count-1;
            $('.item', gallery).hide();
            $('.item', gallery).eq(index).show();
        });        
    };

    this.ajax_call = function() 
    {
        var self = this;

        $('.button').bind('click', function(e) 
        {
            e.preventDefault();

            var slug = $(this).attr('id');

            Dajaxice.orzubalsky.ajax_load(
                self.ajax_load_callback, 
                {
                    'slug' : slug
                }
            );
        });	
    };


    this.ajax_load_callback = function(data)
    {
        $('#loader').hide();
        $('#dynamic').html(data);
    };
};
})(jQuery);

$(document).ready(function()
{
	site.init();
});		