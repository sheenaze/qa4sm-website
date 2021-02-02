// showing and hiding main section of a news on click on Read more and Read less
function show_body(obj){
  var currentObject = obj.currentTarget;
  var newsMainBody = $(currentObject).closest('.container').find('section.news_main');

  $(newsMainBody).attr('hidden', false);
  $(currentObject).attr('hidden', true);

}

function hide_body(obj){
  var currentObject = obj.currentTarget;
  var newsMainBody = $(currentObject).closest('section.news_main');
  var readMore = $(newsMainBody).closest('.container').find('a.read_more');

  $(newsMainBody).attr('hidden', true);
  $(readMore).attr('hidden', false);
}
