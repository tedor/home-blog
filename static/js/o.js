$(document).ready(function(){
	hide_all = function() {
		$('#pessimus_content, #realis_content, #optimus_content').hide(0);
		$('#pessimus, #realis, #optimus').removeClass('active');
	}
	
	$('.show_content').click(function(){
		hide_all();
		$('#' + this.id + '_content').show(0);
		$('#' + this.id).addClass('active');
		
	})
});