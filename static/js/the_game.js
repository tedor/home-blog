the_game = function() {
	$("body")
	.queue("fx", function(){
		$('body #content .title').each(function(index){
			var _this = this;
			setTimeout(function(){
				$(_this).addClass('animated fadeOutUp');
			}, index*150);		
		});
		$('body #content .tags').each(function(index){
			var _this = this;
			setTimeout(function(){
				$(_this).addClass('animated fadeOutRight');
			}, index*150);
			
		});
		$(this).dequeue();
	})
	.delay(300)
	.queue("fx", function(){
		$('body #content .blog p').each(function(index){
			var effects = ['fadeOutLeft', 'fadeOutRight'];
			var i = getRandomArbitary(0, effects.length)
			if(index % 2) {
				$(this).addClass('animated ' + effects[0]);
			} else {
				$(this).addClass('animated ' + effects[1]);
			}
		});
		$(this).dequeue();	
	})
	.delay(300)
	.queue("fx", function(){
		$('#page_label').addClass('animated hinge');
		$(this).dequeue();	
	})
	.delay(1000)
	.queue("fx", function(){
		var tadam = $("<div>").text("ТА-ДА-М").css({
			'margin' : '100px 0 0 0'
			,'text-align': 'center'
			,'font-size' : '40px'
		});
		$("body #content").prepend(tadam);
		tadam.addClass('animated tada');

		setTimeout(function(){
			tadam.addClass('animated fadeOutDown');		
		}, 1000);
		$(this).dequeue();
	})
	.delay(1500)
	.queue("fx", function() {	
		var text = "Поздравляю с новым    годом!   Пусть в  новом годуисполнятся256 ваших  желаний!  Улыбнись  :) и иди   бухай   ";
		var colors = ['#6699FF', '#ff0000', '#FFCC33', '#00CC00', '#FFCC33', '#6699FF', '#000000'];
		var index_color = 0;
		var global_blocks = $('<div id="blocks_body">');
		var card_blocks = $('<div id="card_body">').css({
			'position': 'absolute'
			,'width' : '940px'

		});
		var text_blocks = $('<div id="text_body">').css({
			'visibility' : 'hidden'
		});

		global_blocks.append(card_blocks);
		global_blocks.append(text_blocks);

		$('#content').html('');	

		$("body #content").prepend(global_blocks);	

		
		for(var i = 0; i<text.length; i++) {
			// var index_color = getRandomArbitary(0, colors.length);
			index_color++;
			if(index_color >= colors.length) index_color = 0;
			// x = i*100;
			var div = $("<div>").css({			
				'width': '90px'
				,'height' : '90px'
				,'margin' : '-0.5px 2px'
				,'padding' : '0'
				,'display' : 'inline-block'
				,'opacity' : '0'
				,'background-color': colors[index_color]
				,'z-index' : '1000'
				,'cursor' : 'pointer'
			}).addClass('divBlock');
			card_blocks.append(div);		

			var div_text = $("<div>").css({			
				'width': '90px'
				,'height' : '58px'
				,'margin' : '2px 2px'
				,'padding' : '0'
				,'display' : 'inline-block'
				,'z-index' : '100'
				,'vertical-align': 'top'
				,'text-align': 'center'
				,'font-size': '50px'
				,'padding-top': '32px'
			});
			text_blocks.append(div_text);
			if(text[i] != "") div_text.text(text[i]);
		}

		setTimeout(function(){
			text_blocks.css('visibility', 'visible');
		}, 3000);
		$(this).dequeue();
	})
	.queue("fx", function(){
		$('body #content .divBlock').each(function(){
			var _this = this;
			setTimeout(function(){	
				$(_this).css({'opacity' : '1'});
				$(_this).addClass('animated flipInX');
			} , getRandomArbitary(0, 20) * 100);	
		});

		$('body #content .divBlock').mouseleave(function(){
			var _this = this;
			if(!$(_this).hasClass('mouseover')) {
				$(_this).removeClass();
				$(_this).addClass('animated swing mouseover');
				setTimeout(function(){	
					$(_this).removeClass('mouseover');
				}, 1300);
			}
		});
		$('body #content .divBlock').mouseover(function(){
			var _this = this;
			if(!$(_this).hasClass('mouseover')) {
				$(_this).removeClass();
			}
		});

		$('body #content .divBlock').click(function(){
			var _this = this;
			$(_this).unbind('mouseleave');
			$(_this).unbind('mouseover');
			$(_this).removeClass();
			$(_this).addClass('animated hinge');
		});

		$(this).dequeue();

	});
}