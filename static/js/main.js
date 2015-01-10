$(document).ready(function(){
	var small_images = [];    
    var headers_top = [];   
    var headers_top_height = 0;
    var post_title_clone = null;
    var scrollToTopVisible = false;
		
	blog_form_submit = function(event) {
		event.preventDefault();
		$('#' + this.id + ' .submit-post').hide(0);
		$('#' + this.id + ' .sending-post').show(0);		
		headers_data = {}
		
		if(typeof protect != 'undefined') {
			header_name = 'X-P-G-' + protect.name;
			headers_data['X-P-G-' + protect.name] = protect.code;			
		}
		
		$.ajax($(this).attr('action'), { 
			headers:	headers_data,
			type: 		"POST",
			data: 		$(this).serialize(),
			success: 	function(data){
				$('#comment-box').html(data);
				$('#comment-box form').submit(blog_form_submit);
				init_auto_help();
		    }			
		});
		return false;
	}
	
	init_auto_help = function(){
		$('.auto-help span').hide(0);
		$('.auto-help').mouseover(function(event){
			$('#' + this.id + ' span').show(0);
		});
		$('.auto-help').mouseout(function(event){
			$('#' + this.id + ' span').hide(0);
		});
	}
	
	init_blog_comments = function() {
		$('.post').mouseover(function(event){
			$('#' + this.id + '-tags').addClass('active');
		});
		
		$('.post').mouseout(function(event){
			$('#' + this.id + '-tags').removeClass('active');
		});
	}

	$('#comment-box form').submit(blog_form_submit);

	$('.move-top').click(function(){
		$.scrollTo($('body'), 500, {offset: -10});
	});
	
	$('.add-comment').click(function(){
		$.scrollTo($('#comment-box'), 500, {offset: -10});
	});
	
	$('#content p a img').load(function(event){
		event.preventDefault();
		var img = $(this);

		img.removeClass('load');
	});
	
	$('#content p a img').click(function(event){
		event.preventDefault();
		var img = $(this);
		var a = $(this).parent();
		
		img.addClass('load');
		
		if(a.attr('href') == img.attr('src')) {
			img.attr('src', small_images[img.attr('alt')]);
		} else {
			if(!small_images[img.attr('alt')]) {
				small_images[img.attr('alt')] = img.attr('src');
			}	
			img.attr('src', a.attr('href'));
		}	
	});	

	try {
		// Autoresize all textarea
	    $("#content textarea").elastic();
	} catch(error) {}
    
    // Scroll headers
    
    $('#post .title.fixed').each(function () {
    	post_title_clone = $(this);
    	post_title_clone.hide(0);
    });
    
    $(document).scroll(function () {
        var scroll_top = $(document).scrollTop();
        $('#post').each(function () {
            var post = $(this);
            var title = post.find('.title');

            if (scroll_top > post.position().top) {
            	post_title_clone.show(0);
            } else {
            	post_title_clone.hide(0);
            }
        });

        if (scroll_top > 140) {
            show_scroll_top();
        } else {
            hide_scroll_top();
        }
    });

    $('#post h1, #post h2').each(function (id) {
    	var left_side_width = Math.round(($(document).width() - $('#content').width()) / 2);
    	var header = $(this);
    	if (left_side_width > 140) {
	    	headers_top_height += header.height();
	    	headers_top[id] = {};
	    	headers_top[id].top = header.position().top - $('#post .title').height();
	    	headers_top[id].offset = headers_top_height;
	    	headers_top[id].offset_slide = headers_top_height+10;
	    	headers_top[id].clone = header.clone();
            headers_top[id].original = header;
	    	headers_top[id].clone.css({
	    		'position' 	: 'fixed',
	    		'top'		: headers_top[id].offset + 10,
	    		'cursor'	: 'pointer',
	    		'max-width' : left_side_width - 25
	    	});
	    	headers_top[id].clone.addClass('header-clone');
	    	header.after(headers_top[id].clone);
	    	headers_top[id].clone.hide(0);
	    	headers_top[id].clone.css('margin-left', ($('#content').width() + 20));

	    	headers_top[id].clone.click(function(){$.scrollTo(header, 500, {offset: -10});})
    	}
    });
    
    $(document).scroll(function () {
        var scroll_top = $(document).scrollTop();
        $('#post h1:not(header-clone), #post h2:not(header-clone)').each(function (id) {
            var header = $(this);
            if(headers_top[id]) {            	           
	            if (scroll_top > headers_top[id].top) {
	            	headers_top[id].clone.fadeIn(300);
	            	$('#post h1:not(header-clone), #post h2:not(header-clone)').removeClass('active');
	            	headers_top[id].clone.addClass('active');
	            } else {	           	
		            headers_top[id].clone.fadeOut(400);	            	
	            }
            }
        });
    });

    $('#post img').load(function(){
        for(id in headers_top) {
            headers_top[id].top = headers_top[id].original.position().top - $('#post .title').height();
        }
    });

    show_scroll_top = function() {
        var scrollToTop = $('.scroll-to-top');
        if (!scrollToTopVisible && scrollToTop.size() > 0) {
            scrollToTop
                .css({
                    'display': 'block',
                    'height': $(document).height(),
                    'left': scrollToTop.width()*-1
                })
                .animate({
                    left: 0
                  }, 100);

            scrollToTopVisible = true;
        }
    };

    hide_scroll_top = function() {
        var scrollToTop = $('.scroll-to-top');
        if (scrollToTopVisible && scrollToTop.size() > 0) {
            scrollToTop
                .animate({
                    'left': scrollToTop.width() * -1
                }, 100);

            scrollToTopVisible = false;
        }
    };


	init_auto_help();
	init_blog_comments();
});