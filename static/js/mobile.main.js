$(document).ready(function(){	
	var small_images = [];    
    var headers_top = [];   
    var headers_top_height = 0;
    var post_title_clone = null;
	
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
	
	hide_all = function() {
		$('#pessimus_content, #realis_content, #optimus_content').hide(0);
		$('#pessimus, #realis, #optimus').removeClass('active');
	}
	
	$('.show_content').click(function(){
		hide_all();
		$('#' + this.id + '_content').show(0);
		$('#' + this.id).addClass('active');		
	})
   
	init_auto_help();
	init_blog_comments();
});