/* Project specific Javascript goes here. */
$(document).ready(function(){
  $("#mocharBtn").on("click", function(){

    if(verifyInput()){
      $(this).button('<i class="fa fa-spinner fa-spin"></i>');
      $(this).prop('disabled', true);;

      $.ajax({
        method: 'POST',
        url: '/api/v1/links/',
        data: { target_url : $('#targetUrl').val()},
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
          }
        },
        success: function(data){
          console.log(data);

          $("#shortUrl").val(data.short_url);
          $("#shortUrl").attr("readonly", true);

          $("#targetUrlResult").text(data.target_url);
          $("#targetUrlResult").attr("href", data.target_url);

          $("#mocharBtn").button("Mochar");
          $("#mocharBtn").prop('disabled', false);;
          $("#result").show();
        },
        error: function(data){
          console.log(data);
          $("#mocharBtn").button("Mochar");
          $("#mocharBtn").prop('disabled', false);;
        }
      }); 
    } else {
      alert('Input empty!'); 
    } 
  });

  function verifyInput(){
    var result = true;
    if($('#targetUrl').val() === ''){
      result = false;
    } 
    return result;
  }
});

/*
 *nerd copy
 */
function copyToClipboard(){
  var copyInput = $('#shortUrl');
  copyInput.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);

    if (!successful) {
      alt(copyInput.val()); 
    }

    $('.copy-msg').show();
    setTimeout(function() {
      $('.copy-msg').hide();
    }, 5000);

  } catch (err) {
    alt(copyInput.val())
  }

  function alt(value){
    console.log('Oops, unable to copy');
    window.prompt("Copy to clipboard: Ctrl+C, Enter", value);
  }
}
/* helper functions for csfr token in ajax requests */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
