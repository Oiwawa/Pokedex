// Index //

$(function() {
  $('#pokedex_logo').hover(function() {
      $('#pokedex_logo').css('background-image', "url('img/pokedex_logo.png')");
      $('#body').css('background-image', "url('img/pokeball_paper.png')");
      $('#body').css('background-position', "center");
  }, function() {
    // on mouseout, reset the background colour
    $('#pokedex_logo').css('background-image', "url('img/pokedex_logo_bw.png')");
    $('#body').css('background-image', 'none');
  });
});



// Home //

$(document).ready(function() {

  // open modal
  $('.grid_container').on('click', '.grid_item', function () {
    $('#modal').css("display", "block")
    $("body").addClass("modal-open")
  });

  // close modal
  $('#modal').on('click', '.modal_close', function () {
    $('#modal').css("display", "none")
    $("body").removeClass("modal-open")
  } );

});

