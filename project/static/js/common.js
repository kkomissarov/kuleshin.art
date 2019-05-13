$(document).ready(function() {

	setTimeout(function() { 
		$('.main-description').addClass('active');
		$('.ava').addClass('active');

	}, 300);


	//scroll opacity

	var controller = new ScrollMagic.Controller();

	$('.work-demo').each(function(){
			
		var photoScene = new ScrollMagic.Scene({
			triggerElement: this,
			triggerHook: 0.85, 
			reverse: false
		})
		.setClassToggle(this, 'fade-in')
		// .addIndicators()
		.addTo(controller);

	}); 

	//Фиксированное меню
	var menuScene = new ScrollMagic.Scene({
		triggerElement: '#worksWrapper',
		triggerHook: 0, 
		reverse: true
	})
	.setClassToggle('nav.menu', 'fixed')
	// .addIndicators()
	.addTo(controller);


	//Кнопки переключения в меню
	$('nav.menu button').on('click', function(){
		$('nav.menu button').removeClass('active');
		$(this).addClass('active');
		$('#worksWrapper > .row').removeClass('active');
		$('#'+$(this).data('bounce')).addClass('active');	
	});


	//Создание поста
	$('#add-post').on('click', function(){
		$('.modal-wrapper').css('display', 'flex');
		$('#create-modal').css('display', 'block');
	});

	//Обновление поста
	$('.edit-btn').on('click', function(){
		$('.modal-wrapper').css('display', 'flex');
		$('#update-modal').css('display', 'block');
		$('#update-post-id').attr('value', $(this).data('element'));
	});

	//Удаление поста
	$('.del-btn').on('click', function(){
		$('.modal-wrapper').css('display', 'flex');
		$('#del-modal').css('display', 'block');
		$('#delete-post-id').attr('value', $(this).data('element'));
	});

	//Кнопки отмены
	$('.modal-cancel').on('click', function(){
		$('.modal-wrapper').css('display', 'none');
		$('.custom-modal').css('display', 'none');
	});


});
