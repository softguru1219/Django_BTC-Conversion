// Mobile menu

$('[js-open-menu]').on('click', function(){
  $('.header__mobile-menu').addClass('is-active');
  $('body').addClass('no-scroll');
});
$('[js-close-menu]').on('click', function(){
  $('.header__mobile-menu').removeClass('is-active');
  $('body').removeClass('no-scroll')
});

// FAQs
$('.faq__item').on('click', function(){
  if ($(this).hasClass('is-active')) {
    $(this).removeClass('is-active');
    $(this).next('.faq__more').slideUp(200).removeClass('is-open');
  } else {
    $('.faq__item').removeClass('is-active');
    $('.faq__more').slideUp(200).removeClass('is-open');
    $(this).addClass('is-active');
    $(this).next('.faq__more').slideDown(200).addClass('is-open');
  }
});

// Active page
 $('.header a').each(function(i, val) {
    if ($(val).attr('href') == window.location.pathname.split('/').pop()) {
      $(val).addClass('is-active');
    } else {
      $(val).removeClass('is-active')
    }
  });