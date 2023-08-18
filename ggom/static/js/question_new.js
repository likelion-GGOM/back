let input, hashtagArray, container, t;

input = document.querySelector('#hashtags');
container = document.querySelector('.tag-container');
hashtagArray = [];

console.log('input =' , input)
input.addEventListener('keydown', (event) => {
  console.log('kkk =' , )
  console.log('event =' , event)
    if (event.which == 38 && input.value.length > 0) {
      var text = document.createTextNode(input.value);
      var p = document.createElement('p');
      container.appendChild(p);
      p.appendChild(text);
      p.classList.add('tag');
      input.value = '';
      
      let deleteTags = document.querySelectorAll('.tag');
      
      for(let i = 0; i < deleteTags.length; i++) {
        deleteTags[i].addEventListener('click', () => {
          container.removeChild(deleteTags[i]);
        });
      }
    }
});

$(document).ready(function(){
  console.log('dkdkdk =' , )
  var fileTarget = $('.file-upload .upload-hidden');

  fileTarget.on('change', function(){
    if(window.FileReader){
      var filename = $(this)[0].files[0].name;
    } 
    else { 
      var filename = $(this).val().split('/').pop().split('\\').pop();
    }
    $(this).siblings('.upload-name').val(filename);
  });
}); 

var imgTarget = $('.preview-image .upload-hidden');

imgTarget.on('change', function(){
  var parent = $(this).parent();
  parent.children('.upload-display').remove();

  if(window.FileReader){
    if (!$(this)[0].files[0].type.match(/image\//)) return;

    var reader = new FileReader();
    reader.onload = function(e){
      var src = e.target.result;
      parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img src="'+src+'" class="upload-thumb"></div></div>');
    }
    reader.readAsDataURL($(this)[0].files[0]);
  }

  else {
    $(this)[0].select();
    $(this)[0].blur();
    var imgSrc = document.selection.createRange().text;
    parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img class="upload-thumb"></div></div>');

    var img = $(this).siblings('.upload-display').find('img');
    img[0].style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(enable='true',sizingMethod='scale',src=\""+imgSrc+"\")";        
  }
});