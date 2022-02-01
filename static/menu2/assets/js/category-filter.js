// FOR MENU3.HTML

(function($) {

  // Menu filer
  $("#menu-flters li a").click(function() {
    $("#menu-flters li a").removeClass('active');
    $(this).addClass('active');

    var selectedFilter = $(this).data("filter");
    //  $("#menu-wrapper").fadeTo(100, 0);

    $(".menu-restaurant").fadeOut();

    setTimeout(function() {
      $(selectedFilter).slideDown();
      // $("#menu-wrapper").fadeTo(300, 1);
    }, 300);
  });


})(jQuery);
// FOR MENU3.HTML