// showing and hiding main section of a news on click on Read more and Read less
function show_body(obj){
  var hidingClass = 'hide_element';
	var currentObject = obj.currentTarget;
  var newsMainBody = $(currentObject).parent().siblings('section.news_main');
  var readLess = $(newsMainBody).children('a.read_less');

  $(newsMainBody).attr('hidden', false);
  $(currentObject).attr('hidden', true);
  $(readLess).attr('hidden', false);
}

function hide_body(obj){
  var hidingClass = 'hide_element';
	var currentObject = obj.currentTarget;
  var newsMainBody = $(currentObject).parent();
  var readMore = $(newsMainBody).siblings('section.news_intro').children('a.read_more');

  $(newsMainBody).attr('hidden', true);
  $(currentObject).attr('hidden', true);
  $(readMore).attr('hidden', false);
}
